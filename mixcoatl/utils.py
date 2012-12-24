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
