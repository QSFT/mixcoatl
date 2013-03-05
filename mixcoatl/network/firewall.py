"""Implements the enStratus Firewall API"""
from mixcoatl.resource import Resource
from mixcoatl.decorators.lazy import lazy_property
from mixcoatl.decorators.validations import required_attrs
from mixcoatl.network.firewall_rule import FirewallRule
from mixcoatl.utils import camelize, camel_keys
from mixcoatl.admin.job import Job

import json

class Firewall(Resource):
    PATH = 'network/Firewall'
    COLLECTION_NAME = 'firewalls'
    PRIMARY_KEY = "firewall_id"

    def __init__(self, firewall_id = None, *args, **kwargs):
        Resource.__init__(self)

        if 'detail' in kwargs:
            self.request_details = kwargs['detail']

        self.__firewall_id = firewall_id

    @property
    def firewall_id(self):
        """`str` - The unique enStratus ID for this firewall"""
        return self.__firewall_id

    @lazy_property
    def status(self):
        """`str` - The status of this firewall"""
        return self.__status

    @lazy_property
    def label(self):
        """`str` - A color label assigned to this firewall"""
        return self.__label

    @label.setter
    def label(self, l):
        self.__label = l

    @lazy_property
    def owning_account(self):
        """`dict` - The enStratus account under which this firewall is registered"""
        return self.__owning_account

    @lazy_property
    def name(self):
        """`str` - The user-friendly name for this firewall"""
        return self.__name

    @name.setter
    def name(self, n):
        self.__name = n

    @lazy_property
    def owning_user(self):
        """`dict` or `None` - The enStratus owner of record for this firewall"""
        return self.__owning_user

    @lazy_property
    def owning_groups(self):
        """`list` - The enStratus groups that have ownership of this firewall"""
        return self.__owning_groups

    @lazy_property
    def description(self):
        """`str` - The description of this firewall in enStratus"""
        return self.__description

    @description.setter
    def description(self, d):
        self.__description = d

    @lazy_property
    def cloud(self):
        """`dict` - The enStratus cloud account in which this firewall lives"""
        return self.__cloud

    @lazy_property
    def provider_id(self):
        """`str` - The cloud provider unique id for this firewall"""
        return self.__provider_id

    @lazy_property
    def region(self):
        """`dict` - The region in which this firewall operates"""
        return self.__region

    @region.setter
    def region(self, r):
        self.__region = {'region_id': r}

    @lazy_property
    def removable(self):
        """`bool` - Indicates if this firewall can be removed"""
        return self.__removable

    @lazy_property
    def budget(self):
        """`int` - The enStratus billing code costs are associated with"""
        return self.__budget

    @budget.setter
    def budget(self, b):
        self.__budget = b

    @lazy_property
    def customer(self):
        """`dict` - The enStratus customer to which this firewall belongs"""
        return self.__customer

    @property
    def rules(self):
        """`list` - The firewall rules associated with this firewall"""
        if self.__firewall_id is None:
            self.__rules = []
            return []
        try:
            return self.__rules
        except AttributeError:
            rls = FirewallRule.all(self.__firewall_id, detail=self.request_details)
            if len(rls) < 1:
                self.__rules = []
            else:
                self.__rules = rls
            return rls

    @required_attrs(['budget', 'region', 'name', 'description'])
    def create(self, **kwargs):
        """Create a new firewall

        :param label: Optional label to assign the firewall
        :type label: str.
        :param callback: Optional callback to call with resulting :class:`Firewall`
        :type callback: func.
        :returns: :class:`Firewall`
        :raises: :class:`FirewallException`
        """

        payload = {'add_firewall':[{
            'budget': self.budget,
            'region': self.region,
            'name': self.name,
            'description': self.description
            }]}

        if 'label' in kwargs:
            payload['add_firewall'][0]['label'] = kwargs['label']

        callback = kwargs.get('callback', None)

        self.post(self.PATH, data=json.dumps(camel_keys(payload)))

        if self.last_error is None:
            if callback is None:
                return self
            else:
                if Job.wait_for(self.current_job) is True:
                    j = Job(self.current_job)
                    self.__firewall_id = j.message
                    self.load()
                    return self
                else:
                    raise FirewallException(j.last_error)
        else:
            raise FirewallException(self.last_error)

    def describe(self):
        """Describe a firewall"""


    @classmethod
    def all(cls, **kwargs):
        """List all firewalls in `region_id`

        :param region_id: Limit results to `region_id`
        :type region_id: int.
        :param account_id: limit results to `account_id`
        :type account_id: int.
        :param detail: Level of detail to return - `basic` or `extended`
        :type detail: str.
        :param keys_only: Return only :attr:`firewall_id` in results
        :type keys_only: bool.
        :returns: `list` of :attr:`firewall_id` or :class:`Firewall`
        :raises: :class:`FirewallException`
        """

        params = {}
        r = Resource(cls.PATH)
        r.request_details = 'none'

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

        if 'account_id' in kwargs:
            params['accountId'] = kwargs['account_id']

        x = r.get(params=params)
        if r.last_error is None:
            keys = [i[camelize(cls.PRIMARY_KEY)] for i in x[cls.COLLECTION_NAME]]
            if keys_only is True:
                firewalls = keys
            else:
                firewalls = []
                for key in keys:
                    fw = cls(key, detail=request_details)
                    fw.load()
                    firewalls.append(fw)
            return firewalls
        else:
            raise FirewallException(r.last_error)

def describe_firewall(firewall_id, **kwargs):
    """Changes the basic meta-data for a firewall

    :param firewall_id: The id of the firewall to modify
    :type firewall_id: int.
    :param description: The description of the firewall
    :type description: string.
    :param label: The label to assign the firewall.
    :type label: string.
    :param name: The name to give the firewall.
    :type name: string.
    :returns: `bool`
    :raises: :class:`FirewallException`
    """

    if kwargs:
        f = Firewall(firewall_id)
        f.label = kwargs.get('label', None)
        f.description = kwargs.get('name', None)
        f.label = kwargs.get('label', None)
        return f.describe()
    else:
        raise FirewallException("No attributes were specified to change")



class FirewallException(BaseException):
    """Generic Firewall Exception"""
    pass
