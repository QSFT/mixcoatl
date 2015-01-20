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

import mixcoatl.admin.api_key as api_key
from mixcoatl.settings.load_settings import settings


class TestApiKey(unittest.TestCase):
    def setUp(self):
        self.es_url = settings.endpoint + '/' + api_key.ApiKey.PATH

    # @httprettified
    # def test_has_all_and_is_one(self):
    #     '''test ApiKey.all() returns a list of ApiKey'''

    #     with open('../../tests/data/unit/admin/apikey.json') as f:
    #         data = f.read()
    #     HTTPretty.register_uri(HTTPretty.GET,
    #         self.es_url,
    #         body=data,
    #         status=200,
    #         content_type="application/json")

    #     s = api_key.ApiKey.all()
    #     assert len(s) == 3
    #     for x in s:
    #         assert isinstance(x, api_key.ApiKey)

    # @httprettified
    # def test_has_one(self):
    #     '''test ApiKey(<id>) returns a valid resource'''
    #     with open('../../tests/data/unit/admin/apikey.json') as f:
    #         data = json.load(f)
    #     data['apiKeys'][:] = [d for d in data['apiKeys'] if d['accessKey'] == 'SLARTIBARTFAST']
    #     HTTPretty.register_uri(HTTPretty.GET,
    #         self.es_url+'/SLARTIBARTFAST',
    #         body=json.dumps(data),
    #         status=200,
    #         content_type="application/json")

    #     s = api_key.ApiKey('SLARTIBARTFAST')
    #     assert s.access_key == 'SLARTIBARTFAST'
    #     assert s.account['account_id'] == 16000
    #     assert s.activation == '2012-11-15T21:42:09.429+0000'
    #     assert s.customer['customer_id'] == 12345
    #     assert s.customer_management_key is False
    #     assert s.description == "Brian's Keys"
    #     assert s.secret_key == 'abcdefg+hijklmnop'
    #     assert s.state == 'ACTIVE'
    #     assert s.system_management_key is False
    #     assert s.user['user_id'] == -1
