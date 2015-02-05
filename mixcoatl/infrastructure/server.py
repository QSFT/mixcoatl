from mixcoatl.resource import Resource
from mixcoatl.admin.job import Job
from mixcoatl.utils import camelize, camel_keys, uncamel_keys
from mixcoatl.decorators.validations import required_attrs
from mixcoatl.decorators.lazy import lazy_property
import json
import sys
import time


class Server(Resource):

    """A server is a virtual machine running within a data center."""
    PATH = 'infrastructure/Server'
    COLLECTION_NAME = 'servers'
    PRIMARY_KEY = 'server_id'

    def __init__(self, server_id=None):
        Resource.__init__(self)
        self.__server_id = server_id

    @property
    def server_id(self):
        """`int` - The DCM ID of this server"""
        return self.__server_id

    @lazy_property
    def agent_version(self):
        """`int` - The version of the DCM agent if installed."""
        return self.__agent_version

    @lazy_property
    def cloud(self):
        """`dict` - The cloud provided where the instance is located."""
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
        """`dict` - The customer account for the server."""
        return self.__customer

    @lazy_property
    def cm_account(self):
        """`dict` - The configuration management account for the server."""
        return self.__cm_account

    @lazy_property
    def data_center(self):
        """`dict` - The specific datacenter where the instance is located."""
        return self.__data_center

    @data_center.setter
    def data_center(self, d):
        self.__data_center = {u'data_center_id': d}

    @lazy_property
    def cmAccount(self):
        return self.__cmAccount

    @lazy_property
    def environment(self):
        return self.__environment

    @environment.setter
    def environment(self, c):
        self.__environment = {u'sharedEnvironmentCode': c}

    @cmAccount.setter
    def cm_account_id(self, c):
        self.__cmAccount = {u'cmAccountId': c}

    @lazy_property
    def cm_scripts(self):
        return self.__cm_scripts

    @lazy_property
    def last_agent_contact_timestamp(self):
        return self.__last_agent_contact_timestamp

    @cm_scripts.setter
    def cm_scripts(self, c):
        s = c.split(",")
        sc = []
        for cm in s:
            sc.append({u'sharedScriptCode': cm})
        self.__cm_scripts = sc

    @lazy_property
    def p_scripts(self):
        return self.__p_scripts

    @p_scripts.setter
    def p_scripts(self, c):
        s = c.split(",")
        p = []
        for cm in s:
            p.append({'sharedPersonalityCode': cm})

        self.__p_scripts = p

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
    def vlan(self):
        """`list` - The vlan to assign/assigned to the server"""
        return self.__vlan

    @vlan.setter
    def vlan(self, v):
        self.__vlan = {u'vlan_id': v}

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
        """`list` - The DCM groups owning the server."""
        return self.__owning_groups

    @lazy_property
    def owning_user(self):
        """`dict` - The DCM user owning the server."""
        return self.__owning_user

    @lazy_property
    def platform(self):
        """`str` - The platform of the server *(i.e. `UBUNTU`)*."""
        return self.__platform

    @lazy_property
    def personalities(self):
        """`dict` - The personalities associated with the server"""
        return self.__personalities

    @lazy_property
    def private_ip_addresses(self):
        """`list` - The private ip addresses assigned to the server."""

        return self.__private_ip_addresses

    @lazy_property
    def public_ip_address(self):
        """`str` - The public ip address of the server."""
        return self.__public_ip_address

    @lazy_property
    def public_ip_addresses(self):
        """`list` - The list of public ip addresses of the server."""
        return self.__public_ip_addresses

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
        """`str` - The provider's identifier for the server *(i.e. `i-abcdefg`)*"""
        return self.__provider_id

    @lazy_property
    def product(self):
        """`dict` - The DCM product record for the server"""
        return self.__product

    @lazy_property
    def start_date(self):
        """`str` - The date the server was started"""
        return self.__start_date

    @lazy_property
    def stop_date(self):
        """`str` - The date the server was stopped"""
        return self.__stop_date

    @lazy_property
    def status(self):
        """`str` - The status of the server *(i.e. `RUNNING` or `PAUSED`)*."""
        return self.__status

    @lazy_property
    def budget(self):
        """`int` - The budget code applied to the server."""
        return self.__budget

    @budget.setter
    def budget(self, b):
        """`int` - The budget code to apply to the server."""
        self.__budget = b

    @lazy_property
    def scripts(self):
        """`list` - The list of configuration management scripts of the server.(Chef?)"""
        return self.__scripts

    @lazy_property
    def run_list(self):
        """`list` - The list of configuration management scripts of the server.(Puppet?)"""
        return self.__run_list

    @lazy_property
    def architecture(self):
        """`str` - The architecture type of the server."""
        return self.__architecture

    @lazy_property
    def terminate_after(self):
        """`str` - The time the server automatically shuts down."""
        return self.__terminate_after

    @terminate_after.setter
    def terminate_after(self, t):
        self.__terminate_after = t

    @lazy_property
    def pause_after(self):
        """`str` - The time the server automatically pauses."""
        return self.__pause_after

    @lazy_property
    def userData(self):
        """`list` - The userdata to assign/assigned to the server"""
        return self.__userData

    @userData.setter
    def userData(self, userData):
        self.__userData = userData

    @lazy_property
    def volumeConfiguration(self):
        """`type` - The volumeConfiguration to assign/assigned to the server"""
        return self.__volumeConfiguration

    @volumeConfiguration.setter
    def volumeConfiguration(self, volumeConfiguration):
        self.__volumeConfiguration = volumeConfiguration

    @property
    def keypair(self):
        """`str` - The keypair to assign

            .. note::
                DCM does not track keypairs used to launch servers.
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
                job = Job(self.current_job)
                self.__server_id = job.message
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
        p = self.PATH + "/" + str(self.server_id)
        qopts = {'reason': reason}
        return self.delete(p, params=qopts)

    @required_attrs(['server_id'])
    def pause(self, reason=None):
        """Pause the server instance with reason :attr:`reason`

        :param reason: The reason for pausing the server
        :type reason: str.
        :returns: Job -- Result of API call
        """
        p = '%s/%s' % (self.PATH, str(self.server_id))
        payload = {'pause': [{}]}

        if reason is not None:
            payload['pause'][0].update({'reason': reason})

        return self.put(p, data=json.dumps(payload))

    @required_attrs(['server_id'])
    def extend_terminate(self, extend):
        p = '%s/%s' % (self.PATH, str(self.server_id))
        qopts = {'terminateAfter': extend}
        return self.delete(p, params=qopts)

    @required_attrs(['server_id'])
    def start(self, reason=None):
        """Start the paused server instance with reason :attr:`reason`

        :param reason: The reason for starting the server
        :type reason: str.
        :returns: Job -- Result of API call
        """
        p = '%s/%s' % (self.PATH, str(self.server_id))
        payload = {'start': [{}]}
        if reason is not None:
            payload['start'][0].update({'reason': reason})
        return self.put(p, data=json.dumps(payload))

    @required_attrs(['server_id'])
    def provision_user(self, user_id, admin_role=None):
        """Add a user to a server

        :param user_id: The ID of the user
        :type reason: int
        :returns: Job -- Result of API call
        """
        p = '%s/%s' % (self.PATH, str(self.server_id))
        user_dict = {'userId': user_id}
        if admin_role is not None:
            user_dict['adminRole'] = admin_role
        payload = {'provisionUser': [{'user': user_dict}]}
        return self.put(p, data=json.dumps(payload))

    @required_attrs(['server_id'])
    def deprovision_user(self, user_id):
        """Remove a user to a server

        :param user_id: The ID of the user
        :type reason: int
        :returns: Job -- Result of API call
        """
        p = '%s/%s' % (self.PATH, str(self.server_id))
        user_dict = {'userId': user_id}
        payload = {'deprovisionUser': [{'user': user_dict}]}
        return self.put(p, data=json.dumps(payload))

    @required_attrs(['server_id', 'name'])
    def rename(self):
        """Rename server"""
        p = '%s/%s' % (self.PATH, str(self.server_id))
        payload = {'describeServer': [{'name': self.name}]}
        return self.put(p, data=json.dumps(payload))

    @required_attrs(['server_id'])
    def stop(self, reason=None):
        """Stop the server instance with reason :attr:`reason`

        :param reason: The reason for stopping the server
        :type reason: str.
        :returns: Job -- Result of API call
        """
        p = '%s/%s' % (self.PATH, str(self.server_id))
        payload = {'stop': [{}]}

        if reason is not None:
            payload['stop'][0].update({'reason': reason})

        return self.put(p, data=json.dumps(payload))

    @required_attrs(['provider_product_id', 'machine_image', 'description',
                     'name', 'data_center', 'budget'])
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
        optional_attrs = ['userData', 'vlan', 'firewalls', 'keypair', 'label',
                          'cmAccount', 'environment', 'cm_scripts', 'p_scripts', 'volumeConfiguration']
        if self.server_id is not None:
            raise ServerLaunchException(
                'Cannot launch an already running server: %s' % self.server_id)

        payload = {'launch':
                   [{
                       'product': {"productId": self.provider_product_id},
                       'budget': self.budget,
                       'machineImage': camel_keys(self.machine_image),
                       'description': self.description,
                       'name': self.name,
                       'dataCenter': camel_keys(self.data_center)
                   }]}

        for oa in optional_attrs:
            try:
                if getattr(self, oa) is not None:
                    if oa == 'cm_scripts':
                        payload['launch'][0].update(
                            {'scripts': getattr(self, oa)})
                    elif oa == 'p_scripts':
                        payload['launch'][0].update(
                            {'personalities': getattr(self, oa)})
                    elif oa == 'volumeConfiguration':
                        payload['launch'][0].update(
                            {'volumeConfiguration': getattr(self, oa)})
                    elif oa == 'vlan':
                        payload['launch'][0].update(
                            {'vlan': camel_keys(getattr(self, oa))})
                    else:
                        payload['launch'][0].update({oa: getattr(self, oa)})
            except AttributeError:
                pass

        self.post(data=json.dumps(payload))
        if self.last_error is None:
            if callback is not None:
                callback(self.current_job)
            else:
                return self.current_job
        else:
            raise ServerLaunchException(self.last_error)

    def duplicate(self, server):
        pass

    def wait_for(self, status='RUNNING', callback=None):
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
    def all(cls, **kwargs):
        """Get a list of all known servers

        >>> Server.all()
        [{'server_id':1,...},{'server_id':2,...}]

        :returns: list -- a list of :class:`Server`
        :raises: ServerException
        """
        r = Resource(cls.PATH)
        params = {}

        if 'detail' in kwargs:
            r.request_details = kwargs['detail']
        else:
            r.request_details = 'basic'

        if 'keys_only' in kwargs:
            keys_only = kwargs['keys_only']
        else:
            keys_only = False

        if 'region_id' in kwargs:
            params['regionId'] = kwargs['region_id']

        x = r.get(params=params)
        if r.last_error is None:
            if keys_only is True:
                return [i[camelize(cls.PRIMARY_KEY)] for i in x[cls.COLLECTION_NAME]]
            else:
                return [type(cls.__name__, (object,), i) for i in uncamel_keys(x)[cls.COLLECTION_NAME]]
        else:
            raise ServerException(r.last_error)


class ServerException(BaseException):
    pass


class ServerLaunchException(ServerException):
    pass
