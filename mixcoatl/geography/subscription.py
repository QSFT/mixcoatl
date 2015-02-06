"""Implements the DCM Cloud API"""
from mixcoatl.resource import Resource
from mixcoatl.decorators.lazy import lazy_property
from mixcoatl.utils import camelize, camel_keys, uncamel_keys


class Subscription(Resource):

    """ A subscription describes the capabilities of a specific region as matched by your subscription to
    the region. You can use this object to tell what cloud capabilities exist in this region. In some
    cases, failure to support something will be a limitation/design choice of the cloud in question. In
    other cases, it just represents the fact that you have yet to subscribe to the service in question. """
    PATH = 'geography/Subscription'
    COLLECTION_NAME = 'subscriptions'
    PRIMARY_KEY = 'region_id'

    def __init__(self, region_id=None, *args, **kwargs):
        Resource.__init__(self)
        self.__region_id = region_id

    @classmethod
    def all(cls, keys_only=False, **kwargs):
        if 'region_id' in kwargs:
            r = Resource(cls.PATH + "/" + str(kwargs['region_id']))
        else:
            r = Resource(cls.PATH)

        if 'details' in kwargs:
            r.request_details = kwargs['details']
        else:
            r.request_details = 'basic'

        x = r.get()
        if r.last_error is None:
            if keys_only is True:
                return [i[camelize(cls.PRIMARY_KEY)] for i in x[cls.COLLECTION_NAME]]
            else:
                return [type(cls.__name__, (object,), i) for i in uncamel_keys(x)[cls.COLLECTION_NAME]]
        else:
            raise SubscriptionException(r.last_error)


class SubscriptionException(BaseException):
    pass
