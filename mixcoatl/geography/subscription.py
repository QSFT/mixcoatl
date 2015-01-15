"""Implements the DCM Cloud API"""
from mixcoatl.resource import Resource
from mixcoatl.decorators.lazy import lazy_property
from mixcoatl.utils import camelize, camel_keys, uncamel_keys

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
    def all(cls, keys_only=False):
        r = Resource(cls.PATH)
        x = r.get()
        if r.last_error is None:
            if keys_only is True:
                results = [i[camelize(cls.PRIMARY_KEY)] for i in x[cls.COLLECTION_NAME]]
            else:
                results = [type(cls.__name__, (object,), i) for i in uncamel_keys(x)[cls.COLLECTION_NAME]]
            return results
        else:
            raise SubscriptionException(r.last_error)

class SubscriptionException(BaseException):
    pass