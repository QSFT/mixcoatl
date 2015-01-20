import os
# These have to be set before importing any mixcoatl modules
os.environ['ES_ACCESS_KEY'] = 'abcdefg'
os.environ['ES_SECRET_KEY'] = 'gfedcba'

import unittest
from mock import patch
from mock import Mock
import mixcoatl.network.firewall as firewall
import mixcoatl.network.firewall_rule as fwrule
import tests.data.firewall as fw_data

@patch('mixcoatl.resource.Resource.get')
class TestFirewall(unittest.TestCase):

    def setUp(self):
        self.last_error = 'job terminated unexpectedly'

    # def test_has_all_fwalls_and_is_Firewall(self, mock_data):
    #     '''test all() returns a list of Firewall'''
    #     mock_data.return_value = fw_data.all_firewalls

    #     f = firewall.Firewall.all(region_id=19344)
    #     assert len(f) == 8
    #     for x in f:
    #         assert isinstance(x, firewall.Firewall), '%s must be an instance of Firewall' % x

    # def test_has_a_firewall(self, mock_data):
    #     mock_data.return_value = fw_data.one_firewall

    #     f = firewall.Firewall(116387)
    #     assert f.firewall_id == 116387
    #     assert f.status == 'ACTIVE'
    #     assert f.region['region_id'] == 19344

    # def test_has_rules(self, mock_data):
    #     mock_data.return_value = fw_data.firewall_rules

    #     f = firewall.Firewall(116387)
    #     assert len(f.rules) == 5
    #     for x in f.rules:
    #         assert isinstance(x, fwrule.FirewallRule), '%s must be an instance of Firewallrule' % x

    # def test_has_no_rules(self, mock_data):
    #     mock_data.return_value = fw_data.no_rules

    #     f = firewall.Firewall(123456)
    #     assert len(f.rules) == 0
