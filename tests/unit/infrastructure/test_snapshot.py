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

import mixcoatl.infrastructure.snapshot as rsrc
from mixcoatl.settings.load_settings import settings
from mixcoatl.utils import camelize


class TestSnapshot(unittest.TestCase):
    def setUp(self):
        self.cls = rsrc.Snapshot
        self.es_url = '%s/%s' % (settings.endpoint, self.cls.PATH)
        self.json_file = '../../tests/data/unit/infrastructure/snapshot.json'

    @httprettified
    def test_has_all_and_is_one(self):
        '''test all() returns a list of Snapshot'''

        with open(self.json_file) as f:
            data = f.read()
        HTTPretty.register_uri(HTTPretty.GET,
            self.es_url,
            body=data,
            status=200,
            content_type="application/json")

        s = self.cls.all()
        assert len(s) == 19
        for x in s:
            assert isinstance(x, self.cls)

    @httprettified
    def test_has_one(self):
        '''test Snapshot(<id>) returns a valid resource'''
        pk = 23237460
        with open(self.json_file) as f:
            data = json.load(f)
        data[self.cls.COLLECTION_NAME][:] = [d for d in data[self.cls.COLLECTION_NAME] if
                                             d[camelize(self.cls.PRIMARY_KEY)] == pk]

        HTTPretty.register_uri(HTTPretty.GET,
            self.es_url+'/'+str(pk),
            body=json.dumps(data),
            status=200,
            content_type="application/json")

        s = self.cls(pk)

        assert s.snapshot_id == 23237460
        assert s.available is True
        assert s.label is None
        assert s.budget  == 10287
        assert s.created_timestamp == '2012-11-20T01:31:53.000+0000'
        assert s.status == 'ACTIVE'
        assert s.region['region_id'] == 19556
        assert s.customer['customer_id'] == 12345
        assert s.encrypted is False
        assert s.description == 'snap-b0810e80'
        assert s.sharable is True
        assert s.name == 'snap-b0810e80'
        assert s.volume['volume_id'] == 209179
        assert s.provider_id == 'snap-b0810e80'
        assert s.cloud['cloud_id'] == 1
        assert s.owning_account['account_id'] == 16000
        assert s.removable is True
        assert s.size_in_gb -- 8
