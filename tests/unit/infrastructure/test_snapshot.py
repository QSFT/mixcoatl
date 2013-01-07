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

import mixcoatl.infrastructure.snapshot as snapshot
from mixcoatl.settings.load_settings import settings
import tests.data.snapshot as snap_data


class TestSnapshot(unittest.TestCase):
    def setUp(self):
        self.es_url = settings.endpoint + '/' + snapshot.Snapshot.path

    @httprettified
    def test_has_all_snapshots_and_is_Snapshot(self):
        '''test all() returns a list of Snapshot'''

        data = snap_data.all_items
        HTTPretty.register_uri(HTTPretty.GET,
            self.es_url,
            body=data,
            status=200,
            content_type="application/json")

        s = snapshot.Snapshot.all()
        print len(s)
        assert len(s) == 19
        for x in s:
            assert isinstance(x, snapshot.Snapshot)

    @httprettified
    def test_has_a_snapshot(self):
        url = self.es_url + '/23237460'
        data = snap_data.one_item

        HTTPretty.register_uri(HTTPretty.GET,
            url,
            body=data,
            status=200,
            content_type="application/json")

        s = snapshot.Snapshot(23237460)

        assert s.snapshot_id == 23237460
        assert s.available is True
        assert s.label is None
        assert s.budget  == 10287
        assert s.created_timestamp == '2012-11-20T01:31:53.000+0000'
        assert s.status == 'ACTIVE'
        assert s.region['region_id'] == 19556
        assert s.customer['customer_id'] == 11111
        assert s.encrypted is False
        assert s.description == 'snap-b0810e80'
        assert s.sharable is True
        assert s.name == 'snap-b0810e80'
        assert s.volume['volume_id'] == 209179
        assert s.provider_id == 'snap-b0810e80'
        assert s.cloud['cloud_id'] == 1
        assert s.owning_account['account_id'] == 16000