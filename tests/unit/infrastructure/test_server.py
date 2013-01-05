import os
# These have to be set before importing any mixcoatl modules
os.environ['ES_ACCESS_KEY'] = 'abcdefg'
os.environ['ES_SECRET_KEY'] = 'gfedcba'

import unittest
from mock import patch
from mock import Mock
import mixcoatl.infrastructure.server as server
import tests.data.server as srv_data
from httpretty import HTTPretty
from httpretty import httprettified

import json
#@patch('mixcoatl.resource.Resource.get')
class TestServer(unittest.TestCase):

    @httprettified
    def test_has_all_servers_and_id_Server(self):
        '''test all() returns a list of Server'''

        es_url = "https://api.enstratus.com/api/enstratus/2012-06-15/infrastructure/Server"
        data = srv_data.all_servers
        HTTPretty.register_uri(HTTPretty.GET,
            es_url,
            body = json.dumps(data),
            status = 200,
            content_type = "application/json")
        s = server.Server.all()
        assert len(s) == 3
        for x in s:
            assert isinstance(x, server.Server), '%s must be an instance of Server' % x

    @httprettified
    def test_has_a_firewall(self):
        es_url = "https://api.enstratus.com/api/enstratus/2012-06-15/infrastructure/Server/331810"
        data = srv_data.one_server
        HTTPretty.register_uri(HTTPretty.GET,
            es_url,
            body = json.dumps(data),
            status = 200,
            content_type = "application/json")

        s = server.Server(331810)
        print s
        assert s.server_id == 331810
        assert s.status == 'RUNNING'
        assert s.agent_version == 17
        assert s.region['region_id'] == 19344
        assert s.data_center['data_center_id'] == 64351

    @httprettified
    def test_launch_basic(self):
        es_url = "https://api.enstratus.com/api/enstratus/2012-06-15/infrastructure/Server"
        jobdata = '{"jobs":[{"jobId":84322,"status":"RUNNING"}]}'
        HTTPretty.register_uri(HTTPretty.POST,
            es_url,
            body = jobdata,
            content_type="application/json",
            status=202)
        s = server.Server()
        s.provider_product_id = 'm1.xlarge'
        s.machine_image = 284831
        s.description = 'unit test server'
        s.name = 'my-test-server'
        s.data_center = 64716
        s.launch()
        assert s.last_error is None
        assert s.current_job == 84322
