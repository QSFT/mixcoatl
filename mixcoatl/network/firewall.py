"""Implements the enStratus Firewall API"""
from mixcoatl.resource import Resource
from mixcoatl.decorators.lazy import lazy_property
from mixcoatl.network.firewall_rule import FirewallRule
from mixcoatl.utils import camelize, camel_keys

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

    @lazy_property
    def owning_account(self):
        """`dict` - The enStratus account under which this firewall is registered"""
        return self.__owning_account

    @lazy_property
    def name(self):
        """`str` - The user-friendly name for this firewall"""
        return self.__name

    @lazy_property
    def owning_user(self):
        """`dict` or `None` - The enStratus owner of record for this firewall"""
        return self.__owning_user

    @lazy_property
    def description(self):
        """`str` - The description of this firewall in enStratus"""
        return self.__description

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

    @lazy_property
    def removable(self):
        """`bool` - Indicates if this firewall can be removed"""
        return self.__removable

    @lazy_property
    def budget(self):
        """`int` - The enStratus billing code costs are associated with"""
        return self.__budget

    @lazy_property
    def customer(self):
        """`dict` - The enStratus customer to which this firewall belongs"""
        return self.__customer

    @property
    def rules(self):
        """`list` - The firewall rules associated with this firewall"""
        try:
            return self.__rules
        except AttributeError:
            rls = FirewallRule.all(self.__firewall_id)
            if len(rls) < 1:
                self.__rules = []
            else:
                self.__rules = rls
            return rls

    @classmethod
    def all(cls, region_id, **kwargs):
        """List all firewalls in `region_id`

        :param region_id: The region to list firewalls for
        :type region_id: int.
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

        params['regionId'] = region_id
        x = r.get(params=params)
        if r.last_error is None:
            keys = [cls(i[camelize(cls.PRIMARY_KEY)]) for i in x[cls.COLLECTION_NAME]]
            if keys_only is True:
                firewalls = keys
            else:
                firewalls = []
                for i in x[cls.COLLECTION_NAME]:
                    key = i[camelize(cls.PRIMARY_KEY)]
                    fw = cls(key)
                    fw.request_details = request_details
                    fw.load()
                    firewalls.append(fw)
            return firewalls
        else:
            raise FirewallException(r.last_error)

class FirewallException(BaseException):
    """Generic Firewall Exception"""
    pass
