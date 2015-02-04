#!/usr/bin/env python
# fab -P gen_configs

import os
import re
import sys
import json
from fabric.api import env, hide, run, settings

env.hosts = []
env.skip_bad_hosts = True
env.user = 'root'
env.key_filename = os.path.expanduser('~') + '/.ssh/id_rsa'
envsfile = os.path.expanduser('~') + '/.mixcoatl/envs'
configpath = os.path.expanduser('~') + '/.mixcoatl'

if os.path.exists(envsfile):
    with open(envsfile, "r") as myfile:
        data = myfile.read()
        myString_list = [item for item in data.split(" ")]
        for item in myString_list:
            try:
                env.hosts.append(
                    re.search("(?P<url>https?://[^\s]+)", item).group("url")[8:])
            except:
                pass
else:
    print "No envs file"
    sys.exit(1)


def gen_configs():
    with hide('output', 'running', 'warnings'), settings(warn_only=True):
        version = run(
            "cat /vagrant/local_settings/current/single_node.json | grep visible_version | awk -F '[:]' '{ print $2; }' | sed -e 's/^\"//' -e 's/\",$//'")
        output = run('cat /vagrant/tmp/qa-apikeys.json')
        for i in json.loads(output):
            if i['customerManagementKey'] is True and i['name'] == 'AWSCustomerKey':
                the_file = configpath + '/' + version + '-customerkey.config'
                if os.path.exists(the_file):
                    os.remove(the_file)

                with open(the_file, "a+") as f:
                    print 'Wrote ' + version + "-customerkey"
                    f.write(
                        'DCM_ENDPOINT=https://' + env.host + '/api/enstratus/2014-07-30\n')
                    f.write('DCM_SSL_VERIFY=0\n')
                    f.write('DCM_ACCESS_KEY=' + i['accessKey'] + '\n')
                    f.write('DCM_SECRET_KEY=' + i['secretKey'] + '\n')
            elif i['customerManagementKey'] is False and i['name'] == 'AWSUserKey':
                the_file = configpath + '/' + version + '-userkey.config'
                if os.path.exists(the_file):
                    os.remove(the_file)

                with open(the_file, "a+") as f:
                    print 'Wrote ' + version + "-userkey"
                    f.write(
                        'DCM_ENDPOINT=https://' + env.host + '/api/enstratus/2014-07-30\n')
                    f.write('DCM_SSL_VERIFY=0\n')
                    f.write('DCM_ACCESS_KEY=' + i['accessKey'] + '\n')
                    f.write('DCM_SECRET_KEY=' + i['secretKey'] + '\n')
