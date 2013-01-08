import os
import sys
# These have to be set before importing any mixcoatl modules
os.environ['ES_ACCESS_KEY'] = 'abcdefg'
os.environ['ES_SECRET_KEY'] = 'gfedcba'
import json

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest
from httpretty import HTTPretty
from httpretty import httprettified

import mixcoatl.automation.configuration_management_account as rsrc
from mixcoatl.settings.load_settings import settings
from mixcoatl.utils import camelize

class TestConfigurationManagementAccount(unittest.TestCase):
    def setUp(self):
        self.cls = rsrc.ConfigurationManagementAccount
        self.es_url = '%s/%s' % (settings.endpoint, self.cls.path)
        self.json_file = '../../tests/data/unit/automation/configuration_management_account.json'

    @httprettified
    def test_has_all_and_is_one(self):
        '''test all() returns a list of ConfigurationManagementAccount'''

        with open(self.json_file) as f:
            data = f.read()
        HTTPretty.register_uri(HTTPretty.GET,
            self.es_url,
            body=data,
            status=200,
            content_type="application/json")

        s = self.cls.all()
        assert len(s) == 2
        for x in s:
            assert isinstance(x, self.cls)

    @httprettified
    def test_has_one(self):
        '''test ConfigurationManagementAccount(<id>) returns a valid resource'''
        pk = 3610
        with open(self.json_file) as f:
            data = json.load(f)
        data[self.cls.collection_name][:] = [d for d in data[self.cls.collection_name] if
                                             d[camelize(self.cls.primary_key)] == pk]
        HTTPretty.register_uri(HTTPretty.GET,
            self.es_url + '/' + str(pk),
            body=json.dumps(data),
            status=200,
            content_type="application/json")
        s = self.cls(pk)
        assert s.cm_account_id == pk
        assert s.account_number == ''
        assert s.budget is -1
        assert s.cm_service['cm_service_id'] == 3710
        assert s.created_timestamp == '2013-01-06T06:50:29.326+0000'
        assert s.customer['customer_id'] == 12345
        assert s.description == 'a chef cm account'
        assert s.guid == '/customer/12345/cmAccount/3610'
        assert s.label == 'iconlightbulb'
        assert s.removable is True
        assert s.status == 'ACTIVE'
        assert s.last_modified_timestamp == '2013-01-06T06:50:29.326+0000'