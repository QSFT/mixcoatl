import os

from mixcoatl.exceptions import ConfigException

class Config(object):
    # pylint: disable-msg=E0710
    def __init__(self):
        self.access_key = None
        self.secret_key = None
        self.endpoint = None
        self.user_agent = 'mixcoatl'
        self.api_version = None
        self.basepath = None

    def configure(self):
        if self.access_key is None:
            if 'ES_ACCESS_KEY' in os.environ:
                self.set_access_key(os.environ['ES_ACCESS_KEY'])
            else:
                raise ConfigException('missing ES_ACCESS_KEY')
        if self.secret_key is None:
            if 'ES_SECRET_KEY' in os.environ:
                self.set_secret_key(os.environ['ES_SECRET_KEY'])
            else:
                raise ConfigException('missing ES_SECRET_KEY')
        if self.api_version is None:
            if 'ES_API_VERSION' in os.environ:
                self.set_api_version(os.environ['ES_API_VERSION'])
            else:
                self.set_api_version('2012-06-15')
            self.set_basepath('/api/enstratus/%s' % self.api_version)

        if self.endpoint is None:
            if 'ES_ENDPOINT' in os.environ:
                self.set_endpoint(os.environ['ES_ENDPOINT'])
            else:
                self.set_endpoint('https://api.enstratus.com'+self.basepath)

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
