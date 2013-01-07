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

import mixcoatl.admin.role as rsrc
from mixcoatl.settings.load_settings import settings

class TestRole(unittest.TestCase):
    def setUp(self):
        self.cls = rsrc.Role
        self.es_url = '%s/%s' % (settings.endpoint, self.cls.path)
        self.json_file = '../../tests/data/unit/admin/role.json'

    @httprettified
    def test_has_all_and_is_one(self):
        '''test all() returns a list of Role'''

        with open(self.json_file) as f:
            data = f.read()
        HTTPretty.register_uri(HTTPretty.GET,
            self.es_url,
            body=data,
            status=200,
            content_type="application/json")

        s = self.cls.all()
        assert len(s) == 2
        for x in s:
            assert isinstance(x, self.cls)

    @httprettified
    def test_has_one(self):
        '''test Role(<id>) returns a valid resource'''
        pk = 13712
        with open(self.json_file) as f:
            data = json.load(f)
        data[self.cls.collection_name][:] = [d for d in data[self.cls.collection_name] if d[self.cls.primary_key] == pk]
        HTTPretty.register_uri(HTTPretty.GET,
            self.es_url + '/' + str(pk),
            body=json.dumps(data),
            status=200,
            content_type="application/json")
        s = self.cls(pk)
        assert s.role_id == pk