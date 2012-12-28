from mixcoatl.resource import Resource

class Job(Resource):
    path = 'admin/Job'
    collection_name = 'jobs'
    def __init__(self):
        Resource.__init__(self)

    def get_job(self, job_id):
        p = self.path+"/"+str(job_id)
        return self.get(path=p)

    @classmethod
    def all(cls):
        r = Resource(cls.path)
        jobs = r.get()[cls.collection_name]
        if r.last_error is None:
            return jobs
        else:
            return r.last_error

def get(job_id):
    j = Job()
    job = j.get_job(job_id)
    if j.last_error is None:
        return job['jobs'][0]
    else:
        return j.last_error
