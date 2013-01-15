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

import mixcoatl.analytics.server_analytics as rsrc
from mixcoatl.settings.load_settings import settings
from mixcoatl.utils import camelize

class TestServerAnalytics(unittest.TestCase):
    def setUp(self):
        self.cls = rsrc.ServerAnalytics
        self.es_url = '%s/%s' % (settings.endpoint, self.cls.path)
        self.json_file = '../../tests/data/unit/analytics/server_analytics.json'

    @httprettified
    def test_has_all_and_is_one(self):
        '''test all() returns a list of ServerAnalytics'''

        with open(self.json_file) as f:
            data = f.read()
        HTTPretty.register_uri(HTTPretty.GET,
            self.es_url+'/'+str(331810),
            body=data,
            status=200,
            content_type="application/json")

        s = self.cls.all(331810)
        assert isinstance(s, self.cls)

    @httprettified
    def test_has_one(self):
        '''test ServerAnalytics(<id>) returns a valid resource'''
        pk = 331810
        with open(self.json_file) as f:
            data = json.load(f)
        data[self.cls.collection_name][:] = [d for d in data[self.cls.collection_name] if
                                             d[camelize(self.cls.primary_key)] == pk]
        HTTPretty.register_uri(HTTPretty.GET,
            self.es_url + '/' + str(pk),
            body=json.dumps(data),
            status=200,
            content_type="application/json")
        s = self.cls(pk)
        assert s.server_id == pk
        assert len(s.data_points) == 53
        assert s.interval_in_minutes == 1
        assert s.period_start == '2013-01-07T19:43:40.406+0000'
        assert s.period_end == '2013-01-07T20:37:12.333+0000'
