"""Implements the DCM ServerProduct API"""
from mixcoatl.utils import uncamel, camelize, camel_keys, uncamel_keys
from mixcoatl.resource import Resource
from mixcoatl.decorators.lazy import lazy_property


class ServerProduct(Resource):

    """The Server Agent resource provides methods by which you can query the output of the Dell
    Cloud Manager agent and retrieve its log output. In the future this will be expanded such that
    you can also query for basic health information of the server on which the agent is installed. """
    PATH = 'infrastructure/ServerProduct'
    COLLECTION_NAME = 'serverProducts'
    PRIMARY_KEY = 'product_id'

    def __init__(self, product_id=None, *args, **kwargs):
        Resource.__init__(self)
        self.__product_id = product_id

    @property
    def product_id(self):
        """`int` - The unique DCM id for this product"""
        return self.__product_id

    @lazy_property
    def cloud(self):
        """`dict` - The cloud in which this server product is valid"""
        return self.__cloud

    @lazy_property
    def architecture(self):
        """`str` - The CPU architecture of the underlying vCPUs"""
        return self.__architecture

    @lazy_property
    def cpu_count(self):
        """`int` - The number of vCPUs for this product"""
        return self.__cpu_count

    @lazy_property
    def cpu_speed_in_mhz(self):
        """`int` - The speed of the vCPUs for this product"""
        return self.__cpu_speed_in_mhz

    @lazy_property
    def currency(self):
        """`str` - The currenct in which the associated costs are charged"""
        return self.__currency

    @lazy_property
    def description(self):
        """`str` - A detailed description of what this product represents"""
        return self.__description

    @lazy_property
    def disk_size_in_gb(self):
        """`int` - The size of the root volume in GB"""
        return self.__disk_size_in_gb

    @lazy_property
    def hourly_rate(self):
        """`int` - The hourly rate for usage of this product"""
        return self.__hourly_rate

    @lazy_property
    def name(self):
        """`str` - The user-friendly name of this product"""
        return self.__name

    @lazy_property
    def platform(self):
        """`str` - The operating system for this product"""
        return self.__platform

    @lazy_property
    def provider_product_id(self):
        """`str` - The cloud provider's unique id for this product"""
        return self.__provider_product_id

    @lazy_property
    def provider_region_id(self):
        """`str` - The cloud provider region id where this product is valid"""
        return self.__provider_region_id

    @lazy_property
    def ram_in_mb(self):
        """`int` - The memory size for this product in MB"""
        return self.__ram_in_mb

    @lazy_property
    def software(self):
        """`str` - Any additional software installed on this product"""
        return self.__software

    @classmethod
    def all(cls, region_id, **kwargs):
        """Return all server products

        :param region_id: The region id to search in
        :type region_id: int.
        :param keys_only: Return :attr:`product_id` or :class:`ServerProduct`
        :type keys_only: bool.
        :param detail: Level of detail to return - `basic` or `extended`
        :type detail: str.
        :returns: `list` of :attr:`product_id` or :class:`ServerProduct`
        :raises: :class:`ServerProductException`
        """
        r = Resource(cls.PATH)
        r.request_details = 'basic'
        params = {'regionId': region_id}
        if 'keys_only' in kwargs:
            keys_only = kwargs['keys_only']
        else:
            keys_only = False

        x = r.get(params=params)
        if r.last_error is None:
            if keys_only is True:
                return [i[camelize(cls.PRIMARY_KEY)] for i in x[cls.COLLECTION_NAME]]
            else:
                return [type(cls.__name__, (object,), i) for i in uncamel_keys(x)[uncamel(cls.COLLECTION_NAME)]]
        else:
            raise ServerProductException(r.last_error)


class ServerProductException(BaseException):
    pass
