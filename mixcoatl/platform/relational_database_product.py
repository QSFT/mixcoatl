from mixcoatl.resource import Resource
from mixcoatl.admin.job import Job
from mixcoatl.decorators.lazy import lazy_property
from mixcoatl.utils import uncamel, camelize, camel_keys, uncamel_keys


class RelationalDatabaseProduct(Resource):
    """Represents a product with costs from a cloud relational database vendor."""

    PATH = 'platform/RelationalDatabaseProduct'
    COLLECTION_NAME = 'rdbmsProducts'
    PRIMARY_KEY = 'product_id'

    def __init__(self, product_id=None, *args, **kwargs):
        Resource.__init__(self)
        self.__product_id = product_id

    @property
    def product_id(self):
        """`int` - The unique ID in DCM for this relational database product."""
        return self.__product_id

    @lazy_property
    def status(self):
        """`str` - The current status of the product."""
        return self.__status

    @lazy_property
    def architecture(self):
        """`str` - The underlying CPU architecture of this database server."""
        return self.__architecture

    @lazy_property
    def cloud(self):
        """`dict` - The cloud for which this product operates."""
        return self.__cloud

    @lazy_property
    def core_count(self):
        """`int` - The number of CPU cores allocated to your database environment."""
        return self.__core_count

    @lazy_property
    def cpu_in_g_hz(self):
        """`int` - The speed of the CPUs allocated to your database environment."""
        return self.__cpu_in_g_hz

    @lazy_property
    def custom_pricing(self):
        """`bool` - Indicates whether or not this pricing reflects the standard retail rates from the cloud provider."""
        return self.__custom_pricing

    @lazy_property
    def description(self):
        """`str` - A long description for this product."""
        return self.__description

    @lazy_property
    def engine(self):
        """ `enum` - The database engine represented by this product."""
        return self.__engine

    @lazy_property
    def hourly_pricing(self):
        """`dict` - The hourly rate the cloud provider charges for having a relational database provisioned."""
        return self.__hourly_pricing

    @lazy_property
    def io_pricing(self):
        """`dict` - The rate charged by the cloud provider for data going in and out of the cloud to the database."""
        return self.__io_pricing

    @lazy_property
    def io_units(self):
        """`int` - The number of I/O units reflecting in the I/O pricing."""
        return self.__io_units

    @lazy_property
    def maximum_storage_in_gb(self):
        """`int` - The amount of storage up to which you may have allocated to be reflected by this product."""
        return self.__maximum_storage_in_gb

    @lazy_property
    def memory_in_gb(self):
        """`int` - The amount of RAM allocated to this virtual database server."""
        return self.__memory_in_gb

    @lazy_property
    def minimum_storage_in_gb(self):
        """`int` - The amount of storage you must have allocated to receive the pricing reflected in this product."""
        return self.__minimum_storage_in_gb

    @lazy_property
    def name(self):
        """`str` - A user-friendly name to describe this product."""
        return self.__name

    @lazy_property
    def region(self):
        """`dict` - A region for which this product is good."""
        return self.__region

    @lazy_property
    def provider_id(self):
        """`str` - How this product is identified to the cloud provider."""
        return self.__provider_id

    @lazy_property
    def storage_pricing(self):
        """`dict` - The rate per storageUnits charged for the storage allocated for this relational database product."""
        return self.__storage_pricing

    @lazy_property
    def storage_units(self):
        """`int` - The number of storage units reflected in the storage pricing."""
        return self.__storage_units

    def reload(self):
        """Reload resource data from API calls"""
        if self.product_id is not None:
            self.load()
        elif self.current_job is None:
            self.load()
        else:
            if Job.wait_for(self.current_job):
                job = Job(self.current_job)
                self.__relational_database_id = job.message
                self.load()
            else:
                return self.last_error

    @classmethod
    def all(cls, region_id, engine, **kwargs):
        """Get a list of all known relational_databases

        >>> RelationalDatabaseProduct.all(region_id=100, engine='MYSQL51')
        [{'product_id':1,...},{'product_id':2,...}]

        :returns: list -- a list of :class:`RelationalDatabaseProduct`
        :raises: RelationalDatabaseProductException
        """
        r = Resource(cls.PATH)
        r.request_details = 'basic'
        params = {'regionId': region_id, 'engine': engine}

        if 'detail' in kwargs:
            r.request_details = kwargs['detail']
        else:
            r.request_details = 'basic'

        if 'keys_only' in kwargs:
            keys_only = kwargs['keys_only']
        else:
            keys_only = False

        x = r.get(params=params)
        if r.last_error is None:
            if keys_only is True:
                results = [i[camelize(cls.PRIMARY_KEY)] for i in x[cls.COLLECTION_NAME]]
            else:
                results = [type(cls.__name__, (object,), i) for i in uncamel_keys(x)[uncamel(cls.COLLECTION_NAME)]]
            return results
        else:
            raise RelationalDatabaseProductException(r.last_error)

class RelationalDatabaseProductException(BaseException):
    pass
