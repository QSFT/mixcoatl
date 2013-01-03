import os
# These have to be set before importing any mixcoatl modules
os.environ['ES_ACCESS_KEY'] = 'abcdefg'
os.environ['ES_SECRET_KEY'] = 'gfedcba'

import unittest
from mock import patch
from mock import Mock
import mixcoatl.geography.cloud as cloud
import tests.data.cloud as cloud_data

@patch('mixcoatl.resource.Resource.get')
class TestClouds(unittest.TestCase):

    def setUp(self):
        self.last_error = '{"error":{"message":"job terminated unexpectedly"}}'

    def test_has_all_clouds_and_is_Cloud(self, mock_data):
        '''test all() returns a list of Cloud'''
        mock_data.return_value = cloud_data.all_clouds

        c = cloud.Cloud.all()
        assert len(c) == 29
        for x in c:
            assert isinstance(x, cloud.Cloud), "%s must be an instance of Cloud" % x