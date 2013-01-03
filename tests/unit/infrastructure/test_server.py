import os
# These have to be set before importing any mixcoatl modules
os.environ['ES_ACCESS_KEY'] = 'abcdefg'
os.environ['ES_SECRET_KEY'] = 'gfedcba'

import unittest
from mock import patch
from mock import Mock
import mixcoatl.infrastructure.server as server
import tests.data.server as srv_data

@patch('mixcoatl.resource.Resource.get')
class TestServer(unittest.TestCase):

    def test_has_all_servers_and_id_Server(self, mock_data):
        '''test all() returns a list of Server'''
        mock_data.return_value = srv_data.all_servers

        s = server.Server.all()
        assert len(s) == 3
        for x in s:
            assert isinstance(x, server.Server), '%s must be an instance of Server' % x

    def test_has_a_firewall(self, mock_data):
        mock_data.return_value = srv_data.one_server

        s = server.Server(331810)
        print s
        assert s.server_id == 331810
        assert s.status == 'RUNNING'
        assert s.agent_version == 17
        assert s.region['region_id'] == 19344
        assert s.data_center['data_center_id'] == 64351

    @patch('mixcoatl.resource.Resource.post')
    def test_launch(self, mock_data, mock_post):
         mock_post.return_value = {u'jobs':[{u'jobId':84322,u'status':u'RUNNING'}]}
         pass