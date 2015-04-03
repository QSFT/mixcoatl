import sys
# These have to be set before importing any mixcoatl modules
import os
os.environ['ES_ACCESS_KEY'] = 'abcdefg'
os.environ['ES_SECRET_KEY'] = 'gfedcba'
import json

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

from httpretty import HTTPretty
from httpretty import httprettified

import mixcoatl.infrastructure.server as rsrc
from mixcoatl.settings.load_settings import config
from mixcoatl.utils import camelize

class TestServer(unittest.TestCase):
    def setUp(self):
        self.cls = rsrc.Server
        self.es_url = '%s/%s' % (config.endpoint, self.cls.PATH)
        self.json_file = '../../tests/data/unit/infrastructure/server.json'

    @httprettified
    def test_has_all_and_is_one(self):
        '''test all() returns a list of Server'''

        with open(self.json_file) as f:
            data = f.read()
        HTTPretty.register_uri(HTTPretty.GET,
            self.es_url,
            body = data,
            status = 200,
            content_type = "application/json")
        s = self.cls.all()

    @httprettified
    def test_has_one(self):
        '''test Server(<id>) returns a valid resource'''
        pk = 331810
        with open(self.json_file) as f:
            data = json.load(f)
        data[self.cls.COLLECTION_NAME][:] = [d for d in data[self.cls.COLLECTION_NAME] if
                                             d[camelize(self.cls.PRIMARY_KEY)] == pk]
        HTTPretty.register_uri(HTTPretty.GET,
            self.es_url+'/'+str(pk),
            body = json.dumps(data),
            status = 200,
            content_type = "application/json")

        s = self.cls(pk)
        s.load()
        assert s.server_id == pk
        assert s.status == 'RUNNING'
        assert s.agent_version == 17
        assert s.region['region_id'] == 19344
        assert s.data_center['data_center_id'] == 64351
        assert s.customer['customer_id'] == 12345
        assert s.cloud['cloud_id'] == 1
        assert '10.1.1.1' in s.private_ip_addresses
        assert s.public_ip_address == '1.1.1.1'
        assert s.platform == 'UBUNTU'
        assert s.owning_groups[0]['group_id'] == 9465
        assert s.provider_id == 'i-0c67a03e'
        assert s.start_date == '2012-12-18T18:31:26.000+0000'
        assert s.budget == 10287
        assert s.owning_user['user_id'] == 54321
        assert s.provider_product_id == 'm1.small'
        assert s.provider_id == 'i-0c67a03e'
        assert s.firewalls[0]['firewall_id'] == 117164
        assert s.machine_image['machine_image_id'] == 281535
        assert s.description == 'Sample-Tier-independent-node-0'
        assert s.product['product_id'] == 652
        assert s.vlan['vlan_id'] == 2600

    @httprettified
    def test_launch_basic(self):
        jobdata = '{"jobs":[{"jobId":84322,"status":"RUNNING"}]}'
        HTTPretty.register_uri(HTTPretty.POST,
            self.es_url,
            body = jobdata,
            content_type="application/json",
            status=202)
        s = self.cls()
        s.provider_product_id = 'm1.xlarge'
        s.machine_image = 284831
        s.vlan = 2600
        s.description = 'unit test server'
        s.name = 'my-test-server'
        s.data_center = 64716
        s.budget = 10287
        s.launch()
        assert s.last_error is None
        assert s.current_job == 84322

    @httprettified
    def test_launch_advanced(self):
        jobdata = '{"jobs":[{"jobId":84322,"status":"RUNNING"}]}'
        HTTPretty.register_uri(HTTPretty.POST,
            self.es_url,
            body = jobdata,
            content_type="application/json",
            status=202)
        s = self.cls()
        s.provider_product_id = 'm1.xlarge'
        s.machine_image = 284831
        s.vlan = 2600
        s.description = 'unit test server'
        s.name = 'my-test-server'
        s.data_center = 64716
        s.budget = 10287
        s.keypair = 'test-kp-uswest2'
        s.launch()
        assert s.keypair == 'test-kp-uswest2'
        assert s.last_error is None
        assert s.current_job == 84322

    @httprettified
    def test_dont_launch_running_server(self):
        pk = 331810
        with open(self.json_file) as f:
            data = json.load(f)
        data[self.cls.COLLECTION_NAME][:] = [d for d in data[self.cls.COLLECTION_NAME] if
                                             d[camelize(self.cls.PRIMARY_KEY)] == pk]
        HTTPretty.register_uri(HTTPretty.GET,
            self.es_url+'/'+str(pk),
            body = json.dumps(data),
            status = 200,
            content_type = "application/json")

        s = self.cls(pk)
        with self.assertRaises(rsrc.ServerLaunchException):
            s.launch()

    # @httprettified
    # def test_destroy_server(self):
    #     HTTPretty.register_uri(HTTPretty.DELETE,
    #         self.es_url,
    #         content_type="application/json",
    #     status = 204)
    #     s = self.cls(33181)
    #     r = s.destroy()
