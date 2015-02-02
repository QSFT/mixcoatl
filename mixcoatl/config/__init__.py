import os
import datetime

from mixcoatl.exceptions import ConfigException


def validate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return date_text
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")


class Config(object):
    # pylint: disable-msg=E0710

    def __init__(self):
        self.access_key = None
        self.secret_key = None
        self.endpoint = None
        self.user_agent = 'mixcoatl'
        self.api_version = None
        self.basepath = None
        self.default_api_version = '2014-07-30'
        self.ssl_verify = None

    def configure(self):
        if self.access_key is None:
            if 'ES_ACCESS_KEY' in os.environ and 'DCM_ACCESS_KEY' not in os.environ:
                os.environ['DCM_ACCESS_KEY'] = os.environ['ES_ACCESS_KEY']

            if 'DCM_ACCESS_KEY' in os.environ:
                self.set_access_key(os.environ['DCM_ACCESS_KEY'])
            else:
                raise ConfigException('missing DCM_ACCESS_KEY')

        if self.secret_key is None:
            if 'ES_SECRET_KEY' in os.environ and 'DCM_SECRET_KEY' not in os.environ:
                os.environ['DCM_SECRET_KEY'] = os.environ['ES_SECRET_KEY']

            if 'DCM_SECRET_KEY' in os.environ:
                self.set_secret_key(os.environ['DCM_SECRET_KEY'])
            else:
                raise ConfigException('missing DCM_SECRET_KEY')

        if self.api_version is None:
            if 'ES_API_VERSION' in os.environ and 'DCM_API_VERSION' not in os.environ:
                os.environ['DCM_API_VERSION'] = os.environ['ES_API_VERSION']

            if 'DCM_API_VERSION' in os.environ:
                self.set_api_version(os.environ['DCM_API_VERSION'])
            else:
                if 'DCM_ENDPOINT' in os.environ:
                    str = os.environ['DCM_ENDPOINT'].split('/')

                    if validate(str[-1]):
                        self.set_api_version(str[-1])
                    else:
                        self.set_api_version(self.default_api_version)
                else:
                    self.set_api_version(self.default_api_version)

            self.set_basepath('/api/enstratus/%s' % self.api_version)

        if self.endpoint is None:
            if 'ES_ENDPOINT' in os.environ and 'DCM_ENDPOINT' not in os.environ:
                os.environ['DCM_ENDPOINT'] = os.environ['ES_ENDPOINT']

            if 'DCM_ENDPOINT' in os.environ:
                self.set_endpoint(os.environ['DCM_ENDPOINT'])
            else:
                self.set_endpoint('https://api.enstratus.com' + self.basepath)

        if self.ssl_verify is None:
            if 'ES_SSL_VERIFY' in os.environ and 'DCM_SSL_VERIFY' not in os.environ:
                os.environ['DCM_SSL_VERIFY'] = os.environ['ES_SSL_VERIFY']

            if 'DCM_SSL_VERIFY' in os.environ:
                self.set_ssl_verify(os.environ['DCM_SSL_VERIFY'])
            else:
                self.set_ssl_verify('1')

    def set_access_key(self, key):
        self.access_key = key

    def set_secret_key(self, key):
        self.secret_key = key

    def set_endpoint(self, ep):
        self.endpoint = ep

    def set_api_version(self, version):
        self.api_version = version

    def set_basepath(self, basepath):
        self.basepath = basepath

    def set_ssl_verify(self, verify):
        if verify == '0':
            self.ssl_verify = False
        else:
            self.ssl_verify = True
