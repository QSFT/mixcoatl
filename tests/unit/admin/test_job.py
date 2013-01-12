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

import mixcoatl.admin.job as rsrc
from mixcoatl.settings.load_settings import settings
from mixcoatl.utils import camelize

class TestJob(unittest.TestCase):

    def setUp(self):
        self.cls = rsrc.Job
        self.es_url = '%s/%s' % (settings.endpoint, self.cls.path)
        self.json_file = '../../tests/data/unit/admin/job.json'
        with open(self.json_file) as f:
            self.data = f.read()

    @httprettified
    def test_has_all_and_is_one(self):
        '''test Job.all() returns a list of Job'''

        HTTPretty.register_uri(HTTPretty.GET,
            self.es_url,
            body=self.data,
            status=200,
            content_type="application/json")

        j = self.cls.all()
        assert len(j) == 5
        for x in j:
            assert isinstance(x, self.cls)

    @httprettified
    def test_has_one(self):
        '''test Job(<id>) returns a valid resource'''

        pk = 2
        with open(self.json_file) as f:
            data = json.load(f)
        data[self.cls.collection_name][:] = [d for d in data[self.cls.collection_name] if
                                             d[camelize(self.cls.primary_key)] == pk]
        HTTPretty.register_uri(HTTPretty.GET,
            self.es_url+'/'+str(pk),
            body=json.dumps(data),
            status=200,
            content_type="application/json")

        j = self.cls(pk)
        assert j.job_id == 2
        assert j.status == 'COMPLETE'
        assert j.description == 'Launch Server dpando-CentosLB'
        assert j.message == '339452'
        assert j.start_date == '2013-01-08T21:29:22.733+0000'
        assert j.end_date == '2013-01-08T21:29:59.662+0000'

    @httprettified
    def test_job_get_last_error(self):
        """test failure on job.get()"""

        pk = 5
        json_data = '{"error": {"message": "No such job ID: 5"}}'
        HTTPretty.register_uri(HTTPretty.GET,
            self.es_url+'/'+str(pk),
            body=json_data,
            status=404,
            content_type="application/json")

        j = self.cls(pk)
        j.load()

        assert j.last_error == json.loads(json_data)

    @httprettified
    def test_waiting_for_job(self):
        """test Job.wait_for(<id>) works"""

        with open(self.json_file) as f:
            running_data = json.load(f)

        with open(self.json_file) as f:
            finished_data = json.load(f)

        running_data[self.cls.collection_name][:] = [d for d in running_data[self.cls.collection_name] if
                                                     d[camelize(self.cls.primary_key)] == 4]

        finished_data[self.cls.collection_name][:] = [d for d in finished_data[self.cls.collection_name] if
                                                     d[camelize(self.cls.primary_key)] == 4]

        finished_data[self.cls.collection_name][0]['status'] = 'COMPLETE'
        finished_data[self.cls.collection_name][0]['message'] = '12345'


        HTTPretty.register_uri(HTTPretty.GET,
            self.es_url+'/'+str(4),
            responses = [
                #HTTPretty.Response(body=json.dumps(running_data), status=200, content_type='application/json')
                HTTPretty.Response(body=json.dumps(finished_data), status=200, content_type='application/json')
            ])

        def validate(x):
            assert isinstance(x, self.cls)
            assert x.status == 'COMPLETE'
            assert x.message == '12345'

        y = self.cls.wait_for(4, callback=validate)
        z = self.cls.wait_for(4)
        assert z is True
