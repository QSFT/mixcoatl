"""Implements the DCM DataCenter API"""
from mixcoatl.resource import Resource
from mixcoatl.decorators.lazy import lazy_property
from mixcoatl.utils import uncamel, camelize, camel_keys, uncamel_keys


class DataCenter(Resource):

    """
    A data center is a part of a regional infrastructure that has some ability
        to share resources with other data centers in the region
    """
    PATH = 'geography/DataCenter'
    COLLECTION_NAME = 'dataCenters'
    PRIMARY_KEY = 'data_center_id'

    def __init__(self, data_center_id=None, *args, **kwargs):
        Resource.__init__(self)
        self.__data_center_id = data_center_id

    @property
    def data_center_id(self):
        """`int` - The unique DCM id for this data center"""
        return self.__data_center_id

    @lazy_property
    def description(self):
        """`str` - A description of the data center"""
        return self.__description

    @lazy_property
    def name(self):
        """`str` - A user-friendly name for the data center"""
        return self.__name

    @lazy_property
    def provider_id(self):
        """`str` - The cloud provider's unique id for the data center"""
        return self.__provider_id

    @lazy_property
    def region(self):
        """`dict` = The region to which this data center belongs"""
        return self.__region

    @lazy_property
    def status(self):
        """`str` - The current status of the data center"""
        return self.__status

    @classmethod
    def all(cls, region_id, **kwargs):
        """Return all data centers

        :param region_id: Required. The region to query against
        :type region_id: int.
        :param keys_only: Return :attr:`data_center_id` instead of :class:`DataCenter`
        :type keys_only: bool.
        :param detail: The level of detail to return - `basic` or `extended`
        :type detail: str.
        :returns: `list` of :class:`DataCenter` or :attr:`data_center_id`
        :raises: :class:`DataCenterException`
        """
        r = Resource(cls.PATH)

        if 'detail' in kwargs:
            r.request_details = kwargs['detail']
        else:
            r.request_details = 'basic'

        if 'keys_only' in kwargs:
            keys_only = kwargs['keys_only']
        else:
            keys_only = False

        params = {'regionId': region_id}

        x = r.get(params=params)
        if r.last_error is None:
            if keys_only is True:
                return [i[camelize(cls.PRIMARY_KEY)] for i in x[cls.COLLECTION_NAME]]
            else:
                return [type(cls.__name__, (object,), i) for i in uncamel_keys(x)[uncamel(cls.COLLECTION_NAME)]]
        else:
            raise DataCenterException(r.last_error)


class DataCenterException(BaseException):
    pass
