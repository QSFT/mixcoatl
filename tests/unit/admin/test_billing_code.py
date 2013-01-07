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

import mixcoatl.admin.billing_code as billing_code
from mixcoatl.settings.load_settings import settings


class TestApiKey(unittest.TestCase):
    def setUp(self):
        self.es_url = settings.endpoint + '/' + billing_code.BillingCode.path

    @httprettified
    def test_has_all_and_is_one(self):
        '''test BillingCode.all() returns a list of BillingCode'''

        with open('../../tests/data/unit/admin/billing_code.json') as f:
            data = f.read()
        HTTPretty.register_uri(HTTPretty.GET,
            self.es_url,
            body=data,
            status=200,
            content_type="application/json")

        s = billing_code.BillingCode.all()
        assert len(s) == 2
        for x in s:
            assert isinstance(x, billing_code.BillingCode)

    @httprettified
    def test_has_one(self):
        '''test BillingCode(<id>) returns a valid resource'''
        with open('../../tests/data/unit/admin/billing_code.json') as f:
            data = json.load(f)
        data['billingCodes'][:] = [d for d in data['billingCodes'] if d['billingCodeId'] == 10670]
        HTTPretty.register_uri(HTTPretty.GET,
            self.es_url+'/10670',
            body=json.dumps(data),
            status=200,
            content_type="application/json")
        s = billing_code.BillingCode(10670)
        assert s.billing_code_id == 10670
        assert s.budget_state == 'NORMAL'
        assert s.current_usage['currency'] == 'USD'
        assert s.customer['customer_id'] == 12345
        assert s.description == 'a test budget code'
        assert s.finance_code == 'TEST'
        assert s.name == 'Test'
        assert s.projected_usage['currency'] == 'USD'
        assert s.status == 'ACTIVE'