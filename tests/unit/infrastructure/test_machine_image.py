import os
# These have to be set before importing any mixcoatl modules
os.environ['ES_ACCESS_KEY'] = 'abcdefg'
os.environ['ES_SECRET_KEY'] = 'gfedcba'

import unittest
import mixcoatl.infrastructure.machine_image as mi
import tests.data.machine_image as mi_data
from httpretty import HTTPretty
from httpretty import httprettified
from mixcoatl.settings.load_settings import settings

class TestMachineImage(unittest.TestCase):

    def setUp(self):
        self.es_url = settings.endpoint+'/'+mi.MachineImage.PATH


    @httprettified
    def test_has_all_and_is_one(self):

        data = mi_data.one_image
        individual_url = self.es_url+'/284542'

        HTTPretty.register_uri(HTTPretty.GET,
            self.es_url,
            body = data,
            status = 200,
            content_type = "application/json")

        HTTPretty.register_uri(HTTPretty.GET,
            individual_url,
            body = data,
            status = 200,
            content_type = "application/json")

        m = mi.MachineImage.all(19344)
        assert len(m) == 1
        for x in m:
            assert isinstance(x, mi.MachineImage)

    @httprettified
    def test_all_keys_only(self):

        data = mi_data.one_image

        HTTPretty.register_uri(HTTPretty.GET,
            self.es_url,
            body = data,
            status = 200,
            content_type = "application/json")

        m = mi.MachineImage.all(19344, keys_only=True)
        assert len(m) == 1
        assert m[0] == 284542

    @httprettified
    def test_has_one(self):
        url = self.es_url+'/284542'
        data = mi_data.one_image
        HTTPretty.register_uri(HTTPretty.GET,
            url,
            body = data,
            status = 200,
            content_type = "application/json")

        m = mi.MachineImage(284542)

        assert m.machine_image_id == 284542
        assert m.sharable is False
        assert m.budget == 10287
        assert m.platform == 'UBUNTU'
        assert m.architecture == 'I64'
        assert m.removable is True
        assert m.region['region_id'] == 19344
        assert m.status == 'ACTIVE'
        assert m.owning_cloud_account_number == '099720109477'
        assert m.customer['customer_id'] == 11111
        assert m.description == 'ubuntu-lucid-10.04-amd64-server-20120913 (x86_64 Ubuntu)'
        assert m.name == 'ubuntu/images/ebs/ubuntu-lucid-10.04-amd64-server-20120913'
        assert m.cloud['cloud_id'] == 1
        assert m.provider_id == 'ami-1a4fc12a'
        assert m.creation_timestamp == '1970-01-01T00:00:00.000+0000'
        assert m.owning_user['user_id'] == 12345
        assert m.agent_version == 17
