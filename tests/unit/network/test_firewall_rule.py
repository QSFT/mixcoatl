import os
# These have to be set before importing any mixcoatl modules
os.environ['ES_ACCESS_KEY'] = 'abcdefg'
os.environ['ES_SECRET_KEY'] = 'gfedcba'

import unittest
from mock import patch
from mock import Mock
import mixcoatl.network.firewall_rule as fwrule
import tests.data.firewall as fw_data

@patch('mixcoatl.resource.Resource.get')
class TestFirewallRule(unittest.TestCase):
    def test_has_all_rules_and_is_FirewallRule(self, mock_data):
        '''test all() returns a list of FirewallRule'''
        mock_data.return_value = fw_data.firewall_rules
        f = fwrule.FirewallRule.all(116387)

    def test_has_a_rule(self, mock_data):
        mock_data.return_value = fw_data.one_firewall_rule
        f = fwrule.FirewallRule(3706471)
        assert f.direction == 'INGRESS'
        assert f.firewall['firewall_id'] == 116387
        assert f.firewall_rule_id == 3706471
        assert f.source == '217.240.165.28/32'
        assert f.source_type == 'CIDR'
        assert f.destination == '406'
        assert f.destination_type == 'GLOBAL'
        assert f.start_port == 2003
        assert f.end_port == 2003
        assert f.precedence == 0
        assert f.protocol == 'TCP'