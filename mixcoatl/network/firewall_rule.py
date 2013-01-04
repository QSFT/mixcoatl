from mixcoatl.resource import Resource
from mixcoatl.decorators.lazy import lazy_property

class FirewallRule(Resource):
    path = 'network/FirewallRule'
    collection_name = 'rules'
    primary_key = 'firewall_rule_id'

    def __init__(self, firewall_rule_id = None, *args, **kwargs):
        Resource.__init__(self)
        self.__firewall_rule_id = firewall_rule_id

    @property
    def firewall_rule_id(self):
        return self.__firewall_rule_id
    
    @lazy_property
    def direction(self):
        return self.__direction

    @lazy_property
    def firewall(self):
        return self.__firewall

    @lazy_property
    def network_address(self):
        return self.__network_address

    @lazy_property
    def protocol(self):
        return self.__protocol

    @classmethod
    def all(cls, firewall_id):
        from mixcoatl.utils import uncamel_keys
        r = Resource(cls.path)
        r.request_details = 'extended'
        params = {'firewallId':firewall_id}
        c = r.get(params=params)
        if r.last_error is None:
            rules = [i['firewallRuleId'] for i in c[cls.collection_name]]
            return [cls(rule) for rule in rules]
        else:
            return r.last_error