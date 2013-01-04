from mixcoatl.resource import Resource
from mixcoatl.decorators.lazy import lazy_property

class Firewall(Resource):
    path = 'network/Firewall'
    collection_name = 'firewalls'
    primary_key = "firewall_id"

    def __init__(self, firewall_id = None, *args, **kwargs):
        Resource.__init__(self)
        self.__firewall_id = firewall_id

    @property
    def firewall_id(self):
        return self.__firewall_id

    @lazy_property
    def status(self):
        return self.__status

    @lazy_property
    def label(self):
        return self.__label

    @lazy_property
    def owning_account(self):
        return self.__owning_account

    @lazy_property
    def name(self):
        return self.__name

    @lazy_property
    def owning_user(self):
        return self.__owning_user

    @lazy_property
    def description(self):
        return self.__description

    @lazy_property
    def cloud(self):
        return self.__cloud

    @lazy_property
    def provider_id(self):
        return self.__provider_id

    @lazy_property
    def region(self):
        return self.__region

    @lazy_property
    def removable(self):
        return self.__removable

    @lazy_property
    def budget(self):
        return self.__budget

    @lazy_property
    def customer(self):
        return self.__customer

    @property
    def rules(self):
        try:
            return self.__rules
        except AttributeError:
            from mixcoatl.network.firewall_rule import FirewallRule
            rls = FirewallRule.all(self.__firewall_id)
            if len(rls) < 1:
                self.__rules = []
            else:
                self.__rules = rls
            return rls

    @classmethod
    def all(cls, region_id):
        from mixcoatl.utils import uncamel_keys
        r = Resource(cls.path)
        r.request_details = 'extended'
        params = {'regionId':region_id}
        c = r.get(params=params)
        if r.last_error is None:
            return [cls(i['firewallId']) for i in c[cls.collection_name]]
            #return uncamel_keys(c)
        else:
            return r.last_error
