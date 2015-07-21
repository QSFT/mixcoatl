import sys
# These have to be set before importing any mixcoatl modules
import os
os.environ['ES_ACCESS_KEY'] = 'abcdefg'
os.environ['ES_SECRET_KEY'] = 'gfedcba'

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

from mixcoatl.resource import Endpoint

class TestEndpoint(unittest.TestCase):

    def setUp(self):
        self.cls = Endpoint

    def test_from_file(self):
        '''test loading endpoint definitions from a json file'''

        e = Endpoint.from_file("../../tests/data/unit/admin/endpoint.json")
        assert e.nickname == "saas"
        assert e.url == "https://dcm.enstratius.com/api/enstratus/2015-05-25"
        assert e.api_version == "2015-05-25"
        assert e.access_key == "abcdefg"
        assert e.secret_key == "gfedcba"
        assert e.ssl_verify == True

    def test_multiple_from_file(self):
        '''test loading multiple endpoints from file'''
        e = Endpoint.multiple_from_file("../../tests/data/unit/admin/endpoints.json")
        assert e['saas'].nickname == "saas"
        assert e['saas'].url == "https://dcm.enstratius.com/api/enstratus/2015-05-25"
        assert e['saas'].api_version == "2015-05-25"
        assert e['saas'].access_key == "abcdefg"
        assert e['saas'].secret_key == "gfedcba"
        assert e['saas'].ssl_verify is True

        assert e['vagrant'].nickname == "vagrant"
        assert e['vagrant'].url == "https://vagrant.vm/api/enstratus/2015-05-25"
        assert e['vagrant'].api_version == "2015-05-25"
        assert e['vagrant'].access_key == "abcdefg"
        assert e['vagrant'].secret_key == "gfedcba"
        assert e['vagrant'].ssl_verify is True
        