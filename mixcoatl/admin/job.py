from mixcoatl.resource import Resource
from mixcoatl.decorators.lazy import lazy_property
from mixcoatl.utils import camelize

import time

class Job(Resource):
    path = 'admin/Job'
    collection_name = 'jobs'
    primary_key = 'job_id'

    def __init__(self, job_id = None, **kwargs):
        Resource.__init__(self)
        self.__job_id = job_id

    @property
    def job_id(self):
        return self.__job_id

    @lazy_property
    def status(self):
        return self.__status

    @lazy_property
    def description(self):
        return self.__description

    @lazy_property
    def message(self):
        return self.__message

    @lazy_property
    def start_date(self):
        return self.__start_date

    @lazy_property
    def end_date(self):
        return self.__end_date


    def get_job(self, job_id):
        p = self.path+"/"+str(job_id)
        return self.get(path=p)


    @classmethod
    def all(cls):
        r = Resource(cls.path)
        x = r.get()
        if r.last_error is None:
            return [cls(i[camelize(cls.primary_key)]) for i in x[cls.collection_name]]
        else:
            return r.last_error

    @classmethod
    def wait_for(cls, job_id, status='COMPLETE', callback = None):
        j = Job(job_id)
        initial_status = j.status
        if initial_status == 'ERROR':
            return False
        while j.status != status:
            time.sleep(5)
            j.load()
            if j.status == 'ERROR':
                if callback is not None:
                    callback(j)
            else:
                continue
        if callback is not None:
            callback(j)
        else:
            return True
