"""Implements the ability to list CM environments via the API"""
from mixcoatl.resource import Resource
from mixcoatl.decorators.lazy import lazy_property
from mixcoatl.decorators.validations import required_attrs
from mixcoatl.utils import camelize, camel_keys, uncamel_keys
from mixcoatl.admin.job import Job


class Environment(Resource):

    """ An Dell Cloud Manager environment represents a Chef environment and is managed in a
    configuration management account.  Environments are NOT uniquely identified by their environmentId. 
    The unique identifier is sharedEnvironmentCode. """
    PATH = 'automation/Environment'
    COLLECTION_NAME = 'environments'
    PRIMARY_KEY = 'environmentId'

    def __init__(self, environmentId=None, *args, **kwargs):
        Resource.__init__(self)
        self.__environmentId = environmentId

    @classmethod
    def all(cls, cmAccountId, **kwargs):
        r = Resource(cls.PATH)

        if 'detail' in kwargs:
            r.request_details = kwargs['detail']
        else:
            r.request_details = 'basic'

        if 'keys_only' in kwargs:
            keys_only = kwargs['keys_only']
        else:
            keys_only = False

        params = {'cmAccountId': cmAccountId}
        x = r.get(params=params)
        if r.last_error is None:
            if keys_only is True:
                return [i[camelize(cls.PRIMARY_KEY)] for i in x[cls.COLLECTION_NAME]]
            else:
                return [type(cls.__name__, (object,), i) for i in uncamel_keys(x)[cls.COLLECTION_NAME]]
        else:
            raise EnvironmentException(r.last_error)


class EnvironmentException(BaseException):
    pass
