"""
mixcoatl.admin.customer
--------------------
"""
from mixcoatl.resource import Resource
from mixcoatl.decorators.lazy import lazy_property
from mixcoatl.decorators.validations import required_attrs
from mixcoatl.utils import camelize, camel_keys, uncamel_keys
import json


class Customer(Resource):

    """The customer resource represents the overarching Dell Cloud Manager customer account. A
    customer may have any number of actual accounts associated with them. Each account is
    billed separately, but share customer-wide resources like users, billing codes, standard networks,
    standard ports, and more."""
    PATH = 'admin/Customer'
    COLLECTION_NAME = 'customers'
    PRIMARY_KEY = 'customer_id'

    def __init__(self, role_id=None, *args, **kwargs):
        Resource.__init__(self)
        self.__customer_id = customer_id

    @property
    def customer_id(self):
        """`int` - The unique id of the customer"""
        return self.__customer_id

    @classmethod
    def all(cls, keys_only=False, **kwargs):
        """Get all customers"""
        r = Resource(cls.PATH)
        params = {}

        if 'detail' in kwargs:
            r.request_details = kwargs['detail']
        else:
            r.request_details = 'basic'

        if 'customer_id' in kwargs:
            params['customer_id'] = kwargs['customer_id']

        x = r.get(params=params)
        if r.last_error is None:
            if keys_only is True:
                return [i[camelize(cls.PRIMARY_KEY)] for i in x[cls.COLLECTION_NAME]]
            else:
                return [type(cls.__name__, (object,), i) for i in uncamel_keys(x)[cls.COLLECTION_NAME]]
        else:
            raise CustomerException(r.last_error)


class CustomerException(BaseException):
    pass
