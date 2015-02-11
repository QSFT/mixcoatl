#!/usr/bin/env python

import os
import time
import json
import string
import random
from termcolor import colored
from fabric.api import cd, path, hide, sudo, run, execute, settings
from fabric.contrib.files import exists


class FabricSupport:

    def __init__(self, hosts, version, console_host, license_key, download_pass, release_path, email, first_name, last_name, company_name):
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
        pass

    def random_pass(self):
        rnd = random.SystemRandom()
        return ''.join(rnd.choice(string.ascii_letters + string.digits) for i in range(11))

    def fetch_vm_info(self):
        output = run("cat /etc/issue")
        parse_string = output.split()
        print "*** OS Detected:  " + parse_string[0] + " " + parse_string[1]

    def deps(self):
        print "Installing dependencies ",
        sudo('apt-get install unzip -y')
        print '\t\t\t\t\t\t\t\t[ ' + colored('OK', 'green') + ' ]'

    def fetch_release(self):
        if exists(self.release_path, use_sudo=True):
            print "DCM Directory (" + self.release_path + ") detected. ",
            print '\t\t\t\t[ ' + colored('SKIPPING FETCH', 'yellow') + ' ]'
        else:
            print "Fetching release " + self.version,
            with cd("/tmp"):
                run("wget -P /tmp https://dl.dropboxusercontent.com/u/3728203/es-onpremise-chef-solo-" +
                    self.version + ".zip")
                print '\t\t\t\t\t\t\t\t[ ' + colored('OK', 'green') + ' ]'

                print "Extracting release to " + self.release_path,
                run("unzip es-onpremise-chef-solo-" +
                    self.version + ".zip -d /tmp")
                print '\t\t\t\t[ ' + colored('OK', 'green') + ' ]'

    def run_setup(self):
        setup_file = self.release_path + \
            "/local_settings/handsfree/single_node.json"
        if exists(setup_file, use_sudo=True):
            print "Setup File detected. ",
            print '\t\t\t\t\t\t\t\t\t[ ' + colored('SKIPPING SETUP', 'yellow') + ' ]'
        else:
            print "Running DCM setup",
            with cd(self.release_path):
                sudo("./setup.sh -s handsfree -l " +
                     self.license_key + " -p " + self.download_pass + " -c " + self.console_host)
            print '\t\t\t\t\t\t\t\t\t[ ' + colored('OK', 'green') + ' ]'

    def install_release(self):
        flags_file = "/tmp/feature-flags-rules.json"
        if exists(flags_file, use_sudo=True):
            print "Installation already completed. ",
            print '\t\t\t\t\t\t\t[ ' + colored('SKIPPING DCM INSTALL', 'yellow') + ' ]'
        else:
            print "Running DCM install",
            with path('/opt/dmcm-base/bin:/opt/dmcm-base/embedded/bin:/opt/dmcm-base/bin:/opt/dmcm-base/embedded/bin'):
                with cd(self.release_path):
                    sudo(
                        "chef-solo -j local_settings/handsfree/single_node.json -c solo.rb -o 'role[single_node]'")
            print '\t\t\t\t\t\t\t\t\t[ ' + colored('OK', 'green') + ' ]'

    def create_master_api_key(self):
        master_apikey = "/tmp/master-apikey.json"
        if exists(master_apikey, use_sudo=True):
            print "Master Key file exists. ",
            print '\t\t\t\t\t\t\t\t[ ' + colored('SKIPPING KEYGEN', 'yellow') + ' ]'
        else:
            print "Generating Master Keys",
            sudo(
                '/services/backend/sbin/create-master-apikey.sh -o /tmp/master-apikey.json')
            print '\t\t\t\t\t\t\t\t\t[ ' + colored('OK', 'green') + ' ]'

    def create_initial_user(self):
        initial_user = "/tmp/initial_user.json"
        if exists(initial_user, use_sudo=True):
            print "Initial User file exists. ",
            print '\t\t\t\t\t\t\t\t[ ' + colored('SKIPPING USER CREATION', 'yellow') + ' ]'
        else:
            print "Creating Initial User",
            with open("users/initial_user.json", "r") as myfile:
                data = json.loads(myfile.read())

            data['firstName'] = self.first_name
            data['lastName'] = self.last_name
            data['email'] = self.email
            data['businessName'] = self.company_name
            data['password'] = self.random_pass()
            data['windowsPassword'] = self.random_pass()

            with open(os.path.expanduser('~') + '/.ssh/id_rsa.pub', "r") as sshkey:
                key = sshkey.read().rstrip('\n')

            data['sshPublicKey'] = key

            sudo("echo "+ json.dumps(data) + " > /tmp/initial_user.json")
            sudo('/services/backend/sbin/create-initial-user.py --context /tmp/master-apikey.json /tmp/initial_user.json')
            print '\t\t\t\t\t\t\t\t\t[ ' + colored('OK', 'green') + ' ]'

    def install_parachute(self):
        install_file = "/opt/parachute/app/cfg/config.ini"
        if exists(install_file, use_sudo=True):
            print "Parachute already installed. ",
            print '\t\t\t\t\t\t\t\t[ ' + colored('SKIPPING PARACHUTE INSTALL', 'yellow') + ' ]'
        else:
            print "Installing Parachute",
            with cd("/tmp"):
                sudo(
                    "curl http://download.parachuteapp.net/install.sh | sudo bash -s - -v k30-rc1")
            print '\t\t\t\t\t\t\t\t\t[ ' + colored('OK', 'green') + ' ]'

    def execute(self, task):
        with hide('output', 'running', 'warnings'), settings(warn_only=True):
            get_task = "task = self.%s" % task
            exec get_task
            execute(task, hosts=self.hosts)
