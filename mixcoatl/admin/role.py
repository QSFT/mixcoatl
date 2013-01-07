from mixcoatl.resource import Resource
from mixcoatl.decorators.lazy import lazy_property

class Role(Resource):
    path = 'admin/Role'
    collection_name = 'roles'
    primary_key = 'role_id'

    def __init__(self, role_id=None, *args, **kwargs):
        Resource.__init__(self)
        self.__role_id = role_id

    @property
    def role_id(self):
        return self.__role_id

    @lazy_property
    def acl(self):
        return self.__acl

    @lazy_property
    def description(self):
        return self.__description

    @lazy_property
    def customer(self):
        return self.__customer

    @lazy_property
    def name(self):
        return self.__name

    @lazy_property
    def status(self):
        return self.__status

    @classmethod
    def all(cls, **kwargs):
        r = Resource(cls.path)
        if 'details' in kwargs:
            r.request_details = kwargs['details']
        else:
            r.request_details = 'basic'

        x = r.get()
        if r.last_error is None:
            return [cls(i['roleId']) for i in x[cls.collection_name]]
        else:
            return x.last_error