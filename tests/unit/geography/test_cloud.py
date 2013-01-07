import os
# These have to be set before importing any mixcoatl modules
os.environ['ES_ACCESS_KEY'] = 'abcdefg'
os.environ['ES_SECRET_KEY'] = 'gfedcba'

import unittest
from mock import patch
from mock import Mock
import mixcoatl.geography.cloud as cloud
import tests.data.cloud as cloud_data

@patch('mixcoatl.resource.Resource.get')
class TestClouds(unittest.TestCase):

    def setUp(self):
        self.last_error = '{"error":{"message":"job terminated unexpectedly"}}'

    def test_has_all_clouds_and_is_Cloud(self, mock_data):
        '''test all() returns a list of Cloud'''
        mock_data.return_value = cloud_data.all_clouds

        c = cloud.Cloud.all()
        assert len(c) == 29
        for x in c:
            assert isinstance(x, cloud.Cloud), "%s must be an instance of Cloud" % x

    def test_has_a_cloud(self, mock_data):
        mock_data.return_value = cloud_data.one_cloud

        c = cloud.Cloud(1)
        assert c.cloud_id == 1
        assert c.status == 'ACTIVE'
        assert c.cloud_provider_console_url == 'http://aws.amazon.com'
        assert c.cloud_provider_logo_url == '/clouds/aws.gif'
        assert c.cloud_provider_name == 'Amazon'
        assert c.compute_access_key_label == 'AWS_ACCESS_KEY'
        assert c.compute_account_number_label == 'AWS_ACCOUNT_NUMBER'
        assert c.compute_delegate == 'org.dasein.cloud.aws.AWSCloud'
        assert c.compute_endpoint == 'https://ec2.us-east-1.amazonaws.com,https://ec2.us-west-1.amazonaws.com,https://ec2.eu-west-1.amazonaws.com'
        assert c.compute_secret_key_label == 'AWS_SECRET_ACCESS_KEY'
        assert c.compute_x509_cert_label == 'AWS_CERTIFICATE'
        assert c.compute_x509_key_label == 'AWS_PRIVATE_KEY'
        assert c.documentation_label is None
        assert c.name == 'Amazon Web Services'
        assert c.private_cloud is False
        assert c.status == 'ACTIVE'