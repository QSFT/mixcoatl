#!/usr/bin/env python

import os
import subprocess
import json
import string
import random
import glob
from subprocess import call, check_output, CalledProcessError
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
        self.groups_dir = '{}/groups'.format(setup_dir)
        self.roles_dir = '{}/roles'.format(setup_dir)
        self.acl_dir = '{}/roles/acl'.format(setup_dir)
        self.billing_dir = '{}/billing'.format(setup_dir)
        self.auth_dir = '{}/auth'.format(setup_dir)
        self.marketplace_dir = '{}/marketplace'.format(setup_dir)
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
        #for private_cloud in os.listdir(self.cloud_descriptors_dir):
        for private_cloud in  glob.glob(self.cloud_descriptors_dir+'/*.json'):

            #put(self.cloud_descriptors_dir+'/'+private_cloud, '/tmp/private-cloud.json')
            put(private_cloud, '/tmp/private-cloud.json')
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
            call(cmd, shell=True, stdout=subprocess.PIPE)

        print "{:}".format('[ ' + colored('OK', 'green') + ' ]')

    def add_roles(self):
        '''
        Creates roles and sets ACL for those roles.
        Looks in setup_dir/roles/roles and setup_dir/roles/acl

        Uses the mixcoatl REST utilities:
        1. dcm-post (for adding the roles)
        2. dcm-set-acl (for setting the acl)

        This method relies on a "role" parameter set in the role_acl like this:
        {
          "role" : "Developer",
          "grant": [

        This allows for the programmatic setting of ACL for each role.
        :return:
        '''

        print "{:80}".format("Adding Roles"),
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
                cmd = "dcm-post admin/Role --json {}".format(self.roles_dir+'/'+role_file)
                call(cmd, shell=True, stdout=subprocess.PIPE)
        print "{:}".format('[ ' + colored('OK', 'green') + ' ]')

        result = subprocess.check_output(['dcm-list-roles', '--json'])

        role_json = json.loads(result)

        role_dict = dict((r['name'], r['role_id']) for r in role_json)

        print "{:80}".format("Setting ACL"),
        for acl_file in os.listdir(self.acl_dir):
            if os.path.isfile(self.acl_dir + '/' + acl_file):
                with open(self.acl_dir + '/' + acl_file, 'r') as f:
                    acl_json = json.loads(f.read())
                    role_name = acl_json['role']

                    cmd = "dcm-put admin/Role/{} --json {}".format(role_dict[role_name], self.acl_dir + '/' + acl_file)
                    call(cmd, shell=True, stdout=subprocess.PIPE)
        print "{:}".format('[ ' + colored('OK', 'green') + ' ]')

    def add_groups(self):
        '''
        Creates groups
        Looks in setup_dir/groups

        Uses the mixcoatl REST utilities:
        1. dcm-post (for adding the groups)
        2. dcm-put (for associating the account-role)

        :return: ID of the created group
        '''

        print "{:80}".format("Adding Groups"),
        with open('{}/userkeys.json'.format(self.setup_dir), 'r') as f:
            contents=json.loads(f.read())

        secret_key=contents['secretKey']
        access_key=contents['accessKey']

        os.environ["DCM_ACCESS_KEY"] = access_key
        os.environ["DCM_SECRET_KEY"] = secret_key
        os.environ["DCM_ENDPOINT"] = 'http://{}:15000/api/enstratus/2015-01-28'.format(self.hosts)
        os.environ["DCM_SSL_VERIFY"] = '0'

        for group_file in os.listdir(self.groups_dir):
            if os.path.isfile(self.groups_dir+'/'+group_file):
                cmd = "dcm-post admin/Group --json {}".format(self.groups_dir+'/'+group_file)
                call(cmd, shell=True, stdout=subprocess.PIPE)
        print "{:}".format('[ ' + colored('OK', 'green') + ' ]')

        role_result = subprocess.check_output(['dcm-list-roles', '--json'])
        role_json = json.loads(role_result)
        role_dict = dict((r['name'], r['role_id']) for r in role_json)

        group_result = subprocess.check_output(['dcm-list-groups', '--json'])
        group_json = json.loads(group_result)
        group_dict = dict((r['name'], r['group_id']) for r in group_json)

        account_result = subprocess.check_output(['dcm-list-accounts', '--json'])
        account_json = json.loads(account_result)
        account_list = [a['account_id'] for a in account_json]

        billing_code_result = subprocess.check_output(['dcm-list-billing-codes', '--json'])
        billing_code_json = json.loads(billing_code_result)

        billing_code_list = [b['billing_code_id'] for b in billing_code_json]

        #print "\n"
        for group_name, group_id in group_dict.iteritems():
            role_assignments = []
            billing_assignments = []
            if group_name != 'Administrators':
                try:
                    for a in account_list:
                        role_assignment = {"accountId": a, "roleId": role_dict[group_name[:-1]]}
                        role_assignments.append(role_assignment)
                        billing_assignment = {"accountId": a, "budgetCodes": billing_code_list}
                        billing_assignments.append(billing_assignment)
                except KeyError:
                    pass

                payload = {"addRoleAssignments": {"group": {"roleAssignments": role_assignments, "groupAccountBudgetCodes": billing_assignments}}}
                with open('/tmp/role_assignment.json','w') as ra:
                    ra.write(json.dumps(payload))
                cmd = "dcm-put admin/Group/{} --json {}".format(group_id, '/tmp/role_assignment.json')
                call(cmd, shell=True, stdout=subprocess.PIPE)

        # for account_id in account_list:
        #     a = account_id
        #     for role_name, role_id in role_dict.iteritems():
        #         rn, ri = role_name, role_id
        #
        #         role_assignment = {"accountId": a, "roleId": ri}
        #
        #     role_assignments.append(role_assignment)
        #
        #     print "\n"
        #     print role_assignments
        #     print "\n"
        # print "{:80}".format("Setting ACL"),
        # for acl_file in os.listdir(self.acl_dir):
        #     if os.path.isfile(self.acl_dir + '/' + acl_file):
        #         with open(self.acl_dir + '/' + acl_file, 'r') as f:
        #             acl_json = json.loads(f.read())
        #             role_name = acl_json['role']
        #
        #             cmd = "dcm-put admin/Role/{} --json {}".format(role_dict[role_name], self.acl_dir + '/' + acl_file)
        #             call(cmd, shell=True, stdout=subprocess.PIPE)
        # print "{:}".format('[ ' + colored('OK', 'green') + ' ]')

    def add_billing_codes(self):
        '''
        Creates billing codes
        Looks in setup_dir/billing

        Uses the mixcoatl REST utilities:
        1. dcm-post (for adding the billing codes)

        :return: DCM ID for the created billing code.
        '''

        print "{:80}".format("Adding Billing Codes"),
        with open('{}/userkeys.json'.format(self.setup_dir), 'r') as f:
            contents=json.loads(f.read())

        secret_key=contents['secretKey']
        access_key=contents['accessKey']

        os.environ["DCM_ACCESS_KEY"] = access_key
        os.environ["DCM_SECRET_KEY"] = secret_key
        os.environ["DCM_ENDPOINT"] = 'http://{}:15000/api/enstratus/2015-01-28'.format(self.hosts)
        os.environ["DCM_SSL_VERIFY"] = '0'

        for billing_file in os.listdir(self.billing_dir):
            if os.path.isfile(self.billing_dir+'/'+billing_file):
                cmd = "dcm-post admin/BillingCode --json {}".format(self.billing_dir+'/'+billing_file)
                call(cmd, shell=True, stdout=subprocess.PIPE)
        print "{:}".format('[ ' + colored('OK', 'green') + ' ]')


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


    def configure_auth(self):
        auth_config_file = '{}/auth_config.json'.format(self.auth_dir)
        if os.path.exists(auth_config_file):
            with open(auth_config_file, 'r') as f:
                contents=json.loads(f.read())

            method = contents['authentication_method']
            endpoint = contents['sso_endpoint']
            key = contents['sso_key']
            saml_issuer = contents['saml_issuer_entity_id']

            print "{:80}".format('Configure ' + method + ' Authentication'),
        
            policy_id = sudo("/services/backend/sbin/singlenode/mysql-root-shell.sh provisioning -N -B -e 'select default_security_policy_id from customer_configuration where customer_id = 200;'")
        
            sql = "update security_policy set authentication_method = \"{}\"".format(method)
            if method == 'SAML':
                sql += ",  sso_key = \"{}\", sso_endpoint = \"{}\"".format(key, endpoint)
                if saml_issuer != None:
                    sql += ", saml_issuer_entity_id = {}".format(saml_issuer)
            sql += " where security_policy_id = {};".format(policy_id)

            result = sudo("/services/backend/sbin/singlenode/mysql-root-shell.sh provisioning -e '{}'".format(sql))

            print "{:}".format('[ ' + colored('OK', 'green') + ' ]')
        else:
            print "{:80} {:}".format("No auth configuration found", '[ ' + colored('SKIPPING AUTH CONFIG', 'yellow') + ' ]')


    def configure_dirsync(self):
        dirsync_file = '{}/auth/dirsync.cfg'.format(self.setup_dir)
        if os.path.exists(dirsync_file):
            print "{:80}".format("Configure dirsync"),

            put(dirsync_file, '/tmp/dirsync.cfg')

            cmd = "/services/backend/sbin/dirsync-tool.sh -f /tmp/dirsync.cfg"
            result = sudo(cmd)

            cmd = "/services/backend/sbin/dirsync-tool.sh --run"
            result = sudo(cmd)

            print "{:}".format('[ ' + colored('OK', 'green') + ' ]')
        else:
            print "{:80} {:}".format("No dirsync configuration found", '[ ' + colored('SKIPPING DIRSYNC', 'yellow') + ' ]')



    def add_private_clouds_pricing(self):
        print "{:80}".format("Adding Private Cloud Pricing Definitions"),
        for private_cloud_pricing in glob.glob(self.cloud_descriptors_dir+'/*pricing.sql'):

            put(private_cloud_pricing, '/tmp/private-cloud-pricing.sql')

            result = sudo("/services/backend/sbin/singlenode/mysql-root-shell.sh provisioning < /tmp/private-cloud-pricing.sql")

        print "{:}".format('[ ' + colored('OK', 'green') + ' ]')


    def setup_marketplace(self):
        marketplace_cfg_file = '{}/marketplace_config.json'.format(self.marketplace_dir)
        if os.path.exists(marketplace_cfg_file):
            print "{:80}".format("Setup Marketplace")

            with open(marketplace_cfg_file, 'r') as f:
                contents=json.loads(f.read())

            github_creds = contents['github_credentials']

            pwd = os.getcwd()

            # Similar to mixcoatl, install the marketplace bits/git contents locally via subprocess calls

            try:
                # TODO: Need a better way to do this, so I don't have to embed personal credentials
                # - Is there an artifactory download?
                result = check_output("git clone https://{}@github.com/enStratus/marketplace-content.git".format(github_creds), shell=True)
        
                # Using virtualenv complicates things here since all the commands need to run in the same shell
                # run and sudo create a new shell for each command
                # NOTE: mixing subprocess commands like 'call' and fabric commands will break things if we actually
                # perform multi-node installs

                #result = run("virtualenv --no-site-packages venv")
                #print "RC04: {}".format(result)
                #result = run("source venv/bin/activate")
                #print "RC05: {}".format(result)
        
                result = check_output("sudo pip install -r {}/marketplace-content/requirements.txt".format(pwd), shell=True)
        
                #master api key and user api should already exist, so just reuse
        
                with open('{}/userkeys.json'.format(self.setup_dir), 'r') as f:
                    contents=json.loads(f.read())

                secret_key=contents['secretKey']
                access_key=contents['accessKey']
                #api_endpoint=contents['apiEndpoint']

                os.environ["DCM_ACCESS_KEY"] = access_key
                os.environ["DCM_SECRET_KEY"] = secret_key
                os.environ["DCM_ENDPOINT"] = 'http://{}:15000/api/enstratus/2015-01-28'.format(self.hosts)
                os.environ["DCM_SSL_VERIFY"] = '0'

                # This was just to test that mixcoatl calls work
                result = check_output("dcm-get admin/Job", shell=True)
                #print "RC06a: {}".format(result)

                result = check_output("{}/marketplace-content/bin/add-catalog --resultpath catalogid 200".format(pwd), shell=True)
        
                result = check_output("{}/marketplace-content/bin/mark-catalog-public `cat catalogid` --callback wss://{}/agentManager".format(pwd, self.hosts), shell=True)
        
                result = check_output("{}/marketplace-content/bin/add-content.sh `cat catalogid`".format(pwd), shell=True)
     
            except CalledProcessError as ex:
                print "{:}".format('[ ' + colored('ERROR Encountered!', 'yellow') + ' ]')
                print "CMD: {}".format(ex.cmd)
                print "Output: {}".format(ex.output)
                
                return -1
 
            print "{:}".format('[ ' + colored('OK', 'green') + ' ]')
        else:
            print "{:80} {:}".format("No github credentials found", '[ ' + colored('SKIPPING MARKETPLACE SETUP', 'yellow') + ' ]')


    def execute(self, task):
        with hide('output', 'running', 'warnings'), settings(warn_only=True):
            get_task = "task = self.%s" % task
            exec get_task
            execute(task, hosts=self.hosts)
