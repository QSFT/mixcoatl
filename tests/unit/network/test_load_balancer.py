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

import mixcoatl.network.load_balancer as rsrc
from mixcoatl.settings.load_settings import settings
from mixcoatl.utils import camelize

class TestLoadBalancer(unittest.TestCase):
    def setUp(self):
        self.cls = rsrc.LoadBalancer
        self.es_url = '%s/%s' % (settings.endpoint, self.cls.path)
        self.json_file = '../../tests/data/unit/network/load_balancer.json'

    @httprettified
    def test_has_all_and_is_one(self):
        '''test all() returns a list of LoadBalancer'''

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
        '''test LoadBalancer(<id>) returns a valid resource'''
        pk = 12516
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
        s.load()
        assert s.load_balancer_id == pk
        assert s.address == 'wordpress-lb.us-west-2.elb.amazonaws.com'
        assert s.budget == 10287
        assert s.cloud['cloud_id'] == 1
        assert s.cname_based is True
        assert s.customer['customer_id'] == 12345
        assert s.description == 'Cloud Load Balancer for wordpress demo deployment'
        assert s.owning_account['account_id'] == 16000
        assert s.owning_groups[0]['group_id'] == 9465
        assert s.owning_user['user_id'] == 54321
        assert s.provider_id == 'wordpress-deployment'
        assert s.region['region_id'] == 19344
        assert s.status == 'ACTIVE'
