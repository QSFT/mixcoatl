import os
# These have to be set before importing any mixcoatl modules
os.environ['ES_ACCESS_KEY'] = 'abcdefg'
os.environ['ES_SECRET_KEY'] = 'gfedcba'

import unittest
from mock import patch
from mock import Mock
import mixcoatl.geography.region as region
import tests.data.region as region_data

@patch('mixcoatl.resource.Resource.get')
class TestRegions(unittest.TestCase):

    def setUp(self):
        self.last_error = '{"error":{"message":"job terminated unexpectedly"}}'

    def test_has_all_regions_and_is_Region(self, mock_data):
        '''test all() returns a list of Region'''
        mock_data.return_value = region_data.all_regions

        d = region.Region.all()
        assert len(d) == 8
        for x in d:
            assert isinstance(x, region.Region), '%s must be an instance of Region' % x

    def test_has_a_region(self, mock_data):
        mock_data.return_value = region_data.one_region

        d = region.Region(19341)
        # test primary_key
        assert d.region_id == 19341
        # test lazy property
        assert d.status == 'ACTIVE'
        # test uncameled property
        assert d.provider_id == 'ap-northeast-1'
        # test nested uncameled key
        assert d.customer['customer_id'] == 11111