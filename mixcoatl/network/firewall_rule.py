from mixcoatl.resource import Resource
from mixcoatl.decorators.lazy import lazy_property
from mixcoatl.decorators.validations import required_attrs
from mixcoatl.admin.job import Job
from mixcoatl.utils import camel_keys
from mixcoatl.utils import camelize

import json

class FirewallRule(Resource):
    PATH = 'network/FirewallRule'
    COLLECTION_NAME = 'rules'
    PRIMARY_KEY = 'firewall_rule_id'

    def __init__(self, firewall_rule_id = None, *args, **kwargs):
        if 'detail' in kwargs:
            self.request_details = kwargs['detail']

        Resource.__init__(self)
        self.__firewall_rule_id = firewall_rule_id

    @property
    def firewall_rule_id(self):
        """`int` - The unique enStratus id for this rule"""
        return self.__firewall_rule_id

    @lazy_property
    def direction(self):
        """`str` - The direction of the rule: `ingress` or `egress`"""
        return self.__direction

    @direction.setter
    def direction(self, d):
        self.__direction = d

    @lazy_property
    def firewall(self):
        """`dict` - The firewall to which this rule belongs"""
        return self.__firewall

    @firewall.setter
    def firewall(self, fwid):
        self.__firewall = {'firewall_id': fwid}

    @lazy_property
    def network_address(self):
        """`str` - The CIDR for the source or destination of traffic"""
        return self.__network_address

    @network_address.setter
    def network_address(self, addr):
        self.__network_address = addr

    @lazy_property
    def protocol(self):
        """`str` - The network protocol for this rule"""
        return self.__protocol

    @protocol.setter
    def protocol(self, p):
        self.__protocol = p

    @lazy_property
    def start_port(self):
        """`int` or `None` - The start port for this rule"""
        return self.__start_port

    @start_port.setter
    def start_port(self, p):
        self.__start_port = p

    @lazy_property
    def end_port(self):
        """`int` or `None` - The end port for this rule"""
        return self.__end_port

    @end_port.setter
    def end_port(self, p):
        self.__end_port = p

    @required_attrs(['firewall', 'network_address', 'protocol', 'direction', 'start_port', 'end_port'])
    def create(self, **kwargs):
        """Create a new firewall rule

            .. warning::

                Does not currently support adding ICMP rules

        :param reason: Reason for the new rule
        :type reason: str.
        :returns: `bool`
        :raises: :class:`FirewallRuleException`
        """

        if 'reason' not in kwargs:
            reason = 'Added by mixcoatl'
        else:
            reason = kwargs['reason']

        payload = {'add_rule':[{
            'firewall_id': self.firewall['firewall_id'],
            'direction': self.direction,
            'start_port': self.start_port,
            'end_port': self.end_port,
            'protocol': self.protocol,
            'reason': reason,
            'cidr' : self.network_address}]}

        if self.firewall_rule_id is not None:
            raise FirewallRuleException('Cannot modify existing firewall rule')

        self.post(self.PATH, data=json.dumps(camel_keys(payload)))

        if self.last_error is None:
            return True
        else:
            if self.last_request.status_code == 418:
                return True
            else:
                raise FirewallRuleException(self.last_error)

    @required_attrs(['firewall_rule_id'])
    def remove(self, reason):
        """Remove a firewall rule

        :param reason: Reason for removing the rule
        :type reason: str.
        :returns: `bool`
        :raises: :class:`FirewallRuleException`
        """

        params = {'reason': reason}
        self.delete(self.PATH+'/'+str(self.firewall_rule_id), params=params)

        if self.last_error is None:
            return True
        else:
            raise FirewallRuleException(self.last_error)

    @classmethod
    def all(cls, firewall_id, **kwargs):
        """List all rules for `firewall_id`

        :param firewall_id: The id of the firewall to list rules for
        :type firewall_id: int.
        :param detail: Level of detail to return - `basic` or `extended`
        :type detail: str.
        :param keys_only: Return only :attr:`firewall_rule_id` in results
        :type keys_only: bool.
        :returns: `list` of :attr:`firewall_rule_id` or :class:`FirewallRule`
        :raises: :class:`FirewallRuleException`
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

        params['firewallId'] = firewall_id
        x = r.get(params=params)
        if r.last_error is None:
            keys = [i[camelize(cls.PRIMARY_KEY)] for i in x[cls.COLLECTION_NAME]]
            if keys_only is True:
                rules = keys
            else:
                rules = []
                for i in x[cls.COLLECTION_NAME]:
                    key = i[camelize(cls.PRIMARY_KEY)]
                    rule = cls(key)
                    rule.request_details = request_details
                    rule.load()
                    rules.append(rule)
            return rules
        else:
            raise FirewallRuleException(r.last_error)

def add_rule(firewall_id, network, proto, direction, start, end, reason):
    """Add a firewall rule to a firewall

    >>> f = add_rule(136663, '10.1.1.1/32', 'TCP', 'INGRESS', 15000, 15000, 'inbound api')

    """
    f = FirewallRule()
    f.firewall = firewall_id
    f.network_address = network
    f.protocol = proto
    f.direction = direction
    f.start_port = start
    f.end_port = end
    return f.create(reason=reason)

def delete_rule(rule_id, reason='rule removed by mixcoatl'):
    """Remove a firewall rule

    :param rule_id: The id of the firewall rule to remove
    :type rule_id: int.
    :param reason: The reason for removing the rule
    :type reason: string
    :returns: `bool`
    :raises: :class:`FirewallRuleException`
    """
    f = FirewallRule(rule_id)
    return f.remove(reason)

class FirewallRuleException(BaseException):
    """Generic Exception for FirewallRules"""
    pass
