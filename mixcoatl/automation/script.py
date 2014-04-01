from mixcoatl.resource import Resource
from mixcoatl.decorators.lazy import lazy_property
from mixcoatl.decorators.validations import required_attrs
from mixcoatl.utils import camelize

class Script(Resource):
    PATH = 'automation/Script'
    COLLECTION_NAME = 'scripts'
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
        return c[cls.COLLECTION_NAME]

class ScriptException(BaseException): pass