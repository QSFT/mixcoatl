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

import mixcoatl.automation.tier as rsrc
from mixcoatl.settings.load_settings import settings
from mixcoatl.utils import camelize

class TestTier(unittest.TestCase):
    def setUp(self):
        self.cls = rsrc.Tier
        self.es_url = '%s/%s' % (settings.endpoint, self.cls.PATH)
        self.json_file = '../../tests/data/unit/automation/tier.json'

    @httprettified
    def test_has_all_and_is_one(self):
        '''test all() returns a list of Tier'''

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
        '''test Tier(<id>) returns a valid resource'''
        pk = 10429
        with open(self.json_file) as f:
            data = json.load(f)
        data[self.cls.COLLECTION_NAME][:] = [d for d in data[self.cls.COLLECTION_NAME] if
                                             d[camelize(self.cls.PRIMARY_KEY)] == pk]
        HTTPretty.register_uri(HTTPretty.GET,
            self.es_url + '/' + str(pk),
            body=json.dumps(data),
            status=200,
            content_type="application/json")
        s = self.cls(pk)
        assert s.tier_id == pk
        assert s.breach_increment == 1
        assert s.breach_period_in_minutes == 5
        assert s.cooldown_period_in_minutes == 5
        assert s.deployment['deployment_id'] == 13607
        assert s.description == 'This is what we call a tier.'
        assert s.last_breach_change_timestamp == '2012-12-18T18:42:06.160+0000'
        assert s.lower_cpu_threshold == 25
        assert s.lower_ram_threshold == 25
        assert s.maximum_servers == 1
        assert s.minimum_servers == 1
        assert s.name == 'Sample Tier'
        assert s.removable is False
        assert s.scaling_rules == 'BASIC'
        assert s.status == 'BREACH_LOWER'
        assert s.upper_cpu_threshold == 75
        assert s.upper_ram_threshold == 75
