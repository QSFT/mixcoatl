#!/usr/bin/env python

import os
from fabric.api import env, run, execute

env.skip_bad_hosts = True
env.user = 'root'
env.key_filename = os.path.expanduser('~') + '/.ssh/id_rsa'


class FabricSupport:

    def __init__(self):
        pass

    def hostname(self):
        run("hostname")

    def df(self):
        run("df -h")

    def execute(self, task, hosts):
        get_task = "task = self.%s" % task
        exec get_task
        execute(task, hosts=hosts)
