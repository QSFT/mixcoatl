#!/usr/bin/env python

import os
import subprocess
import json
import string
import random
from subprocess import call
from termcolor import colored
from fabric.api import cd, path, hide, sudo, run, execute, settings, get, put
from fabric.contrib.files import exists


class FabricSupport:
    MASTER_API_KEY = None
    MASTER_SECRET_KEY = None

    def __init__(self, hosts, version, console_host, license_key, download_pass, release_path, email, first_name, last_name, company_name, setup_dir):

        self.hosts = hosts
        self.version = version
        self.console_host = console_host
        self.license_key = license_key
        self.download_pass = download_pass
        self.release_path = release_path
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.company_name = company_name
        self.sbin_dir = '/services/backend/sbin'
        self.setup_dir = setup_dir
        self.cloud_descriptors_dir = '{}/clouds/descriptors'.format(setup_dir)
        self.cloud_credentials_dir = '{}/clouds/credentials'.format(setup_dir)
        self.user_dir = '{}/users'.format(setup_dir)
        self.groups = '{}/groups'.format(setup_dir)
        self.roles_dir = '{}/roles'.format(setup_dir)
        self.acl_dir = '{}/roles/acl'.format(setup_dir)
        self.billing = '{}/billing'.format(setup_dir)
        pass

    def random_pass(self):
        rnd = random.SystemRandom()
        return ''.join(rnd.choice(string.ascii_letters + string.digits) for i in range(11))

    def fetch_vm_info(self):
        output = run("cat /etc/issue")
        parse_string = output.split()
        print "*** OS Detected:  " + parse_string[0] + " " + parse_string[1]

    def deps(self):
        print "{:80}".format("Installing dependencies "),
        sudo('apt-get install unzip -y')
        print "{:}".format('[ ' + colored('OK', 'green') + ' ]')

    def fetch_release(self):
        if exists(self.release_path, use_sudo=True):
            print "{:80} {:}".format("DCM Directory (" + self.release_path + ") detected. ", '[ ' + colored('SKIPPING FETCH', 'yellow') + ' ]')
        else:
            print "{:80}".format("Fetching release " + self.version),
            # To do: fix this redundancy
            with cd("/tmp"):
                run("curl -o /tmp/es-onpremise-chef-solo-{}.tar.gz https://onpremise:{}@download.ext.enstratius.com/{}/es-onpremise-chef-solo-{}.tar.gz".format(self.version,self.download_pass,self.version,self.version))
                print "{:}".format('[ ' + colored('OK', 'green') + ' ]')

                print "{:80}".format("Extracting release to " + self.release_path),
                run("tar -zxf es-onpremise-chef-solo-" + self.version + ".tar.gz -C /tmp")
                print "{:}".format('[ ' + colored('OK', 'green') + ' ]')

    def run_setup(self):
        setup_file = self.release_path + \
            "/local_settings/handsfree/single_node.json"
        if exists(setup_file, use_sudo=True):
            print "{:80} {:}".format("Setup File detected. ", '[ ' + colored('SKIPPING SETUP', 'yellow') + ' ]')
        else:
            print "{:80}".format("Running DCM setup"),
            with cd(self.release_path):
                sudo("./setup.sh -s handsfree -l " +
                     self.license_key + " -p " + self.download_pass + " -c " + self.console_host)
            print "{:}".format('[ ' + colored('OK', 'green') + ' ]')

    def install_release(self):
        flags_file = "/tmp/feature-flags-rules.json"
        if exists(flags_file, use_sudo=True):
            print "{:80} {:}".format("Installation already completed. ", '[ ' + colored('SKIPPING DCM INSTALL', 'yellow') + ' ]')
        else:
            print "{:80}".format("Running DCM install"),
            with path('/opt/dmcm-base/bin:/opt/dmcm-base/embedded/bin:/opt/dmcm-base/bin:/opt/dmcm-base/embedded/bin'):
                with cd(self.release_path):
                    sudo("chef-solo -j local_settings/handsfree/single_node.json -c solo.rb -o 'role[single_node]'")
            print "{:}".format('[ ' + colored('OK', 'green') + ' ]')

    def create_master_api_key(self):
        master_apikey = "/tmp/master-apikey.json"
        if exists(master_apikey, use_sudo=True):
            print "{:80} {:}".format("Master Key file exists. ", '[ ' + colored('SKIPPING KEYGEN', 'yellow') + ' ]')
        else:
            print "{:80}".format("Generating Master API Key"),
            sudo('/services/backend/sbin/create-master-apikey.sh -o /tmp/master-apikey.json')
            print "{:}".format('[ ' + colored('OK', 'green') + ' ]')

    def create_initial_user(self):
        '''
        This method creates the initial user account in DCM.

        It completes the "registration" step for a newly installed environment.
        '''

        print "{:80}".format("Registering Initial User Account"),
        with open('{}/initial-account.json'.format(self.user_dir), 'r') as initial_account:

            put(initial_account, '/tmp/initial-account.json')

        cmd = '{}/create-initial-user.py --context /tmp/master-apikey.json /tmp/initial-account.json'.format(self.sbin_dir)
        sudo(cmd)
        print "{:}".format('[ ' + colored('OK', 'green') + ' ]')

    def create_initial_cloud_accounts(self):
        '''
        Adds the initial cloud accounts credential

        Depends on the presence of an initial set of cloud credentials.
        '''

        put('{}/clouds/initial_cloud.json'.format(self.setup_dir), '/tmp/initial_cloud.json')
        print "{:80}".format("Creating Initial Cloud Account(s)"),
        cmd = '{}/create-initial-cloudaccount.py {} /tmp/initial_cloud.json --context /tmp/master-apikey.json'.format(self.sbin_dir, self.email)
        sudo(cmd)
        print "{:}".format('[ ' + colored('OK', 'green') + ' ]')

    def add_private_clouds(self):

        print "{:80}".format("Adding Private Cloud Definitions"),
        for private_cloud in os.listdir(self.cloud_descriptors_dir):

            put(self.cloud_descriptors_dir+'/'+private_cloud, '/tmp/private-cloud.json')
            cmd = 'bash {}/add-cloud.sh /tmp/private-cloud.json'.format(self.sbin_dir)

            sudo(cmd)

        print "{:}".format('[ ' + colored('OK', 'green') + ' ]')

    def create_user_api_key(self):
        '''
        Creates a user API key and stores it locally in a file called userkeys.json
        '''

        print "{:80}".format("Create User API Key"),

        cmd = '{}/create-initial-apikeys.py ' \
            '--genUserKey ' \
            '--initialUser /tmp/initial-account.json ' \
            '--initialAccount /tmp/initial_cloud.json ' \
            '--output /tmp/userkeys.json ' \
            '--context /tmp/master-apikey.json'.format(self.sbin_dir)

        sudo(cmd)
        print "{:}".format('[ ' + colored('OK', 'green') + ' ]')

        get('/tmp/userkeys.json', '{}/userkeys.json'.format(self.setup_dir))

    def install_admin(self):
        '''
        Adds the user in initial-account.json as an installation admin.
        This means the user will have access to the DCM operator console.
        '''

        print "{:80}".format("Setting Install Admin"),

        cmd = '{}/manage-install-admins.sh add -e {}'.format(self.sbin_dir, self.email)

        sudo(cmd)
        print "{:}".format('[ ' + colored('OK', 'green') + ' ]')

    def set_user_credentials(self):
        '''
        Creates a local config file.
        '''

        print "{:80}".format("Adding Additional Cloud Credentials"),

        with open('{}/userkeys.json'.format(self.setup_dir), 'r') as f:
            contents=json.loads(f.read())

        secret_key=contents['secretKey']
        access_key=contents['accessKey']

        with open('{}/config.txt'.format(self.setup_dir), 'w') as mixcoatl_config:
            mixcoatl_config.write("export DCM_ACCESS_KEY={}\n".format(access_key))
            mixcoatl_config.write("export DCM_SECRET_KEY={}\n".format(secret_key))
            mixcoatl_config.write("export DCM_ENDPOINT=http://{}:15000/api/enstratus/2015-01-28\n".format(self.hosts))
            mixcoatl_config.write("export DCM_SSL_VERIFY=0\n")

        os.environ["DCM_ACCESS_KEY"] = access_key
        os.environ["DCM_SECRET_KEY"] = secret_key
        os.environ["DCM_ENDPOINT"] = 'http://{}:15000/api/enstratus/2015-01-28'.format(self.hosts)
        os.environ["DCM_SSL_VERIFY"] = '0'

        for credentials_file in os.listdir(self.cloud_credentials_dir):
            cmd = "dcm-post admin/Account --json {}".format(self.cloud_credentials_dir+'/'+credentials_file)
            call(cmd, shell=True)

        print "{:}".format('[ ' + colored('OK', 'green') + ' ]')

    def add_roles(self):
        '''
        Creates roles and sets ACL for those roles.
        Looks in setup_dir/roles/roles and setup_dir/roles/acl

        Uses the mixcoatl command line helpers:
        1. dcm-create-role
        2. dcm-set-acl
        :return:
        '''

        print "{:80}".format("Adding Roles")
        with open('{}/userkeys.json'.format(self.setup_dir), 'r') as f:
            contents=json.loads(f.read())

        secret_key=contents['secretKey']
        access_key=contents['accessKey']

        os.environ["DCM_ACCESS_KEY"] = access_key
        os.environ["DCM_SECRET_KEY"] = secret_key
        os.environ["DCM_ENDPOINT"] = 'http://{}:15000/api/enstratus/2015-01-28'.format(self.hosts)
        os.environ["DCM_SSL_VERIFY"] = '0'

        for role_file in os.listdir(self.roles_dir):
            if os.path.isfile(self.roles_dir+'/'+role_file):
                print role_file
                cmd = "dcm-post admin/Role --json {}".format(self.roles_dir+'/'+role_file)
                call(cmd, shell=True)

        # result = subprocess.check_output(['dcm-list-roles', '--json'])

        # role_json = json.loads(result)

        # for r in role_json:
        #     print r['name'], r['role_id']


    def install_parachute(self):
        install_file = "/opt/parachute/bin/parachute"
        if exists(install_file, use_sudo=True):
            print "{:80} {:}".format("Parachute already installed. ", '[ ' + colored('SKIPPING PARACHUTE INSTALL', 'yellow') + ' ]')
        else:
            print "{:80}".format("Installing Parachute"),
            with cd("/tmp"):
                sudo(
                    "bash -s - -v k.36 < <( curl http://download.parachuteapp.net/install.sh )")
            print "{:}".format('[ ' + colored('OK', 'green') + ' ]')

    def execute(self, task):
        with hide('output', 'running', 'warnings'), settings(warn_only=True):
            get_task = "task = self.%s" % task
            exec get_task
            execute(task, hosts=self.hosts)
