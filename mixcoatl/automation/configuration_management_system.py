from mixcoatl.resource import Resource
from mixcoatl.decorators.lazy import lazy_property
from mixcoatl.decorators.validations import required_attrs
from mixcoatl.utils import uncamel, camelize, camel_keys, uncamel_keys
import json

class ConfigurationManagementSystem(Resource):
    PATH = 'automation/ConfigurationManagementSystem'
    COLLECTION_NAME = 'cmSystems'
    PRIMARY_KEY = 'cm_system_id'

    def __init__(self, cm_account_id=None, *args, **kwargs):
        Resource.__init__(self)

    @classmethod
    def all(cls, **kwargs):
        r = Resource(cls.PATH)
        if 'details' in kwargs:
            r.request_details = kwargs['details']
        else:
            r.request_details = 'basic'

        if 'keys_only' in kwargs:
            keys_only = kwargs['keys_only']
        else:
            keys_only = False

        x = r.get()
        if r.last_error is None:
            if keys_only is True:
                results = [i[camelize(cls.PRIMARY_KEY)] for i in x[cls.COLLECTION_NAME]]
            else:
                results = [type(cls.__name__, (object,), i) for i in uncamel_keys(x)[uncamel(cls.COLLECTION_NAME)]]
            return results
        else:
            return x.last_error


class CMException(BaseException):
    pass
	

class CMCreationException(CMException):
    """CM Creation Exception"""
    pass