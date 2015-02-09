"""
mixcoatl.admin.job
------------------
Implements access to the DCM Job API
"""
from mixcoatl.resource import Resource
from mixcoatl.decorators.lazy import lazy_property
from mixcoatl.utils import camelize, camel_keys, uncamel_keys
import time


class Job(Resource):

    """A job is an asynchronous process resulting from a client request that resulted in a 202
    ACCEPTED response. If the client cares about the ultimate result of the original request, it can
    query for the job returned in the initial response until the job completes."""
    PATH = 'admin/Job'
    COLLECTION_NAME = 'jobs'
    PRIMARY_KEY = 'job_id'

    def __init__(self, job_id=None, **kwargs):
        Resource.__init__(self)
        self.__job_id = job_id

    @property
    def job_id(self):
        """`int` The unique DCM id for this job"""
        return self.__job_id

    @lazy_property
    def status(self):
        """`str` The current status of this job"""
        return self.__status

    @lazy_property
    def description(self):
        """`str` The description of the running job."""
        return self.__description

    @lazy_property
    def message(self):
        """`str` A message describing the current disposition of the operation"""
        return self.__message

    @lazy_property
    def start_date(self):
        """`str` The date and time when the job was started"""
        return self.__start_date

    @lazy_property
    def end_date(self):
        """`str` The data and time when the job was completed
        `None` if :attr:`status is `RUNNING`
        """
        return self.__end_date

    @lazy_property
    def job_message(self):
        return self.__job_message

    @classmethod
    def all(cls, keys_only=False):
        """Get all jobs
        :param keys_only: Only return :attr:`job_id` instead of :class:`Job`
        :type keys_only: bool.
        :returns: `list` of :class:`Job` or :attr:`job_id`
        :raises: :class:`JobException`
        """
        r = Resource(cls.PATH)
        x = r.get()
        if r.last_error is None:
            if keys_only is True:
                return [i[camelize(cls.PRIMARY_KEY)]
                        for i in x[cls.COLLECTION_NAME]]
            else:
                return [type(cls.__name__, (object,), i)
                        for i in uncamel_keys(x)[cls.COLLECTION_NAME]]
        else:
            raise JobException(r.last_error)

    @classmethod
    def wait_for(cls, job_id, status='COMPLETE', callback=None):
        """Blocks execution until :attr:`job_id` returns :attr:`status`

        :param job_id: The ID of the job to wait on
        :type job_id: int.
        :param status: The status to expect before continuing
        :type status: str.
        :param callback: Optional callback to be called with the final :class:`Job`
            when :attr:`status` is reached
        :type callback: func.
        :returns: `bool` - Result of job exectution
        :raises: :class:`JobException`
        """
        j = Job(job_id)
        j.load()
        if j.last_error is not None:
            raise JobException(j.last_error)
        else:
            while j.status != status:
                time.sleep(5)
                j.load()
                if j.status == 'ERROR':
                    break
                else:
                    continue
        if callback is not None:
            callback(j)
        else:
            return True


class JobException(BaseException):
    pass
