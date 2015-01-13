import os
# These have to be set before importing any mixcoatl modules
os.environ['ES_ACCESS_KEY'] = 'abcdefg'
os.environ['ES_SECRET_KEY'] = 'gfedcba'

import unittest
import mixcoatl.infrastructure.server_product as sp
import tests.data.server_product as sp_data
from httpretty import HTTPretty
from httpretty import httprettified
from mixcoatl.settings.load_settings import settings

class TestServerProduct(unittest.TestCase):
    """Test ServerProduct API"""

    def setUp(self):
        self.es_url = settings.endpoint+'/'+sp.ServerProduct.PATH

    # @httprettified
    # def test_has_all_and_is_one(self):
    #     """Test ServerProduct.all() returns a list of ServerProduct"""

    #     data = sp_data.one_product
    #     individual_url = self.es_url+'/693'

    #     HTTPretty.register_uri(HTTPretty.GET,
    #         self.es_url,
    #         body = data,
    #         status = 200,
    #         content_type = "application/json")

    #     HTTPretty.register_uri(HTTPretty.GET,
    #         individual_url,
    #         body = data,
    #         status = 200,
    #         content_type = "application/json")

    #     s = sp.ServerProduct.all(19344)
    #     assert len(s) == 1
    #     for x in s:
    #         assert isinstance(x, sp.ServerProduct)

    # @httprettified
    # def test_has_all_keys_only(self):
    #     """Test ServerProduct.all(keys_only=True) returns a list of keys"""

    #     data = sp_data.one_product

    #     HTTPretty.register_uri(HTTPretty.GET,
    #         self.es_url,
    #         body = data,
    #         status = 200,
    #         content_type = "application/json")

    #     s = sp.ServerProduct.all(19344, keys_only=True)
    #     assert len(s) == 1
    #     assert s[0] == 693

    # @httprettified
    # def test_has_a_server_product(self):
    #     """Test ServerProduct(<id>) returns a valid resource"""

    #     url = self.es_url+'/693'
    #     data = sp_data.one_product

    #     HTTPretty.register_uri(HTTPretty.GET,
    #         url,
    #         body = data,
    #         status = 200,
    #         content_type = "application/json")

    #     s = sp.ServerProduct(693)

    #     assert s.product_id == 693
    #     assert s.cpu_count == 2
    #     assert s.platform == 'UNIX'
    #     assert s.hourly_rate == 0.17
    #     assert s.provider_region_id == 'us-west-2'
    #     assert s.ram_in_mb == 1700
    #     assert s.architecture == 'I32'
    #     assert s.cpu_speed_in_mhz == 2
    #     assert s.currency == 'USD'
    #     assert s.software == ''
    #     assert s.disk_size_in_gb == 350
    #     assert s.description == '32-bit, 2x2.5 CPU, 1.7 GB RAM, 350 GB Disk'
    #     assert s.name == '32-bit High CPU Medium'
    #     assert s.cloud['cloud_id'] == 1
    #     assert s.provider_product_id == 'c1.medium'
