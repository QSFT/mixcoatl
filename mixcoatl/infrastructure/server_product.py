from mixcoatl.resource import Resource
from mixcoatl.decorators.lazy import lazy_property

class ServerProduct(Resource):
    path = 'infrastructure/ServerProduct'
    collection_name = 'serverProducts'
    primary_key = 'product_id'

    def __init__(self, product_id = None, *args, **kwargs):
        Resource.__init__(self)
        self.__product_id = product_id

    @property
    def product_id(self):
        return self.__product_id
        
    @lazy_property
    def cloud(self):
        return self.__cloud

    @lazy_property
    def architecture(self):
        return self.__architecture

    @lazy_property
    def cpu_count(self):
        return self.__cpu_count

    @lazy_property
    def cpu_speed_in_mhz(self):
        return self.__cpu_speed_in_mhz

    @lazy_property
    def currency(self):
        return self.__currency

    @lazy_property
    def description(self):
        return self.__description

    @lazy_property
    def disk_size_in_gb(self):
        return self.__disk_size_in_gb

    @lazy_property
    def hourly_rate(self):
        return self.__hourly_rate

    @lazy_property
    def name(self):
        return self.__name

    @lazy_property
    def platform(self):
        return self.__platform

    @lazy_property
    def provider_product_id(self):
        return self.__provider_product_id

    @lazy_property
    def provider_region_id(self):
        return self.__provider_region_id

    @lazy_property
    def ram_in_mb(self):
        return self.__ram_in_mb

    @lazy_property
    def software(self):
        return self.__software

    @classmethod
    def all(cls, region_id):
        from mixcoatl.utils import uncamel_keys
        r = Resource(cls.path)
        params = {'regionId':region_id}
        c = r.get(params=params)
        if r.last_error is None:
            return [cls(i['productId']) for i in c[cls.collection_name]]
        else:
            return r.last_error