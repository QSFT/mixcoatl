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

import mixcoatl.admin.user as rsrc
from mixcoatl.settings.load_settings import settings

class TestUserArbitrary(unittest.TestCase):
    def setUp(self):
        self.cls = rsrc.User
        self.es_url = '%s/%s' % (settings.endpoint, self.cls.PATH)
        self.json_file = '../../tests/data/unit/admin/user-arbitrary.json'

    @httprettified
    def test_has_all_and_is_one(self):
        '''test User.all() returns a list of User'''
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
        '''test User(<id>) returns a valid resource, and that we can handle arbitrary keys'''
        pk = 6789
        with open(self.json_file) as f:
            data = json.load(f)
        data[self.cls.COLLECTION_NAME][:] = [d for d in data[self.cls.COLLECTION_NAME] if d['userId'] == pk]
        HTTPretty.register_uri(HTTPretty.GET,
            self.es_url + '/' + str(pk),
            body=json.dumps(data),
            status=200,
            content_type="application/json")
        s = self.cls(pk)
        assert s.user_id == pk
        assert s.alpha_name == 'Vincent, John'

        # check if can if the access methods for an arbitrary set of keys
        # are created correctly are runtime
        assert s.favorite_color == "Blue"
        assert s.quest['name'] == "grail"

        assert s.customer['customer_id'] == 12345
        assert s.editable is False
        assert s.email == 'john.vincent@domain.com'
        assert s.family_name == 'Vincent'
        assert s.given_name == 'John'
        assert s.groups[0]['group_id'] == 9465
        assert s.has_cloud_api_access is False
        assert s.has_cloud_console_access is False
        assert s.status == 'ACTIVE'
        assert s.ssh_public_key == 'ssh-rsa AAAABsshkey user@machine'
        assert s.time_zone == 'America/New_York'
        assert s.user_id == 6789
        assert s.vm_login_id == 'p6789'

