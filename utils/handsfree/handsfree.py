#!/usr/bin/env python

import os
import time
from termcolor import colored
from fabric.api import cd, path, hide, sudo, run, execute, settings
from fabric.contrib.files import exists

class FabricSupport:

    def __init__(self, version, release_path):
        self.version = version
        self.release_path = release_path
        pass

    def fetch_vm_info(self):
        output = run("cat /etc/issue")
        parse_string = output.split()
        print "*** OS Detected:  "+parse_string[0]+" "+parse_string[1]

    def deps(self):
        print "Installing dependencies ",
        sudo('apt-get install unzip -y')
        print '\t\t\t\t\t\t\t\t[ ' + colored('OK', 'green') + ' ]'

    def fetch_release(self):
        if exists(self.release_path, use_sudo=True):
            print "DCM Directory ("+self.release_path+") detected. ",
            print '\t\t\t\t[ ' + colored('SKIPPING FETCH', 'yellow') + ' ]'
        else:
            print "Fetching release "+self.version,
            with cd("/tmp"):
                run("wget -P /tmp https://dl.dropboxusercontent.com/u/3728203/es-onpremise-chef-solo-"+self.version+".zip")
                print '\t\t\t\t\t\t\t\t[ ' + colored('OK', 'green') + ' ]'

            print "Extracting release to "+self.release_path,
            with cd("/tmp"):
                run("unzip es-onpremise-chef-solo-"+self.version+".zip -d /tmp")
                print '\t\t\t\t[ ' + colored('OK', 'green') + ' ]'

    def run_setup(self):
        print "Running setup",
        with cd(self.release_path):
            sudo("./setup.sh -s handsfree -l "+os.environ['ES_LICENSE']+" -p "+os.environ['ES_DLPASS'])
        print '\t\t\t\t\t\t\t\t[ ' + colored('OK', 'green') + ' ]'

    def install_release(self):
        print "Running install",
        with path('/opt/dmcm-base/bin:/opt/dmcm-base/embedded/bin:/opt/dmcm-base/bin:/opt/dmcm-base/embedded/bin'):
            with cd(self.release_path):
                sudo("chef-solo -j local_settings/handsfree/single_node.json -c solo.rb -o 'role[single_node]'")
        print '\t\t\t\t\t\t\t\t[ ' + colored('OK', 'green') + ' ]'

    def execute(self, task, hosts):
        with hide('output', 'running', 'warnings'), settings(warn_only=True):
            get_task = "task = self.%s" % task
            exec get_task
            execute(task, hosts=hosts)
