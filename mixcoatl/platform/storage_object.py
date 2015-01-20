from mixcoatl.resource import Resource
from mixcoatl.admin.job import Job
from mixcoatl.decorators.lazy import lazy_property
from mixcoatl.utils import uncamel, camelize, camel_keys, uncamel_keys


class StorageObject(Resource):
    """A blob or container in which blobs are stored in a cloud storage system."""
    PATH = 'platform/StorageObject'
    COLLECTION_NAME = 'storageObjects'
    PRIMARY_KEY = 'storage_object_id'

    def __init__(self, storage_object_id=None, *args, **kwargs):
        Resource.__init__(self)
        self.__storage_object_id = storage_object_id

    @property
    def storage_object_id(self):
        """`int` - The unique ID of this storage object."""
        return self.__storage_object_id

    @lazy_property
    def budget(self):
        """`int` - The budget to which the data stored in a container/bucket is billed against."""
        return self.__budget

    @lazy_property
    def e_type(self):
        """`str` - The type of storage object."""
        return self.__e_type

    @lazy_property
    def cloud(self):
        """`dict` - The cloud for which this storage object rests."""
        return self.__cloud

    @lazy_property
    def container(self):
        """`dict` - The container in which this storage object rests."""
        return self.__container

    @lazy_property
    def find_free_name(self):
        """`bool` - If this field is true and there is a name conflict in the cloud DCM will append numbers to the end of the name until it finds an available name for the storage object. If the field is false and there is a name conflict an error will be thrown."""
        return self.__find_free_name

    @lazy_property
    def created_timestamp(self):
        """`str` - The time when this storage object was initially created in cloud storage."""
        return self.__created_timestamp

    @lazy_property
    def label(self):
        """`str` - A label for displaying the storage object."""
        return self.__label

    @lazy_property
    def last_modified_timestamp(self):
        """`str` - The time when this storage object last had changes made to it."""
        return self.__last_modified_timestamp

    @lazy_property
    def name(self):
        """`str` - A user-friendly name you use to identify the storage object."""
        return self.__name

    @lazy_property
    def owning_group(self):
        """`str` - The group owning this container and governing permissions on the container."""
        return self.__owning_group

    @lazy_property
    def owning_user(self):
        """`str` - The user who owns this storage object."""
        return self.__owning_user

    @lazy_property
    def provider_id(self):
        """`str` - The unique identifier in the cloud storage system for this storage object."""
        return self.__provider_id

    @lazy_property
    def read_any(self):
        """`bool` - Indicates that anyone with access to this account can read items stored in the container. Only for containers."""
        return self.__read_any

    @lazy_property
    def read_code(self):
        """`bool` - Indicates that anyone with provisioning rights to the billing code under which this container is billed can read items stored in the container. Only for containers."""
        return self.__read_code

    @lazy_property
    def read_group(self):
        """`bool` - Indicates that anyone in the same group owning this container can read items stored in the container. Only valid for containers."""
        return self.__read_group

    @lazy_property
    def read_public(self):
        """`bool` - Indicates that items in this container should be made public to the entire world. Only valid for containers."""
        return self.__read_public

    @lazy_property
    def region(self):
        """`str` - The region in which this object is stored."""
        return self.__region

    @lazy_property
    def size(self):
        """`int` - The file size for the storage object. Only valid for objects of type 'blob'."""
        return self.__size

    @lazy_property
    def write_any(self):
        """`bool` - Indicates that anyone with access to this account can write to this container. Valid only for containers."""
        return self.__write_any

    @lazy_property
    def write_code(self):
        """`bool` - Indicates that anyone with provisioning rights to the billing code under which this container is billed can write to the container. Valid only for containers."""
        return self.__write_code

    @lazy_property
    def write_group(self):
        """`bool` - Indicates that anyone in the same group owning this container can write to this container. Valid only for containers."""
        return self.__write_group

    def reload(self):
        """Reload resource data from API calls"""
        if self.storage_object_id is not None:
            self.load()
        elif self.current_job is None:
            self.load()
        else:
            if Job.wait_for(self.current_job):
                job = Job(self.current_job)
                self.__storage_object_id = job.message
                self.load()
            else:
                return self.last_error

    @classmethod
    def all(cls, region_id, **kwargs):
        """Get a list of all known storage objects.

        >>> StorageObject.all(region_id=100)
        [{'storage_object_id':1,...},{'storage_object_id':2,...}]

        :returns: list -- a list of :class:`StorageObject`
        :raises: StorageObjectException
        """
        r = Resource(cls.PATH)
        params = {'regionId': region_id}

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
            raise StorageObjectException(r.last_error)


class StorageObjectException(BaseException):
    pass
