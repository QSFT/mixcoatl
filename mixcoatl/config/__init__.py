import os
import sys
import glob
import shutil
import datetime
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
        self.default_api_version = '2014-07-30'
        self.ssl_verify = None
        self.mixcoatl_dir = os.path.expanduser('~') + "/.mixcoatl"

    def configure(self):
        if not os.path.exists(self.mixcoatl_dir):
            os.makedirs(self.mixcoatl_dir)

        if 'ES_ACCESS_KEY' not in os.environ and 'DCM_ACCESS_KEY' not in os.environ:
            if not os.path.exists(self.mixcoatl_dir + "/default"):
                try:
                    # Python 2
                    prompt = raw_input
                except NameError:
                    # Python 3
                    prompt = input

                cfg_num = 0
                file_list = glob.glob(self.mixcoatl_dir + "/*.config")

                if len(file_list) > 0:
                    for i in file_list:
                        print ">>> Type", cfg_num, "for", i.replace(self.mixcoatl_dir + "/", "").replace(".config", "")
                        cfg_num += 1

                    cfg_pick = prompt("Which config would you like to use? ")

                    shutil.copy(
                        file_list[int(cfg_pick)], self.mixcoatl_dir + "/default")
                else:
                    results = []
                    print "No config file(s) found.  Let us generate one now:"
                    dcm_host = prompt(
                        "What API endpoint would you like to connect to (Example: http[s]://api.endpoint.domain/api/enstratus/<api version>)?\n")
                    dcm_api_access = prompt("What is the API Access Key?\n")
                    dcm_api_secret = prompt("What is the API Secret Key?\n")
                    dcm_ssl_verify = prompt(
                        "Would you like to disable SSL verification (Y/N)?\n")
                    dcm_config_name = prompt(
                        "What would you like to call this connection (No spaces allowed in name)?\n")

                    if dcm_ssl_verify is ['N', 'n', 'no', 'NO', 'No', 'nO']:
                        dcm_ssl_verify_chk = 0
                    else:
                        dcm_ssl_verify_chk = 1

                    results = ['DCM_ENDPOINT=' + str(dcm_host), 'DCM_ACCESS_KEY=' + str(
                        dcm_api_access), 'DCM_SECRET_KEY=' + str(dcm_api_secret), 'DCM_SSL_VERIFY=' + str(dcm_ssl_verify_chk)]

                    new_file = self.mixcoatl_dir + "/" + \
                        dcm_config_name.replace(' ', '') + ".config"

                    with open(new_file, "w") as out_file:
                        out_file.write('\n'.join(results))

                    shutil.copy(new_file, self.mixcoatl_dir + "/default")

                with open(self.mixcoatl_dir + "/default") as f:
                    for line in f:
                        k, v = line.split('=', 1)
                        os.environ[k] = v.strip()
            else:
                with open(self.mixcoatl_dir + "/default") as f:
                    for line in f:
                        k, v = line.split('=', 1)
                        os.environ[k] = v.strip()

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
                    thestring = os.environ['DCM_ENDPOINT'].split('/')

                    if self.validate(thestring[-1]):
                        self.set_api_version(thestring[-1])
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

    def validate(self, date_text):
        try:
            datetime.datetime.strptime(date_text, '%Y-%m-%d')
            return date_text
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")

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
