from mixcoatl.resource import Resource

class Job(Resource):
    def __init__(self):
        self.path = 'admin/Job'

    def get_job(self, job_id):
        p = self.path+"/"+str(job_id)
        return self.get(path=p)

def list():
    j = Job()
    return j.get()['jobs']

def get(job_id):
    j = Job()
    job = j.get_job(job_id)
    if j.last_error is None:
        return job['jobs'][0]
    else:
        return j.last_error
