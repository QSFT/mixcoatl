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

import mixcoatl.analytics.tier_analytics as rsrc
from mixcoatl.settings.load_settings import settings
from mixcoatl.utils import camelize

class TestTierAnalytics(unittest.TestCase):
    def setUp(self):
        self.cls = rsrc.TierAnalytics
        self.es_url = '%s/%s' % (settings.endpoint, self.cls.PATH)
        self.json_file = '../../tests/data/unit/analytics/tier_analytics.json'

    @httprettified
    def test_has_all_and_is_one(self):
        '''test all() returns a list of TierAnalytics'''
        with open(self.json_file) as f:
            data = f.read()
        HTTPretty.register_uri(HTTPretty.GET,
            self.es_url+'/'+str(10429),
            body=data,
            status=200,
            content_type="application/json")

        s = self.cls.all(10429)
        assert len(s) == 1

    @httprettified
    def test_has_one(self):
        '''test TierAnalytics(<id>) returns a valid resource'''
        pk = 10429
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
        assert s.tier_id == pk
        assert len(s.data_points) == 9
        assert s.interval_in_minutes == 5
        assert s.period_start == '2013-01-08T03:01:39.992+0000'
        assert s.period_end == '2013-01-08T03:51:34.996+0000'
