from mixcoatl.resource import Resource
from mixcoatl.decorators.lazy import lazy_property

class User(Resource):
    path = 'admin/User'
    collection_name = 'users'
    primary_key = 'user_id'

    def __init__(self, user_id=None, *args, **kwargs):
        Resource.__init__(self)
        self.__user_id = user_id

    @property
    def user_id(self):
        return self.__user_id

    @lazy_property
    def alpha_name(self):
        return self.__alpha_name

    @lazy_property
    def customer(self):
        return self.__customer

    @lazy_property
    def editable(self):
        return self.__editable

    @lazy_property
    def email(self):
        return self.__email

    @lazy_property
    def family_name(self):
        return self.__family_name

    @lazy_property
    def given_name(self):
        return self.__given_name

    @lazy_property
    def groups(self):
        return self.__groups

    @lazy_property
    def has_cloud_api_access(self):
        return self.__has_cloud_api_access

    @lazy_property
    def has_cloud_console_access(self):
        return self.__has_cloud_console_access

    @lazy_property
    def status(self):
        return self.__status

    @lazy_property
    def time_zone(self):
        return self.__time_zone

    @lazy_property
    def vm_login_id(self):
        return self.__vm_login_id

    @lazy_property
    def ssh_public_key(self):
        return self.__ssh_public_key

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