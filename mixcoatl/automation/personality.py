from mixcoatl.resource import Resource
from mixcoatl.decorators.lazy import lazy_property
from mixcoatl.decorators.validations import required_attrs
from mixcoatl.utils import camelize, camel_keys, uncamel_keys


class Personality(Resource):

    """ A Dell Cloud Manager personality represents an ordered collection of scripts and/or
    personalities that are executed in an environment to bring a server to fit a certain role. """
    PATH = 'automation/Personality'
    COLLECTION_NAME = 'personalities'
    PRIMARY_KEY = 'cmAccountId'

    def __init__(self, cmAccountId=None, *args, **kwargs):
        Resource.__init__(self)
        self.__cmAccountId = cmAccountId

    @property
    def cmAccountId(self):
        return self.__cmAccountId

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
            raise PersonalityException(r.last_error)


class PersonalityException(BaseException):
    pass
