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

import mixcoatl.automation.launch_configuration as rsrc
from mixcoatl.settings.load_settings import settings
from mixcoatl.utils import camelize

class TestLaunchConfiguration(unittest.TestCase):
    def setUp(self):
        self.cls = rsrc.LaunchConfiguration
        self.es_url = '%s/%s' % (settings.endpoint, self.cls.PATH)
        self.json_file = '../../tests/data/unit/automation/launch_configuration.json'

    @httprettified
    def test_has_one(self):
        '''test LaunchConfiguration(<id>) returns a valid resource'''
        pk = 16415
        with open(self.json_file) as f:
            data = json.load(f)

        data[self.cls.COLLECTION_NAME][:] = [d for d in data[self.cls.COLLECTION_NAME] if
                                             d[camelize(self.cls.PRIMARY_KEY)] == pk]
        HTTPretty.register_uri(HTTPretty.GET,
            self.es_url + '/' + str(pk),
            body=json.dumps(data),
            status=200,
            content_type="application/json")
        s = self.cls(pk)
        assert s.launch_configuration_id == 16415
        assert s.primary_product['product_id'] == 'm1.medium'
        assert s.secondary_product['product_id'] == 'm1.medium'
        assert s.primary_machine_image['machine_image_id'] == 281731
        assert s.secondary_machine_image['machine_image_id'] == 281731
        assert s.server_name_template == '{group}-{role}-{count}-{timestamp}'
        assert s.firewalls[0]['firewall_id'] == 116387
        assert s.array_volume_capacity == 0
        assert s.array_volume_count == 0
        assert s.customer['customer_id'] == 12345
        assert s.region['region_id'] == 19344
