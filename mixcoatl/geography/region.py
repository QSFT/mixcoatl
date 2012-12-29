from mixcoatl.resource import Resource
from mixcoatl.decorators.lazy import lazy

@lazy(key='region_id')
class Region(Resource):
    path = 'geography/Region'
    collection_name = 'regions'

    def __init__(self, region_id = None, *args, **kwargs):
        Resource.__init__(self)
        if region_id is None:
            pass
            #            self.__name = None
        #            self.__status = None
        #            self.__cloud_provider_console_url = None
        #            self.__cloud_provider_logo_url = None
        #            self.__cloud_provider_name = None
        #            self.__compute_account_number_label = None
        #            self.__compute_delegate = None
        #            self.__compute_endpoint = None
        #            self.__compute_secret_key_label = None
        #            self.__documentation_label = None
        #            self.__private_cloud = None

        self.__region_id = region_id

    @property
    def region_id(self):
        return self.__region_id

    @property
    def cloud(self):
        return self.__cloud

    @property
    def customer(self):
        return self.__customer

    @property
    def jurisdiction(self):
        return self.__jurisdiction

    @property
    def name(self):
        return self.__name

    @property
    def provider_id(self):
        return self.__provider_id

    @property
    def status(self):
        return self.__status

    @classmethod
    def all(cls,deref=False):
        r = Resource(cls.path)
        c = r.get()
        if r.last_error is None:
            return [cls(item['regionId']) for item in c[cls.collection_name]]
        else:
            return r.last_error