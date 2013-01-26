"""Implements the enStratus Region API"""
from mixcoatl.resource import Resource
from mixcoatl.decorators.lazy import lazy_property
from mixcoatl.utils import camelize

class Region(Resource):
    """A region is a logical sub-infrastructure within a cloud"""
    PATH = 'geography/Region'
    COLLECTION_NAME = 'regions'
    PRIMARY_KEY = 'region_id'

    def __init__(self, region_id = None, *args, **kwargs):
        Resource.__init__(self)
        self.__region_id = region_id

    @property
    def region_id(self):
        """`int` - The unique enStratus id for this region"""
        return self.__region_id

    @lazy_property
    def cloud(self):
        """`dict` - The cloud to which this region belongs"""
        return self.__cloud

    @lazy_property
    def customer(self):
        """`dict` - The customer to whom this region belongs"""
        return self.__customer

    @lazy_property
    def jurisdiction(self):
        """`str` - The legal context in which the region operates"""
        return self.__jurisdiction

    @lazy_property
    def name(self):
        """`str` - The user-friendly name for the region"""
        return self.__name

    @lazy_property
    def provider_id(self):
        """`str` - The cloud provider's unique id for the region"""
        return self.__provider_id

    @lazy_property
    def status(self):
        """`str` - The current status of the region"""
        return self.__status

    @lazy_property
    def description(self):
        """`str` - The description of the region"""
        return self.__description

    @classmethod
    def all(cls, **kwargs):
        """Return all regions

        :param account_id: Limit results to regions with the specified account
        :type account_id: int.
        :param jurisdiction: Limit results to the specified jurisdiction
        :type jurisdiction: str.
        :param scope: Limit results to `all` (Default - cross-cloud)
            or `account` (cloud-specific)
        :type scope: str.
        :param keys_only: Return :attr:`region_id` instead of :class:`Region`
        :type keys_only: bool.
        :param detail: The level of detail to return - `basic` or `extended`
        :type detail: str.
        :returns: `list` of :class:`Region` or :attr:`region_id`
        :raises: :class:`RegionException`
        """
        r = Resource(cls.PATH)
        r.request_details = 'basic'
        params = {}
        if 'keys_only' in kwargs:
            keys_only = kwargs['keys_only']
        else:
            keys_only = False
        for x in ['account_id', 'jurisdiction', 'scope']:
            if x in kwargs:
                params[camelize(x)] = kwargs[x]
        c = r.get(params=params)
        if r.last_error is None:
            if keys_only is True:
                regions = [item['regionId'] for item in c[cls.COLLECTION_NAME]]
            else:
                regions = []
                for i in c[cls.COLLECTION_NAME]:
                    region = cls(i['regionId'])
                    if 'detail' in kwargs:
                        region.request_details = kwargs['detail']
                    region.load()
                    regions.append(region)
            return regions
        else:
            raise RegionException(r.last_error)

class RegionException(BaseException): pass
