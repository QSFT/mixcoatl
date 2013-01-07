from mixcoatl.resource import Resource
from mixcoatl.decorators.lazy import lazy_property

class ApiKey(Resource):
    path = 'admin/ApiKey'
    collection_name = 'apiKeys'
    primary_key = 'access_key'

    def __init__(self, access_key = None, *args, **kwargs):
        Resource.__init__(self)
        self.__access_key = access_key

    @property
    def access_key(self):
        return self.__access_key

    @lazy_property
    def account(self):
        return self.__account

    @lazy_property
    def activation(self):
        return self.__activation

    @lazy_property
    def customer(self):
        return self.__customer

    @lazy_property
    def customer_management_key(self):
        return self.__customer_management_key

    @lazy_property
    def description(self):
        return self.__description

    @lazy_property
    def name(self):
        return self.__name

    @lazy_property
    def secret_key(self):
        return self.__secret_key

    @lazy_property
    def state(self):
        return self.__state

    @lazy_property
    def system_management_key(self):
        return self.__system_management_key

    @lazy_property
    def user(self):
        return self.__user

    @classmethod
    def all(cls, **kwargs):
        r = Resource(cls.path)
        if 'detail' in kwargs:
            r.request_details = kwargs['detail']
        else:
            r.request_details = 'basic'
        c = r.get()
        if r.last_error is None:
            return [cls(i['accessKey']) for i in c[cls.collection_name]]
        else:
            return r.last_error
