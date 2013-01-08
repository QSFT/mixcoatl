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

import mixcoatl.automation.service as rsrc
from mixcoatl.settings.load_settings import settings
from mixcoatl.utils import camelize

class TestService(unittest.TestCase):
    def setUp(self):
        self.cls = rsrc.Service
        self.es_url = '%s/%s' % (settings.endpoint, self.cls.path)
        self.json_file = '../../tests/data/unit/automation/service.json'

    @httprettified
    def test_has_all_and_is_one(self):
        '''test all() returns a list of Service'''

        with open(self.json_file) as f:
            data = f.read()
        HTTPretty.register_uri(HTTPretty.GET,
            self.es_url,
            body=data,
            status=200,
            content_type="application/json")

        s = self.cls.all()
        assert len(s) == 1
        for x in s:
            assert isinstance(x, self.cls)

    @httprettified
    def test_has_one(self):
        '''test Service(<id>) returns a valid resource'''
        pk = 11621
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
        assert s.service_id == pk
        assert s.backup_interval_in_minutes == 0
        assert s.budget == 10287
        assert s.description == 'wordpress-mysql'
        assert s.name == 'wordpress-mysql'
        assert s.owning_group[0]['group_id'] == 9465
        assert s.owning_user['user_id'] == 54321
        assert s.run_as_user is None
        assert s.scaling_model == 'REPLICATED'
        assert s.status == 'PAUSED'