from mixcoatl.resource import Resource
from mixcoatl.decorators.lazy import lazy_property

class Region(Resource):
    path = 'geography/Region'
    collection_name = 'regions'
    primary_key = 'region_id'

    def __init__(self, region_id = None, *args, **kwargs):
        Resource.__init__(self)
        self.__region_id = region_id

    @property
    def region_id(self):
        return self.__region_id

    @lazy_property
    def cloud(self):
        return self.__cloud

    @lazy_property
    def customer(self):
        return self.__customer

    @lazy_property
    def jurisdiction(self):
        return self.__jurisdiction

    @lazy_property
    def name(self):
        return self.__name

    @lazy_property
    def provider_id(self):
        return self.__provider_id

    @lazy_property
    def status(self):
        return self.__status

    @lazy_property
    def description(self):
        return self.__description

    @classmethod
    def all(cls,deref=False):
        r = Resource(cls.path)
        c = r.get()
        if r.last_error is None:
            return [cls(item['regionId']) for item in c[cls.collection_name]]
        else:
            return r.last_error