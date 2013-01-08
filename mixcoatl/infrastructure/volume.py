from mixcoatl.resource import Resource
from mixcoatl.decorators.lazy import lazy_property
from mixcoatl.utils import camelize

class Volume(Resource):
    path = 'infrastructure/Volume'
    collection_name = 'volumes'
    primary_key = 'volume_id'

    def __init__(self, volume_id=None, *args, **kwargs):
        Resource.__init__(self)
        self.__volume_id = volume_id

    @property
    def volume_id(self):
        return self.__volume_id

    @lazy_property
    def available(self):
        return self.__available

    @lazy_property
    def customer(self):
        return self.__customer

    @lazy_property
    def provider_id(self):
        return self.__provider_id

    @lazy_property
    def size_string(self):
        return self.__size_string

    @lazy_property
    def name(self):
        return self.__name

    @lazy_property
    def encrypted(self):
        return self.__encrypted

    @lazy_property
    def region(self):
        return self.__region

    @lazy_property
    def budget(self):
        return self.__budget

    @lazy_property
    def server(self):
        return self.__server

    @lazy_property
    def owning_groups(self):
        return self.__owning_groups

    @lazy_property
    def size_in_gb(self):
        return self.__size_in_gb

    @lazy_property
    def status(self):
        return self.__status

    @lazy_property
    def removable(self):
        return self.__removable

    @lazy_property
    def data_center(self):
        return self.__data_center

    @lazy_property
    def owning_account(self):
        return self.__owning_account

    @lazy_property
    def device_id(self):
        return self.__device_id

    @lazy_property
    def creation_timestamp(self):
        return self.__creation_timestamp

    @lazy_property
    def owning_user(self):
        return self.__owning_user

    @lazy_property
    def cloud(self):
        return self.__cloud

    @lazy_property
    def description(self):
        return self.__description

    @classmethod
    def all(cls, **kwargs):
        r = Resource(cls.path)
        if 'details' in kwargs:
            r.request_details = kwargs['details']
        else:
            r.request_details = 'basic'

        x = r.get()
        if r.last_error is None:
            return [cls(i[camelize(cls.primary_key)]) for i in x[cls.collection_name]]
        else:
            return x.last_error