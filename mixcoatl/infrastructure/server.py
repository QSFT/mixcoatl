from mixcoatl.resource import Resource
from mixcoatl.admin import job
from mixcoatl.utils import wait_for_job

import time
import os
import json

class Server(Resource):
    def __init__(self):
        self.path = 'infrastructure/Server'

    def get_server(self, server_id):
        p = self.path+"/"+str(server_id)
        return self.get(path=p)

    def del_server(self, server_id, reason):
        p = self.path+"/"+str(server_id)
        params = {'reason':reason}
        return self.delete(path=p, params=params)

def list_all():
    s = Server()
    servers = s.get()
    if s.last_error is None:
        return servers['servers']
    else:
        return s.last_error

def get(server_id):
    s = Server()
    server = s.get_server(server_id)
    if s.last_error is None:
        return server['servers'][0]
    else:
        return s.last_error

def terminate(server_id, reason='mixcoatl terminate server'):
    s = Server()
    s.del_server(server_id, reason)
    if s.last_error is None:
        return True
    else:
        return s.last_error

# This should be abstracted a bit more....
def launch(img_id, product, dc_id, fw_id, kp=None, wait=False):
    s = Server()
    now = int(round(time.time() * 1000))
    whoami = os.environ['USER']

    payload = {'launch':
            [{
                'product':product,
                'firewalls':[{'firewallId':fw_id}],
                'machineImage':{'machineImageId':img_id},
                'description':'mixcoatl server launch',
                'name':'mixcoatl-'+whoami+'-'+str(now),
                'dataCenter':{'dataCenterId':dc_id}
                }]}

    if kp is None:
        pass
    else:
        payload['launch'][0].update({'kp':kp})

    s.post(data=json.dumps(payload))
    if s.last_error is None:
        if wait is True:
            w = wait_for_job(s.current_job)
            if w == True:
                sid = job.get(s.current_job)['message']
                return get(sid)
            else:
                return job.get(s.current_job)
        else:
            return s.current_job
    else:
        return s.last_error
