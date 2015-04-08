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

import mixcoatl.admin.group as grp
from mixcoatl.settings.load_settings import config

class TestGroups(unittest.TestCase):
    def setUp(self):
        self.es_url = config.endpoint + '/' + grp.Group.PATH

    @httprettified
    def test_has_all_and_is_one(self):
        '''test Group.all() returns a list of Group'''
        with open('../../tests/data/unit/admin/group.json') as f:
            data = f.read()
        HTTPretty.register_uri(HTTPretty.GET,
            self.es_url,
            body=data,
            status=200,
            content_type="application/json")

        s = grp.Group.all()
        assert len(s) == 2

    @httprettified
    def test_has_one(self):
        '''test Group(<id>) returns a valid resource'''
        with open('../../tests/data/unit/admin/group.json') as f:
            data = json.load(f)
        data[grp.Group.COLLECTION_NAME][:] = [d for d in data[grp.Group.COLLECTION_NAME] if d['groupId'] == 9848]
        HTTPretty.register_uri(HTTPretty.GET,
            self.es_url + '/9848',
            body=json.dumps(data),
            status=200,
            content_type="application/json")
        s = grp.Group(9848)
        assert s.group_id == 9848
        assert s.customer['customer_id'] == 12345
        assert s.description == 'The Development group'
        assert s.name == 'Development'
        assert s.status == 'ACTIVE'
