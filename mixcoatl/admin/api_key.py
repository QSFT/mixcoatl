"""
mixcoatl.admin.api_key
----------------------

Implements access to the DCM ApiKey API
"""
from mixcoatl.resource import Resource
from mixcoatl.decorators.lazy import lazy_property
from mixcoatl.decorators.validations import required_attrs
from mixcoatl.utils import uncamel, camelize, camel_keys, uncamel_keys
import json


class ApiKey(Resource):

    """An API key is an access key and secret key that provide API access into DCM."""
    PATH = 'admin/ApiKey'
    COLLECTION_NAME = 'apiKeys'
    PRIMARY_KEY = 'access_key'

    def __init__(self, access_key=None, *args, **kwargs):
        Resource.__init__(self)
        self.__access_key = access_key

    @property
    def access_key(self):
        """The primary identifier of the `ApiKey`. Same as `DCM_ACCESS_KEY`"""
        return self.__access_key

    @lazy_property
    def account(self):
        """`dict` - The account with which this API key is associated."""
        return self.__account

    @lazy_property
    def activation(self):
        """`str` - The date and time when this key was activated."""
        return self.__activation

    @lazy_property
    def expiration(self):
        """`str` - The date and time when this API key should automatically be made inactivate."""
        return self.__expiration

    @expiration.setter
    def expiration(self, e):
        self.__expiration = e

    @lazy_property
    def customer(self):
        """`dict` - The customer to whom this API key belongs."""
        return self.__customer

    @lazy_property
    def customer_management_key(self):
        """`bool` - Identifies whether or not this key can be used across all customer accounts."""
        return self.__customer_management_key

    @lazy_property
    def description(self):
        """`str` - A user-friendly description of this API key."""
        return self.__description

    @description.setter
    def description(self, d):
        self.__description = d

    @lazy_property
    def name(self):
        """`str` - The user-friendly name used to identify the key."""
        return self.__name

    @name.setter
    def name(self, n):
        self.__name = n

    @lazy_property
    def secret_key(self):
        """`str` - The secret part of this API key."""
        return self.__secret_key

    @lazy_property
    def state(self):
        """`str` - The status of the key *(i.e. `ACTIVE`)*"""
        return self.__state

    @lazy_property
    def system_management_key(self):
        """`bool` - Identifies if the key can be used for DCM system management functions"""
        return self.__system_management_key

    @lazy_property
    def user(self):
        """`dict` - The user associated with this API key. Account-level keys return `{'user_id': -1}`"""
        return self.__user

    @required_attrs(['description', 'name'])
    def create(self):
        """Call the API to generate an API key from the current instance of `ApiKey`"""

        payload = {
            'generateApiKey': [{'description': self.description, 'name': self.name}]}
        s = self.post(data=json.dumps(payload))
        if self.last_error is None:
            self.__access_key = s['apiKeys'][0]['accessKey']
            self.load()
        else:
            raise ApiKeyGenerationException(self.last_error)

    def invalidate(self, reason='key deleted via mixcoatl'):
        """Call the API to invalidate the current instance of `ApiKey`
        This is the same as deleting the api key

        :param reason: the reason for invalidating the key
        :type reason: str.
        :returns: True
        :raises: :class:`ApiKeyInvalidationException`
        """
        params = {'reason': reason}
        self.delete(params=params)
        if self.last_error is None:
            return True
        else:
            raise ApiKeyInvalidationException(self.last_error)

    @classmethod
    def generate_api_key(cls, key_name, description, expiration=None):
        """Generates a new API key

        >>> ApiKey.generate_api_key('my-api-key', 'this is my api key')
        {'access_key':'ABCDEFGHIJKL':....}

        :param key_name: the name for the key
        :type key_name: str.
        :param description: the description for the key
        :type description: str.
        :param expiration: *unused for now*
        :type expiration: str.
        :returns: :class:`ApiKey`
        :raises: :class:`ApiKeyGenerationException`
        """

        a = cls()
        a.name = key_name
        a.description = description
        a.create()
        return a

    @classmethod
    def all(cls, keys_only=False, **kwargs):
        """Get all api keys

        .. note::

            The keys used to make the request determine results visibility

        :param keys_only: Only return `access_key` instead of `ApiKey` objects
        :type keys_only: bool.
        :param detail: The level of detail to return - `basic` or `extended`
        :type detail: str.
        :param account_id: Display all system keys belonging to `account_id`
        :type account_id: int.
        :param user_id: Display all keys belonging to `user_id`
        :type user_id: int.
        :returns: `list` - of :class:`ApiKey` or :attr:`access_key`
        """

        if 'access_key' in kwargs:
            r = Resource(cls.PATH + "/" + kwargs['access_key'])
            params = {}
        else:
            r = Resource(cls.PATH)

            if 'detail' in kwargs:
                r.request_details = kwargs['detail']
            else:
                r.request_details = 'basic'

            if 'account_id' in kwargs:
                params = {'accountId': kwargs['account_id']}
            elif 'user_id' in kwargs:
                params = {'userId': kwargs['user_id']}
            else:
                params = {}

        x = r.get(params=params)
        if r.last_error is None:
            if keys_only is True:
                return [i[camelize(cls.PRIMARY_KEY)]
                        for i in x[cls.COLLECTION_NAME]]
            else:
                return [type(cls.__name__, (object,), i)
                        for i in uncamel_keys(x)[uncamel(cls.COLLECTION_NAME)]]
        else:
            raise ApiKeyException(r.last_error)


class ApiKeyException(BaseException):
    pass


class ApiKeyGenerationException(ApiKeyException):
    pass


class ApiKeyInvalidationException(ApiKeyException):
    pass
