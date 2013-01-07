from mixcoatl.resource import Resource
from mixcoatl.decorators.lazy import lazy_property

class User(Resource):
    path = 'admin/User'
    collection_name = 'users'
    primary_key = 'userId'

    def __init__(self, user_id=None, *args, **kwargs):
        Resource.__init__(self)
        self.__user_id = user_id

    @property
    def user_id(self):
        return self.__user_id

    @classmethod
    def all(cls, **kwargs):
        r = Resource(cls.path)
        if 'details' in kwargs:
            r.request_details = kwargs['details']
        else:
            r.request_details = 'basic'

        x = r.get()
        if r.last_error is None:
            return [cls(i['userId']) for i in x[cls.collection_name]]
        else:
            return x.last_error