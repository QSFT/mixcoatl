from mixcoatl.admin import job
import time
import json

def wait_for_job(job_id, status='COMPLETE'):
    j = job.get(job_id)
    initial_status = j['status']
    if initial_status == 'ERROR':
        return False
    while job.get(job_id)['status'] != status:
        time.sleep(5)
        j = job.get(job_id)
        if j['status'] == 'ERROR':
            return False
        else:
            continue

    return True

def uncamel(str):
    import re
    s = lambda str: re.sub('(((?<=[a-z])[A-Z])|([A-Z](?![A-Z]|$)))', '_\\1', str).lower().strip('_')
    return s(str)

def uncamel_keys(d1):
    d2 = dict()
    if not isinstance(d1, dict):
        return d1
    for k,v in d1.iteritems():
        new_key = uncamel(k)
        if isinstance(v, dict):
            d2[new_key] = uncamel_keys(v)
        elif isinstance(v, list):
            d2[new_key] = [uncamel_keys(item) for item in v]
        else:
            d2[new_key] = v
    return d2
