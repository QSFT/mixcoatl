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
configpath = os.path.expanduser('~') + '/.mixcoatl'

API_URL = 'https://slack.com/api/{api}'

def get_rc_nodes(token, count):

    '''
    This function
    :param token: slack web API token from https://api.slack.com/web
    :param count: controls the number of messages returned. A result is not
    necessarily an RC, as not all messages are RC node related.
    :return: a list of recent RC node URL
    '''

    search_str = '^Latest'

    channel_list='channels.list'
    channel_history='channels.history'

    channel_list_response = requests.get(API_URL.format(api=channel_list)+'?token='+token)

    all_channels = json.loads(channel_list_response.content)['channels']

    for channel in all_channels:
        if channel['name'] == 'dcm-latestdevinstance':
            dev_instance_channel_id = str(channel['id'])

    dev_channel_history = json.loads(requests.get(API_URL.format(api=channel_history)+
                                                  '?channel='+dev_instance_channel_id+
                                                  '&token='+token+'&count='+str(count)).content)

    # print dev_channel_history
    for message in dev_channel_history['messages']:
        if re.search(search_str, message['text']):
            env.hosts.append(message['text'].split()[4][9:].replace(">",""))

    return env.hosts


token=os.environ.get('SLACK_TOKEN')

if not token:
    print '''
    This function requires a slack token.

    Please visit: https://api.slack.com/web to get your token.

    Once you have your token, run:

    export SLACK_TOKEN='<your token>'

    '''
    sys.exit(99)


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
