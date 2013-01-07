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
from mixcoatl.settings.load_settings import settings

class TestGroups(unittest.TestCase):
    def setUp(self):
        self.es_url = settings.endpoint + '/' + grp.Group.path

    @httprettified
    def test_has_all_group_and_is_Group(self):
        '''test all() returns a list of BillingCode'''

        with open('../../tests/data/unit/admin/group.json') as f:
            data = f.read()
        HTTPretty.register_uri(HTTPretty.GET,
            self.es_url,
            body=data,
            status=200,
            content_type="application/json")

        s = grp.Group.all()
        assert len(s) == 2
        for x in s:
            assert isinstance(x, grp.Group)

    @httprettified
    def test_has_a_group(self):
        with open('../../tests/data/unit/admin/group.json') as f:
            data = json.load(f)
        data[grp.Group.collection_name][:] = [d for d in data[grp.Group.collection_name] if d['groupId'] == 9848]
        HTTPretty.register_uri(HTTPretty.GET,
            self.es_url + '/9848',
            body=json.dumps(data),
            status=200,
            content_type="application/json")
        s = grp.Group(9848)
        assert s.group_id == 9848