from mixcoatl.resource import Resource
from mixcoatl.decorators.lazy import lazy_property
from mixcoatl.decorators.validations import required_attrs
from mixcoatl.utils import camelize

class Personality(Resource):
    PATH = 'automation/Personality'
    COLLECTION_NAME = 'personalities'
    PRIMARY_KEY = 'cmAccountId'

    def __init__(self, cmAccountId = None, *args, **kwargs):
        Resource.__init__(self)
        self.__cmAccountId = cmAccountId 

    @property
    def cmAccountId(self):
        return self.__cmAccountId

    @classmethod
    def all(cls, cmAccountId, **kwargs):
        r = Resource(cls.PATH)
        r.request_details = 'basic'
        params = {'cmAccountId':cmAccountId}
        c = r.get(params=params)
        if r.last_error is None:
        	return c[cls.COLLECTION_NAME]
        else:
        	raise PersonalityException(r.last_error)

class PersonalityException(BaseException): pass