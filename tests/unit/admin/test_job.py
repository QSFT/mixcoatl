import os
# These have to be set before importing any mixcoatl modules
os.environ['ES_ACCESS_KEY'] = 'abcdefg'
os.environ['ES_SECRET_KEY'] = 'gfedcba'

import unittest
from mock import patch
from mock import Mock
import mixcoatl.admin.job as job
import tests.data.job as job_data

@patch('mixcoatl.resource.Resource.get')
class TestJobs(unittest.TestCase):

    def setUp(self):
        self.last_error = '{"error":{"message":"job terminated unexpectedly"}}'

    def test_all_jobs(self,mock_job_get):
        '''test Job.all()'''
        mock_job_get.return_value = job_data.jobs
        j = job.Job.all()
        assert len(j) == 3

    def test_get_job(self, mock_job_get):
        '''test Job.get_job(job_id)'''
        mock_job_get.return_value = job_data.one_job
        j = job.Job()
        jb = j.get_job(76115)
        assert jb['jobs'][0]['status'] == 'COMPLETE'

    def test_job_get(self, mock_job_get):
        '''test job.get(jobid)'''
        mock_job_get.return_value = job_data.one_job
        j = job.get(76115)
        assert j['status'] == 'COMPLETE'


    def test_job_get_last_error(self,mock_job_get):
        '''test failure on job.get()'''
        with patch('mixcoatl.resource.Resource.last_error', autospec=True) as mock_last_error:
            mock_last_error.__get__ = Mock(return_value=self.last_error)
            j = job.get(12345)
            assert j == self.last_error

    def test_all_last_error(self,mock_job_get):
        '''test failure on all()'''
        with patch('mixcoatl.resource.Resource.last_error', autospec=True) as mock_last_error:
            mock_last_error.__get__ = Mock(return_value=self.last_error)
            j = job.Job.all()
            assert j == self.last_error


