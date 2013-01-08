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

import mixcoatl.automation.deployment as rsrc
from mixcoatl.settings.load_settings import settings
from mixcoatl.utils import camelize

class TestDeployment(unittest.TestCase):
    def setUp(self):
        self.cls = rsrc.Deployment
        self.es_url = '%s/%s' % (settings.endpoint, self.cls.path)
        self.json_file = '../../tests/data/unit/automation/deployment.json'

    @httprettified
    def test_has_all_and_is_one(self):
        '''test all() returns a list of Deployment'''

        with open(self.json_file) as f:
            data = f.read()
        HTTPretty.register_uri(HTTPretty.GET,
            self.es_url,
            body=data,
            status=200,
            content_type="application/json")

        s = self.cls.all()
        assert len(s) == 10
        for x in s:
            assert isinstance(x, self.cls)

    @httprettified
    def test_has_one(self):
        '''test Deployment(<id>) returns a valid resource'''
        pk = 13392
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
        assert s.deployment_id == pk
        assert s.backup_window['days_of_week'] == ['SUNDAY', 'MONDAY', 'TUESDAY',
                                                   'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY']
        assert s.budget == 9465
        assert s.creation_timestamp == '2012-11-13T22:57:45.622+0000'
        assert s.customer['customer_id'] == 12345
        assert s.description == 'Copied from dpando-Wordpress-MySQLreplication'
        assert s.for_service_catalog is False
        assert s.launch_timestamp == '1970-01-01T00:00:00.000+0000'
        assert s.maintenance_window['days_of_week'] == ['SUNDAY', 'MONDAY', 'TUESDAY',
                                                        'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY']
        assert s.name == 'DemoDeployment'
        assert s.owning_groups[0]['group_id'] == 9465
        assert s.regions[0]['region_id'] == 19344
        assert s.removable is True
        assert s.status == 'STOPPED'
        assert s.e_type == 'DEDICATED'