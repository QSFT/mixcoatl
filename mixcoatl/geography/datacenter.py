from mixcoatl.resource import Resource
from mixcoatl.decorators.lazy import lazy

@lazy(key='datacenter_id')
class DataCenter(Resource):
    path = 'geography/DataCenter'
    collection_name = 'dataCenters'

    def __init__(self, datacenter_id = None, *args, **kwargs):
        Resource.__init__(self)
        if datacenter_id is None:
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

        self.__datacenter_id = datacenter_id

    @property
    def datacenter_id(self):
        return self.__datacenter_id

    @property
    def description(self):
        return self.__description

    @property
    def name(self):
        return self.__name

    @property
    def provider_id(self):
        return self.__provider_id

    @property
    def region(self):
        return self.__region

    @property
    def status(self):
        return self.__status

    @classmethod
    def all(cls,region_id):
        r = Resource(cls.path)
        params = {'regionId':region_id}
        c = r.get(params=params)
        if r.last_error is None:
            x = [cls(i['dataCenterId']) for i in c[cls.collection_name]]
            return x
        else:
            return r.last_error