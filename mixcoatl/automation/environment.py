"""Implements the ability to list CM environments via the API"""
from mixcoatl.resource import Resource
from mixcoatl.decorators.lazy import lazy_property
from mixcoatl.decorators.validations import required_attrs
from mixcoatl.utils import camelize, camel_keys
from mixcoatl.admin.job import Job

class Environment(Resource):
    PATH = 'automation/Environment'
    COLLECTION_NAME = 'environments'
    PRIMARY_KEY = 'environmentId'

    def __init__(self, environmentId=None, *args, **kwargs):
        Resource.__init__(self)
        self.__environmentId = environmentId

    @classmethod
    def all(cls, cmAccountId, **kwargs):
        r = Resource(cls.PATH)
        r.request_details = 'basic'
        params = {'cmAccountId':cmAccountId}
        x = r.get(params=params)
        if r.last_error is None:
        	return x[cls.COLLECTION_NAME]
        else:
        	return r.last_error

class EnvironmentException(BaseException): pass