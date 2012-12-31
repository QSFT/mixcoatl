from mixcoatl.resource import Resource
from mixcoatl.decorators.lazy import lazy

@lazy(key='firewall_rule_id')
class FirewallRule(Resource):
    path = 'network/FirewallRule'
    collection_name = 'rules'

    def __init__(self, firewall_rule_id = None, *args, **kwargs):
        Resource.__init__(self)
        if firewall_rule_id is None:
            pass
        self.__firewall_rule_id = firewall_rule_id

    @property
    def direction(self):
        return self.__direction

    @property
    def firewall(self):
        return self.__firewall

    @property
    def firewall_rule_id(self):
        return self.__firewall_rule_id

    @property
    def network_address(self):
        return self.__network_address

    @property
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
            return [cls(i['firewallRuleId']) for i in c[cls.collection_name]]
        else:
            return r.last_error