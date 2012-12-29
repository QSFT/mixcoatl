from mixcoatl.resource import Resource
from mixcoatl.admin import job
from mixcoatl.utils import wait_for_job
from mixcoatl.utils import camel_keys
from mixcoatl.decorators.validations import required_attrs
from mixcoatl.decorators.lazy import lazy

import json


@lazy(key='server_id')
class Server(Resource):
    path = 'infrastructure/Server'
    collection_name = 'servers'

    def __init__(self, server_id = None, *args, **kwargs):
        self.collection_name = self.__class__.collection_name
        Resource.__init__(self)
        if server_id is None:
            self.__server_id = None
            self.__cloud = None
            self.__datacenter = None
            self.__region = None
            self.__status = None
            self.__name = None
            self.__platform = None
            self.__budget = None
            self.__start_date = None
            self.__label = None
            self.__customer = None
            self.__description = None
            self.__firewalls = None
            self.__private_ip_addresses = None
            self.__public_ip_address = None
            self.__owning_groups = None
            self.__owning_user = None
            self.__product_id = None
            self.__provider_product_id = None
            self.__keypair = None
            self.__agent_version = None
            self.__machine_image = None
            self.__provider_id = None
            self.__keypair = None
        else:
            self.__server_id = server_id


    @property
    def server_id(self):
        '''The immutable enStratus ID of this server'''
        return self.__server_id

    @server_id.setter
    def server_id(self, sid):
        self.__server_id = sid

    @property
    def cloud(self):
        '''The id of the cloud where the instance is located'''
        return self.__cloud

    @cloud.setter
    def cloud(self, c):
        self.__cloud = c

    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, label):
        self.__label = label

    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, c):
        self.__customer = c

    @property
    def datacenter(self):
        '''The id of the specific datacenter where the instance is located.'''
        return self.__datacenter

    @datacenter.setter
    def datacenter(self, dc):
        self.__datacenter = dc

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, desc):
        self.__description = desc

    @property
    def machine_image(self):
        return self.__machine_image

    @machine_image.setter
    def machine_image(self, mi):
        self.__machine_image = mi

    @property
    def firewalls(self):
        return self.__firewalls

    @firewalls.setter
    def firewalls(self, fw):
        self.__firewalls = fw

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, n):
        self.__name = n

    @property
    def owning_groups(self):
        return self.__owning_groups

    @owning_groups.setter
    def owning_groups(self, og):
        self.__owning_groups = og

    @property
    def owning_user(self):
        return self.__owning_user

    @owning_user.setter
    def owning_user(self, ou):
        self.__owning_user = ou

    @property
    def platform(self):
        return self.__platform

    @property
    def private_ip_addresses(self):
        return self.__private_ip_addresses

    @private_ip_addresses.setter
    def private_ip_addresses(self, ip_list):
        self.__private_ip_addresses = ip_list

    @property
    def public_ip_address(self):
        return self.__public_ip_address

    @public_ip_address.setter
    def public_ip_address(self, ip):
        self.__public_ip_address = ip

    @property
    def region(self):
        return self.__region

    @region.setter
    def region(self, r):
        self.__region = r

    @property
    def platform(self):
        return self.__platform

    @platform.setter
    def platform(self, p):
        self.__platform = p

    @property
    def product_id(self):
        return self.__product_id

    @product_id.setter
    def product_id(self, pid):
        self.__product_id = pid

    @property
    def provider_product_id(self):
        return self.__provider_product_id

    @provider_product_id.setter
    def provider_product_id(self, ppid):
        self.__provider_product_id = ppid

    @property
    def provider_id(self):
        return self.__provider_id

    @provider_id.setter
    def provider_id(self, pid):
        self.__provider_id = pid

    @property
    def start_date(self):
        return self.__start_date

    @start_date.setter
    def start_date(self, date):
        self.__start_date = date

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, s):
        self.__status = s

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, bid):
        self.__budget = bid

    @property
    def keypair(self):
        return self.__keypair

    @keypair.setter
    def keypair(self, kp):
        self.__keypair = kp

    def reload(self):
        if self.server_id is not None:
            self.load()
        elif self.current_job is None:
            self.load()
        else:
            if wait_for_job(self.current_job):
                self.server_id = job.get(self.current_job)['message']
                self.load()
            else:
                return self.last_error

    @required_attrs(['server_id'])
    def destroy(self, reason='no reason provided'):
        p = self.path+"/"+str(self.server_id)
        qopts = {'reason':reason}
        return self.delete(p, params=qopts)

    @required_attrs(['server_id'])
    def pause(self, reason=None):
        p = '%s/%s' % (self.path, str(self.server_id))
        payload = {'pause':[{}]}

        if reason is not None:
            payload['pause'][0].update({'reason':reason})

        return self.put(p, data=json.dumps(payload))

    @required_attrs(['provider_product_id', 'machine_image', 'description', 'name','datacenter'])
    def launch(self, callback=None):
        optional_attrs = ['firewalls','keypair', 'label']
        if self.server_id is not None:
            raise ServerLaunchException('Cannot launch an already running server: %s' % self.server_id)

        payload = {'launch':
                    [{
                        'productId': self.provider_product_id,
                        'machineImage': camel_keys(self.machine_image),
                        'description': self.description,
                        'name': self.name,
                        'dataCenter': camel_keys(self.datacenter)
                    }]}

        for oa in optional_attrs:
            if getattr(self, oa) is not None:
                payload['launch'][0].update(camel_keys({oa:getattr(self, oa)}))

        self.post(data=json.dumps(payload))

    def duplicate(self, server):
        pass

    @classmethod
    def all(cls):
        r = Resource(cls.path)
        s = r.get()
        if r.last_error is None:
            return [cls(server['serverId']) for server in s[cls.collection_name]]
        else:
            return r.last_error

class ServerException(BaseException): pass
class ServerLaunchException(ServerException): pass
