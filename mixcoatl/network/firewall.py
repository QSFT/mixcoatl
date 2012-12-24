from mixcoatl.resource import Resource
from mixcoatl.admin import job
from mixcoatl.utils import wait_for_job

import time
import os
import json

class Firewall(Resource):
    def __init__(self):
        self.path = 'network/Firewall'

    def get_firewall(self, firewall_id):
        p = self.path+"/"+str(firewall_id)
        return self.get(path=p)

    def del_firewall(self, firewall_id, reason):
        p = self.path+"/"+str(firewall_id)
        params = {'reason':reason}
        return self.delete(path=p, params=params)

def list_all(region_id):
    f = Firewall()
    firewalls = f.get(params={'regionId':region_id})
    if f.last_error is None:
        return firewalls['firewalls']
    else:
        return f.last_error

def show(firewall_id):
    f = Firewall()
    firewall = f.get_firewall(firewall_id)
    if f.last_error is None:
        return firewall['firewalls'][0]
    else:
        return f.last_error

def create(region_id, budget_id, wait=False):
    f = Firewall()
    now = int(round(time.time() * 1000))
    whoami = os.environ['USER']

    payload = {'addFirewall':[{
        'region':{'regionId':region_id},
        'budget':budget_id,
        'description':'mixcoatl-generated firewall',
        'name':'mixcoatl-'+whoami+'-'+str(now)}]}

    f.post(data=json.dumps(payload))
    if f.last_error is None:
        if wait is True:
            w = wait_for_job(f.current_job)
            if w == True:
                fwid = job.get(f.current_job)['message']
                return show(fwid)
            else:
                return job.get(f.current_job)
        else:
            return f.current_job
    else:
        return f.last_error
