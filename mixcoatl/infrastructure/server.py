from mixcoatl.resource import Resource
from mixcoatl.admin import job
from mixcoatl.utils import wait_for_job
from mixcoatl.utils import camel_keys
from mixcoatl.decorators.validations import required_attrs
from mixcoatl.decorators.lazy import lazy_property

import json


class Server(Resource):
    path = 'infrastructure/Server'
    collection_name = 'servers'
    primary_key = 'server_id'

    def __init__(self, server_id = None, *args, **kwargs):
        self.collection_name = self.__class__.collection_name
        Resource.__init__(self)
        self.__server_id = server_id

    @property
    def server_id(self):
        '''The immutable enStratus ID of this server'''
        return self.__server_id

    @lazy_property
    def agent_version(self):
        return self.__agent_version

    @lazy_property
    def cloud(self):
        '''The id of the cloud where the instance is located'''
        return self.__cloud

    @lazy_property
    def label(self):
        return self.__label

    @label.setter
    def label(self, l):
        self.__label = l

    @lazy_property
    def customer(self):
        return self.__customer

    @lazy_property
    def data_center(self):
        '''The id of the specific datacenter where the instance is located.'''
        return self.__data_center

    @data_center.setter
    def data_center(self, d):
        self.__data_center = {u'data_center_id':d}

    @lazy_property
    def description(self):
        return self.__description

    @description.setter
    def description(self, d):
        self.__description = d

    @lazy_property
    def machine_image(self):
        return self.__machine_image

    @machine_image.setter
    def machine_image(self, m):
        self.__machine_image = {u'machine_image_id':m}

    @lazy_property
    def firewalls(self):
        return self.__firewalls

    @firewalls.setter
    def firewalls(self, f):
        self.__firewalls = f

    @lazy_property
    def name(self):
        return self.__name

    @name.setter
    def name(self, n):
        self.__name = n

    @lazy_property
    def owning_groups(self):
        return self.__owning_groups

    @lazy_property
    def owning_user(self):
        return self.__owning_user

    @lazy_property
    def platform(self):
        return self.__platform

    @lazy_property
    def private_ip_addresses(self):
        return self.__private_ip_addresses

    @lazy_property
    def public_ip_address(self):
        return self.__public_ip_address

    @lazy_property
    def region(self):
        return self.__region

    @lazy_property
    def provider_product_id(self):
        return self.__provider_product_id

    @provider_product_id.setter
    def provider_product_id(self, id):
        self.__provider_product_id = id

    @lazy_property
    def provider_id(self):
        return self.__provider_id

    @lazy_property
    def product(self):
        return self.__product

    @lazy_property
    def start_date(self):
        return self.__start_date

    @lazy_property
    def status(self):
        return self.__status

    @lazy_property
    def budget(self):
        return self.__budget

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

    @required_attrs(['provider_product_id', 'machine_image', 'description', 'name','data_center'])
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
                        'dataCenter': camel_keys(self.data_center)
                    }]}

        for oa in optional_attrs:
            try:
                if getattr(self, oa) is not None:
                    payload['launch'][0].update(camel_keys({oa:getattr(self, oa)}))
            except AttributeError:
                pass

        s = self.post(data=json.dumps(payload))
        if callback is not None:
            callback(s)
        else:
            return s

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
