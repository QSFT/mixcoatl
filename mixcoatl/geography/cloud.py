from mixcoatl.resource import Resource
from mixcoatl.decorators.lazy import lazy

@lazy(key='cloud_id')
class Cloud(Resource):
    path = 'geography/Cloud'
    collection_name = 'clouds'

    def __init__(self, cloud_id = None, *args, **kwargs):
        Resource.__init__(self)
        if cloud_id is None:
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

        self.__cloud_id = cloud_id

    @property
    def cloud_id(self):
        return self.__cloud_id

    @property
    def cloud_provider_console_url(self):
        return self.__cloud_provider_console_url

    @property
    def cloud_provider_logo_url(self):
        return self.__cloud_provider_logo_url

    @property
    def cloud_provider_name(self):
        return self.__cloud_provider_name

    @property
    def compute_account_number_label(self):
        return self.__compute_account_number_label

    @property
    def compute_delegate(self):
        return self.__compute_delegate

    @property
    def compute_endpoint(self):
        return self.__compute_endpoint

    @property
    def compute_secret_key_label(self):
        return self.__compute_secret_key_label

    @property
    def documentation_label(self):
        return self.__documentation_label

    @property
    def name(self):
        return self.__name

    @property
    def private_cloud(self):
        return self.__private_cloud

    @property
    def status(self):
        return self.__status

    @classmethod
    def all(cls):
        r = Resource(cls.path)
        c = r.get()
        if r.last_error is None:
            return c
        else:
            return r.last_error