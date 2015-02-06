from mixcoatl.resource import Resource
from mixcoatl.decorators.lazy import lazy_property
from mixcoatl.decorators.validations import required_attrs
from mixcoatl.utils import uncamel, camelize, camel_keys, uncamel_keys
import json


class ConfigurationManagementSystem(Resource):

    """A configuration management system represents a product supported by Dell Cloud Manager for
    configuration management. It might be a commercial product like Chef or Puppet or a custom,
    in-house system. Configuration management systems are configured by a Dell Cloud Manager
    administrator. In the SaaS environment, you may request through the help desk system for Dell
    Cloud Manager to include your configuration management system of choice if it isn’t one that
    is supported. """
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
                return [i[camelize(cls.PRIMARY_KEY)] for i in x[cls.COLLECTION_NAME]]
            else:
                return [type(cls.__name__, (object,), i) for i in uncamel_keys(x)[uncamel(cls.COLLECTION_NAME)]]
        else:
            raise CMException(r.last_error)


class CMException(BaseException):
    pass


class CMCreationException(CMException):

    """CM Creation Exception"""
    pass
