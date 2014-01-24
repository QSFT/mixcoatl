"""Implements the enStratus Cloud API"""
from mixcoatl.resource import Resource
from mixcoatl.decorators.lazy import lazy_property
from mixcoatl.utils import camelize

class Subscription(Resource):
    PATH = 'geography/Subscription'
    COLLECTION_NAME = 'subscriptions'
    PRIMARY_KEY = 'region_id'

    def __init__(self, region_id = None, *args, **kwargs):
        Resource.__init__(self)
        self.__region_id = region_id

    @property
    def region_id(self):
        return self.__region_id

    @classmethod
    def region(cls, region_id, **kwargs):
        """Returns subscription for given Region"""

        r = Resource(cls.PATH+"/"+str(region_id))
        r.request_details = 'basic'
        s = r.get()
        return s

    @classmethod
    def all(cls, **kwargs):
        """Returns subscriptions for all regions"""

        r = Resource(cls.PATH)
        r.request_details = 'basic'
        s = r.get()
        return s