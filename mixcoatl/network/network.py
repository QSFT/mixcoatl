"""Implements the DCM Network API"""
from mixcoatl.resource import Resource
from mixcoatl.decorators.lazy import lazy_property
from mixcoatl.decorators.validations import required_attrs
from mixcoatl.utils import camelize, camel_keys, uncamel_keys
from mixcoatl.admin.job import Job
import json


class Network(Resource):

    """ Dell Cloud Manager models two distinct kinds of networks as network resources:

    * Standard networks such as an AWS VPC or Cloud.com network that represent a 
      network as known to a cloud provider
    * Overlay networks such as a VPNCubed, CloudSwitch, or vCider network in which 
      the network is an overlay on top of the cloud providers network 
    """
    PATH = 'network/Network'
    COLLECTION_NAME = 'networks'
    PRIMARY_KEY = "network_id"

    def __init__(self, network_id=None, *args, **kwargs):
        Resource.__init__(self)

        if 'detail' in kwargs:
            self.request_details = kwargs['detail']

        self.__network_id = network_id

    @property
    def network_id(self):
        """`str` - The unique ID for this network"""
        return self.__network_id

    @lazy_property
    def status(self):
        """`str` - The status of this network"""
        return self.__status

    @lazy_property
    def label(self):
        """`str` - A color label assigned to this network"""
        return self.__label

    @lazy_property
    def data_center(self):
        return self.__data_center

    @label.setter
    def label(self, l):
        self.__label = l

    @lazy_property
    def name(self):
        """`str` - The user-friendly name for this network"""
        return self.__name

    @name.setter
    def name(self, n):
        self.__name = n

    @lazy_property
    def description(self):
        """`str` - The description of this network"""
        return self.__description

    @description.setter
    def description(self, d):
        self.__description = d

    @lazy_property
    def account(self):
        """`dict` - The account associated with the network"""
        return self.__account

    @lazy_property
    def owning_groups(self):
        """`list` - The DCM groups that have ownership of this network"""
        return self.__owning_groups

    @owning_groups.setter
    def owning_groups(self, g):
        self.__owning_groups = [{'group_id': g}]

    @lazy_property
    def cloud(self):
        """`dict` - The DCM cloud account in which this network lives"""
        return self.__cloud

    @lazy_property
    def data_center(self):
        """`dict` - The data center (if any) to which this network is tied"""
        return slef.__data_center

    @lazy_property
    def provider_id(self):
        """`str` - The cloud provider unique id for this network"""
        return self.__provider_id

    @lazy_property
    def region(self):
        """`dict` - The region in which this network operates"""
        return self.__region

    @region.setter
    def region(self, r):
        self.__region = {'region_id': r}

    @lazy_property
    def removable(self):
        """`bool` - Indicates if this network can be removed"""
        return self.__removable

    @lazy_property
    def budget(self):
        """`int` - The DCM billing code costs are associated with"""
        return self.__budget

    @budget.setter
    def budget(self, b):
        self.__budget = b

    @lazy_property
    def customer(self):
        """`dict` - The DCM customer to which this network belongs"""
        return self.__customer

    @lazy_property
    def guid(self):
        """`str` - The permanent unique URI identifier for this network in DCM."""
        return self.__guid

    @lazy_property
    def agent_communication(self):
        """`bool` - Indicates whether communication between DCM and the agents on the guest operating systems 
        in the cloud occur over a public or private channel."""
        return self.__agent_communication

    @lazy_property
    def allow_subnet_creation(self):
        """`bool` - Indicates whether or not you can POST to the Subnet resource to dynamically create subnets 
        against this network."""
        return self.__allow_subnet_creation

    @lazy_property
    def can_have_subnets(self):
        """`bool` - Indicates whether the technology behind this network supports subdivision into subnets."""
        return self.__can_have_subnets

    @lazy_property
    def publicly_addressable(self):
        """`bool` - Indicates whether the resources in this network can be accessed from the public Internet."""
        return self.__publicly_addressable

    @lazy_property
    def flat(self):
        """`bool` - Indicates whether this network is a flat network or is part of a more fine-grained 
        network hierarchy."""
        return self.__flat

    @lazy_property
    def created_timestamp(self):
        """`str` - Creation time."""
        return self.__created_timestamp

    @lazy_property
    def last_modified_timestamp(self):
        """`str` - The time when a modification was last made to this network."""
        return self.__last_modified_timestamp

    @lazy_property
    def network_address(self):
        """`str` - An IPv4 CIDR representing the block of IP addresses hosted in this network."""
        return self.__network_address

    @network_address.setter
    def network_address(self, n):
        self.__network_address = n

    @lazy_property
    def network_type(self):
        """`str` - Identifies what kind of network is represented by this resource."""
        return self.__network_type

    @lazy_property
    def ntp_servers(self):
        """`list` - A list of NTP servers configured for this network."""
        return self.__ntp_servers

    @ntp_servers.setter
    def ntp_servers(self, n):
        self.__ntp_servers = [n]

    @lazy_property
    def subnets(self):
        """`list` - The list of subnets associated with this network."""
        return self.__subnets

    @lazy_property
    def dns_servers(self):
        """`list` - A list of DNS servers configured for this network."""
        return self.__dns_servers

    @dns_servers.setter
    def dns_servers(self, d):
        self.__dns_servers = [d]

    @lazy_property
    def owning_user(self):
        """`str` - The network's owning user. """
        return self.__owning_user

    @required_attrs(['budget', 'name', 'network_address', 'region', 'description'])
    def create(self, **kwargs):
        """Create a new network

        :param callback: Optional callback to call with resulting :class:`Network`
        :type callback: func.
        :returns: :class:`Job`
        :raises: :class:`NetworkException`
        """

        optional_attrs = [
            'owning_groups', 'ntp_servers', 'dns_servers', 'label']
        payload = {'add_network': [{
                   'budget': self.budget,
                   'name': self.name,
                   'network_address': self.network_address,
                   'description': self.description,
                   'region': self.region}]}

        if 'label' in kwargs:
            payload['add_network'][0]['label'] = kwargs['label']

        callback = kwargs.get('callback', None)

        for oa in optional_attrs:
            try:
                if getattr(self, oa) is not None:
                    payload['add_network'][0].update({oa: getattr(self, oa)})
            except AttributeError:
                pass

        self.post(self.PATH, data=json.dumps(camel_keys(payload)))

        if self.last_error is None:
            j = Job(self.current_job)
            j.load()
            if callback is not None:
                callback(j)
            else:
                return j
        else:
            raise NetworkException(self.last_error)

    @required_attrs(['network_id'])
    def destroy(self, reason='no reason provided'):
        """Destroy network with reason :attr:`reason`

        :param reason: The reason for terminating the server
        :type reason: str.
        :returns: bool -- Result of API call
        """
        p = self.PATH + "/" + str(self.network_id)
        qopts = {'reason': reason}
        return self.delete(p, params=qopts)

    @classmethod
    def all(cls, **kwargs):
        """List all networks in `region_id`

        :param region_id: Limit results to `region_id`
        :type region_id: int.
        :param data_center_id: Limit results to `data_center_id`
        :type region_id: int.
        :param account_id: limit results to `account_id`
        :type account_id: int.
        :param detail: Level of detail to return - `basic` or `extended`
        :type detail: str.
        :param keys_only: Return only :attr:`network_id` in results
        :type keys_only: bool.
        :param active_only: Limits the list of networks to only active networks if true. Default is True.
        :type keys_only: bool.
        :returns: `list` of :attr:`network_id` or :class:`Network`
        :raises: :class:`NetworkException`
        """
        params = {}
        r = Resource(cls.PATH)

        if 'detail' in kwargs:
            request_details = kwargs['detail']
        else:
            request_details = 'extended'

        if 'keys_only' in kwargs:
            keys_only = kwargs['keys_only']
        else:
            keys_only = False

        if 'region_id' in kwargs:
            params['regionId'] = kwargs['region_id']

        if 'data_center_id' in kwargs:
            params['dataCenterId'] = kwargs['data_center_id']

        if 'account_id' in kwargs:
            params['accountId'] = kwargs['account_id']

        if 'active_only' in kwargs:
            params['activeOnly'] = kwargs['active_only']
        else:
            params['activeOnly'] = True

        x = r.get(params=params)
        if r.last_error is None:
            if keys_only is True:
                return [i[camelize(cls.PRIMARY_KEY)] for i in x[cls.COLLECTION_NAME]]
            else:
                return [type(cls.__name__, (object,), i) for i in uncamel_keys(x)[cls.COLLECTION_NAME]]
        else:
            raise NetworkException(r.last_error)


class NetworkException(BaseException):

    """Generic Network Exception"""
    pass
