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

import mixcoatl.infrastructure.volume as rsrc
from mixcoatl.settings.load_settings import settings
from mixcoatl.utils import camelize

class TestVolume(unittest.TestCase):
    def setUp(self):
        self.cls = rsrc.Volume
        self.es_url = '%s/%s' % (settings.endpoint, self.cls.PATH)
        self.json_file = '../../tests/data/unit/infrastructure/volume.json'
        with open(self.json_file) as f:
            self.raw_data = json.load(f)

    # @httprettified
    # def test_has_all_and_is_one(self):
    #     '''Volume.all() returns a list of Volume'''

    #     with open(self.json_file) as f:
    #         data = f.read()
    #     HTTPretty.register_uri(HTTPretty.GET,
    #         self.es_url,
    #         body=data,
    #         status=200,
    #         content_type="application/json")

    #     for d in self.raw_data[self.cls.COLLECTION_NAME]:
    #         rec = {self.cls.COLLECTION_NAME:[d]}
    #         u = self.es_url+'/'+str(d['volumeId'])
    #         HTTPretty.register_uri(HTTPretty.GET,
    #                 u,
    #                 body=json.dumps(rec),
    #                 status=200,
    #                 content_type="application/json")

    #     s = self.cls.all()
    #     assert len(s) == 17
    #     for x in s:
    #         assert isinstance(x, self.cls)

    @httprettified
    def test_has_all_keys_only(self):
        '''Volume.all(keys_only=True) returns a list of keys'''

        with open(self.json_file) as f:
            data = f.read()
        HTTPretty.register_uri(HTTPretty.GET,
            self.es_url,
            body=data,
            status=200,
            content_type="application/json")

        for d in self.raw_data[self.cls.COLLECTION_NAME]:
            rec = {self.cls.COLLECTION_NAME:[d]}
            u = self.es_url+'/'+str(d['volumeId'])
            HTTPretty.register_uri(HTTPretty.GET,
                    u,
                    body=json.dumps(rec),
                    status=200,
                    content_type="application/json")

        s = self.cls.all(keys_only=True)
        assert len(s) == 17
        [self.assertIsInstance(x, int) for x in s]

    @httprettified
    def test_has_one(self):
        '''test Volume(<id>) returns a valid resource'''
        pk = 211309
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
        s.load()
        assert s.volume_id == pk
        assert s.available is True
        assert s.budget == 10287
        assert s.cloud['cloud_id'] == 1
        assert s.creation_timestamp == '1970-01-01T00:00:00.000+0000'
        assert s.customer['customer_id'] == 12345
        assert s.data_center['data_center_id'] == 64716
        assert s.description == 'vol-4816d27b'
        assert s.device_id == '/dev/sda1'
        assert s.encrypted is False
        assert s.name == 'vol-4816d27b'
        assert s.owning_account['account_id'] == 16000
        assert s.owning_groups[0]['group_id'] == 9465
        assert s.provider_id == 'vol-4816d27b'
        assert s.owning_user['user_id'] == 54321
        assert s.region['region_id'] == 19556
        assert s.removable is False
        assert s.server['server_id'] == 322765
        assert s.size_in_gb == 8
        assert s.size_string == '8GB'
        assert s.status == 'ACTIVE'
