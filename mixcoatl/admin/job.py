from mixcoatl.resource import Resource
from mixcoatl.decorators.lazy import lazy_property
from mixcoatl.utils import camelize

import time

class Job(Resource):
    path = 'admin/Job'
    collection_name = 'jobs'
    primary_key = 'job_id'

    def __init__(self, job_id = None, **kwargs):
        """
        Initialize a new Job object from the provided job_id
        """
        Resource.__init__(self)
        self.__job_id = job_id

    @property
    def job_id(self):
        """Return the job's ID. *Immutable*"""

        return self.__job_id

    @lazy_property
    def status(self):
        """Return the job's status. *Immutable*"""

        return self.__status

    @lazy_property
    def description(self):
        """Return the job's description. *Immutable*"""

        return self.__description

    @lazy_property
    def message(self):
        """Return the job's message. *Immutable*"""

        return self.__message

    @lazy_property
    def start_date(self):
        """Return the job's start date. *Immutable*"""

        return self.__start_date

    @lazy_property
    def end_date(self):
        """Return the job's stop date. *Immutable*"""
        
        return self.__end_date

    @classmethod
    def all(cls):
        """Get all jobs

        :returns: list -- a list of :class:`Job`'s
        """
        r = Resource(cls.path)
        x = r.get()
        if r.last_error is None:
            return [cls(i[camelize(cls.primary_key)]) for i in x[cls.collection_name]]
        else:
            return r.last_error

    @classmethod
    def wait_for(cls, job_id, status='COMPLETE', callback = None):
        """Blocks execution until :attr:`job_id` returns :attr:`status`

        :param job_id: The ID of the job to wait on
        :type job_id: int.
        :param status: The status to expect before continuing
        :type status: str.
        :param callback: Optional callback to be called with the final ``Job`` when ``status`` is reached
        :type callback: func.
        """
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
