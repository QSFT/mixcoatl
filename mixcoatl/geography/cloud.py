from mixcoatl.resource import Resource
from mixcoatl.decorators.lazy import lazy_property

class Cloud(Resource):
    path = 'geography/Cloud'
    collection_name = 'clouds'
    primary_key = 'cloud_id'

    def __init__(self, cloud_id = None, *args, **kwargs):
        Resource.__init__(self)
        self.__cloud_id = cloud_id

    @property
    def cloud_id(self):
        return self.__cloud_id

    @lazy_property
    def cloud_provider_console_url(self):
        return self.__cloud_provider_console_url

    @lazy_property
    def cloud_provider_logo_url(self):
        return self.__cloud_provider_logo_url

    @lazy_property
    def cloud_provider_name(self):
        return self.__cloud_provider_name

    @lazy_property
    def compute_account_number_label(self):
        return self.__compute_account_number_label

    @lazy_property
    def compute_delegate(self):
        return self.__compute_delegate

    @lazy_property
    def compute_endpoint(self):
        return self.__compute_endpoint

    @lazy_property
    def compute_secret_key_label(self):
        return self.__compute_secret_key_label

    @lazy_property
    def documentation_label(self):
        return self.__documentation_label

    @lazy_property
    def name(self):
        return self.__name

    @lazy_property
    def private_cloud(self):
        return self.__private_cloud

    @lazy_property
    def status(self):
        return self.__status

    @classmethod
    def all(cls):
        r = Resource(cls.path)
        c = r.get()
        if r.last_error is None:
            return [cls(i['cloudId']) for i in c[cls.collection_name]]
        else:
            return r.last_error