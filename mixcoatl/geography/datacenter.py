"""Implements the enStratus DataCenter API"""
from mixcoatl.resource import Resource
from mixcoatl.decorators.lazy import lazy_property

class DataCenter(Resource):
    """
    A data center is a part of a regional infrastructure that has some ability
        to share resources with other data centers in the region
    """
    PATH = 'geography/DataCenter'
    COLLECTION_NAME = 'dataCenters'
    PRIMARY_KEY = 'data_center_id'

    def __init__(self, data_center_id = None, *args, **kwargs):
        Resource.__init__(self)
        self.__data_center_id = data_center_id

    @property
    def data_center_id(self):
        """`int` - The unique enStratus id for this data center"""
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
        if 'keys_only' in kwargs:
            keys_only = kwargs['keys_only']
        else:
            keys_only = False

        r = Resource(cls.PATH)
        r.request_details = 'basic'
        params = {'regionId':region_id}
        c = r.get(params=params)
        if r.last_error is None:
            if keys_only is True:
                dcs = [i['dataCenterId'] for i in c[cls.COLLECTION_NAME]]
            else:
                dcs = []
                for i in c[cls.COLLECTION_NAME]:
                    dc = cls(i['dataCenterId'])
                    if 'detail' in kwargs:
                        dc.request_details = kwargs['detail']
                    dc.load()
                    dcs.append(dc)
            return dcs
        else:
            raise DataCenterException(r.last_error)

class DataCenterException(BaseException): pass
