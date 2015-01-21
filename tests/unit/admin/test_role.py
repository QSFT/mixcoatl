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
        self.es_url = '%s/%s' % (settings.endpoint, self.cls.PATH)
        self.json_file = '../../tests/data/unit/admin/role.json'

    @httprettified
    def test_has_all_and_is_one(self):
        '''test Role.all() returns a list of Role'''

        with open(self.json_file) as f:
            data = f.read()
        HTTPretty.register_uri(HTTPretty.GET,
            self.es_url,
            body=data,
            status=200,
            content_type="application/json")

        s = self.cls.all()
        assert len(s) == 2

    @httprettified
    def test_has_one(self):
        '''test Role(<id>) returns a valid resource'''
        pk = 13712
        with open(self.json_file) as f:
            data = json.load(f)
        data[self.cls.COLLECTION_NAME][:] = [d for d in data[self.cls.COLLECTION_NAME] if d['roleId'] == pk]
        HTTPretty.register_uri(HTTPretty.GET,
            self.es_url + '/' + str(pk),
            body=json.dumps(data),
            status=200,
            content_type="application/json")
        s = self.cls(pk)
        assert s.role_id == pk
        assert len(s.acl) == 1
        assert s.customer['customer_id'] == 12345
        assert s.name == 'Admin'
        assert s.description == 'General Admin Role'
        assert s.status == 'ACTIVE'
