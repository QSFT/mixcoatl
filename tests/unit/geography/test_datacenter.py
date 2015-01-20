import os
# These have to be set before importing any mixcoatl modules
os.environ['ES_ACCESS_KEY'] = 'abcdefg'
os.environ['ES_SECRET_KEY'] = 'gfedcba'

import unittest
from mock import patch
from mock import Mock
import mixcoatl.geography.datacenter as datacenter
import tests.data.datacenter as dc_data

@patch('mixcoatl.resource.Resource.get')
class TestDataCenters(unittest.TestCase):

    def setUp(self):
        self.last_error = 'job terminated unexpectedly'

    # def test_has_all_dcs_and_is_DataCenter(self, mock_data):
    #     '''test all() returns a list of DataCenter'''
    #     mock_data.return_value = dc_data.all_datacenters

    #     d = datacenter.DataCenter.all(19344)
    #     assert len(d) == 3
    #     for x in d:
    #         assert isinstance(x, datacenter.DataCenter), '%s must be an instance of DataCenter' % x

    # def test_has_a_datacenter(self, mock_data):
    #     mock_data.return_value = dc_data.one_datacenter

    #     d = datacenter.DataCenter(64351)
    #     assert d.data_center_id == 64351
    #     assert d.status == 'ACTIVE'
    #     assert d.provider_id == 'us-west-2a'
