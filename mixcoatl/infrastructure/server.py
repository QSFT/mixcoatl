from mixcoatl.resource import Resource
from mixcoatl.admin.job import Job
from mixcoatl.utils import camel_keys
from mixcoatl.decorators.validations import required_attrs
from mixcoatl.decorators.lazy import lazy_property

import json


class Server(Resource):
    """A server is a virtual machine running within a data center."""

    path = 'infrastructure/Server'
    collection_name = 'servers'
    primary_key = 'server_id'

    def __init__(self, server_id=None, *args, **kwargs):
        self.collection_name = self.__class__.collection_name
        Resource.__init__(self)
        self.__server_id = server_id

    @property
    def server_id(self):
        """`int` - The enStratus ID of this server. *Immutable*"""

        return self.__server_id

    @lazy_property
    def agent_version(self):
        """`int` - The version of the enStratus agent if installed. *Immutable*"""

        return self.__agent_version

    @lazy_property
    def cloud(self):
        """`dict` - The cloud provided where the instance is located. _*Immutable*_"""

        return self.__cloud

    @lazy_property
    def label(self):
        """`str` - The label assigned to the server"""

        return self.__label

    @label.setter
    def label(self, l):
        self.__label = l

    @lazy_property
    def customer(self):
        """`dict` - The customer account for the server. *Immutable*"""

        return self.__customer

    @lazy_property
    def data_center(self):
        """`dict` - The specific datacenter where the instance is located."""

        return self.__data_center

    @data_center.setter
    def data_center(self, d):
        self.__data_center = {u'data_center_id': d}

    @lazy_property
    def description(self):
        """The description of the server"""

        return self.__description

    @description.setter
    def description(self, d):
        self.__description = d

    @lazy_property
    def machine_image(self):
        """`dict` - The machine image to use/used to provision the server"""

        return self.__machine_image

    @machine_image.setter
    def machine_image(self, m):
        self.__machine_image = {u'machine_image_id': m}

    @lazy_property
    def firewalls(self):
        """`list` - The firewalls to assign/assigned to the server"""

        return self.__firewalls

    @firewalls.setter
    def firewalls(self, f):
        self.__firewalls = f

    @lazy_property
    def name(self):
        """`str` - The name assigned/to assign to the server"""

        return self.__name

    @name.setter
    def name(self, n):
        self.__name = n

    @lazy_property
    def owning_groups(self):
        """`list` - The enStratus groups owning the server. *Immutable*"""

        return self.__owning_groups

    @lazy_property
    def owning_user(self):
        """`dict` - The enStratus user owning the server. *Immutable*"""

        return self.__owning_user

    @lazy_property
    def platform(self):
        """`str` - The platform of the server *(i.e. `UBUNTU`)*. *Immutable*"""

        return self.__platform

    @lazy_property
    def private_ip_addresses(self):
        """`list` - The private ip addresses assigned to the server. *Immutable*"""

        return self.__private_ip_addresses

    @lazy_property
    def public_ip_address(self):
        """`str` - The public ip address of the server. *Immutable*"""

        return self.__public_ip_address

    @lazy_property
    def region(self):
        """`dict` - The region where the server is located"""

        return self.__region

    @lazy_property
    def provider_product_id(self):
        """`str` - The provider's product identifier for the server *(i.e. `m1.large`)*"""

        return self.__provider_product_id

    @provider_product_id.setter
    def provider_product_id(self, id):
        self.__provider_product_id = id

    @lazy_property
    def provider_id(self):
        """`str` - The provider's identifier for the server *(i.e. `i-abcdefg`)* *Immutable*"""

        return self.__provider_id

    @lazy_property
    def product(self):
        """The enStratus product record for the server"""

        return self.__product

    @lazy_property
    def start_date(self):
        """`str` - The date the server was started"""

        return self.__start_date

    @lazy_property
    def status(self):
        """`str` - The status of the server *(i.e. `RUNNING` or `PAUSED`)*. *Immutable*"""

        return self.__status

    @lazy_property
    def budget(self):
        """`int` - The budget code to apply/applied to the server."""

        return self.__budget

    @property
    def keypair(self):
        """`str` - The keypair to assign

            .. note::
                enStratus does not track keypairs used to launch servers.
                This attribute is used only in the `launch()` call.
        """

        return self.__keypair

    @keypair.setter
    def keypair(self, kp):
        self.__keypair = kp

    def reload(self):
        """Reload resource data from API calls"""

        if self.server_id is not None:
            self.load()
        elif self.current_job is None:
            self.load()
        else:
            if Job.wait_for(self.current_job):
                self.__server_id = job.get(self.current_job)['message']
                self.load()
            else:
                return self.last_error

    @required_attrs(['server_id'])
    def destroy(self, reason='no reason provided'):
        """Terminate server instance with reason :attr:`reason`

        :param reason: The reason for terminating the server
        :type reason: str.
        :returns: bool -- Result of API call
        """
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

    # TODO: Refactor this a bit. We should be raising exceptions instead of 
    # this madness of returning the last error. Makes no sense. I should have
    # never done it.
    @required_attrs(['provider_product_id', 'machine_image', 'description',
                    'name', 'data_center'])
    def launch(self, callback=None):
        """Launches a server with the configured parameters

        >>> def cb(j): print(j)
        >>> s = Server()
        >>> s.provider_product_id = 'm1.large'
        >>> s.machine_image = 12345
        >>> s.description = 'my first launch'
        >>> s.name = 'server-1-test'
        >>> s.data_center = 54321
        >>> s.keypair = 'my-aws-keypair'
        >>> s.launch(callback=cb)

        :param callback: Optional callback to send the results of the API call
        :type callback: func.
        :returns: int -- The job id of the launch request
        :raises: :class:`ServerLaunchException`, :class:`mixcoatl.decorators.validations.ValidationException`
        """
        optional_attrs = ['firewalls', 'keypair', 'label']
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
        if self.last_error is None:
            if callback is not None:
                callback(s)
            else:
                return s
        else:
            raise ServerLaunchException(self.last_error)

    def duplicate(self, server):
        pass

    def wait_for(self, status='RUNNING', callback = None):
        """Blocks execution until the current server has status of :attr:`status`

        :param status: The status to expect before continuing *(i.e. `RUNNING` or `PAUSED`)*
        :type status: str.
        :param callback: Optional callback to be called with the final :class:`Server`` when ``status`` is reached
        :type callback: func.
        :raises: `ServerException`
        """
        if self.server_id is None:
            raise ServerException('Must be called with an existing server.')
        initial_status = self.status
        if self.last_error is None:
            if initial_status == status:
                return self
            while self.status != status:
                time.sleep(5)
                self.load()
                if self.last_error is not None:
                    raise ServerException(self.last_error)
                else:
                    continue
            if callback is not None:
                callback(self)
            else:
                return self
                
    @classmethod
    def all(cls):
        """Get a list of all known servers

        >>> Server.all()
        [{'server_id':1,...},{'server_id':2,...}]

        :returns: list -- a list of :class:`Server`
        :raises: ServerException
        """
        r = Resource(cls.path)
        r.request_details = 'basic'
        s = r.get()
        if r.last_error is None:
            servers = [cls(server['serverId']) for server in s[cls.collection_name]]
            return servers
        else:
            raise ServerException(r.last_error)

class ServerException(BaseException): pass
class ServerLaunchException(ServerException): pass
