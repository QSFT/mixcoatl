"""
mixcoatl.admin.account
----------------------

Implements access to the DCM Account API
"""
from mixcoatl.resource import Resource
from mixcoatl.decorators.lazy import lazy_property
from mixcoatl.decorators.validations import required_attrs
from mixcoatl.utils import camelize, camel_keys, uncamel_keys
import json


class Account(Resource):

    """An account object represents an DCM account held by an DCM customer."""
    PATH = 'admin/Account'
    COLLECTION_NAME = 'accounts'
    PRIMARY_KEY = 'account_id'

    def __init__(self, account_id=None, *args, **kwargs):
        Resource.__init__(self)
        self.__account_id = account_id

    @property
    def account_id(self):
        """`int` - The unique ID of this account"""
        return self.__account_id

    @lazy_property
    def alert_configuration(self):
        """`dict` - The configuration of alert preferences for this account."""
        return self.__alert_configuration

    @lazy_property
    def billing_system_id(self):
        """`int` - The ID that may appear on invoices."""
        return self.__billing_system_id

    @lazy_property
    def cloud_subscription(self):
        """`dict` or `None` -- Information about the cloud for this account"""
        return self.__cloud_subscription

    @lazy_property
    def cloud_subscription_id(self):
        """`int` -- Cloud subscription ID """
        return self.__cloud_subscription_id

    @lazy_property
    def configured(self):
        """`bool` - Has account has been tied to an account with a cloud"""
        return self.__configured

    @lazy_property
    def customer(self):
        """`dict` - The DCM customer record to which this account belongs"""
        return self.__customer

    @lazy_property
    def default_budget(self):
        """The billing id that is the default for discovered resources"""
        return self.__default_budget

    @lazy_property
    def dns_automation(self):
        """Does this account subscribe to dns_automation?"""
        return self.__dns_automation

    @lazy_property
    def name(self):
        """`str` - User-friendly name used to identify the account"""
        return self.__name

    @lazy_property
    def owner(self):
        """`dict` - user who owns this account"""
        return self.__owner

    @lazy_property
    def plan_id(self):
        """`int` - pricing plan associated with this account"""
        return self.__plan_id

    @lazy_property
    def provisioned(self):
        """`bool` - Is this account in goodstanding and managed by DCM"""
        return self.__provisioned

    @lazy_property
    def status(self):
        """`str` - The current account payment status"""
        return self.__status

    @lazy_property
    def subscribed(self):
        """`bool` - If the account is configured & working with DCM"""
        return self.__subscribed

    @lazy_property
    def account_name(self):
        return self.__account_name

    @account_name.setter
    def account_name(self, n):
        self.__account_name = n

    @lazy_property
    def account_number(self):
        return self.__account_number

    @account_number.setter
    def account_number(self, n):
        self.__account_number = n

    @lazy_property
    def api_key_id(self):
        return self.__api_key_id

    @api_key_id.setter
    def api_key_id(self, n):
        self.__api_key_id = n

    @lazy_property
    def api_key_secret(self):
        return self.__api_key_secret

    @api_key_secret.setter
    def api_key_secret(self, n):
        self.__api_key_secret = n

    @lazy_property
    def cloud_id(self):
        return self.__cloud_id

    @cloud_id.setter
    def cloud_id(self, n):
        self.__cloud_id = n

    @customer.setter
    def customer(self, n):
        self.__customer = n

    @required_attrs(['account_name', 'account_number', 'cloud_id', 'api_key_id', 'api_key_secret'])
    def add(self):
        payload = {'addAccount': [
            {
                'name': self.account_name,
                'cloudSubscription':
                {
                    'accountNumber': self.account_number,
                    'cloudId': int(self.cloud_id),
                    'apiKeyId': self.api_key_id,
                    'apiKeySecret': self.api_key_secret
                }
            }
        ]}

        if self.customer:
            payload['addAccount'].append({'customer': {'customerId': int(self.customer)}})

        response = self.post(self.PATH, data=json.dumps(payload))
        if self.last_error is None:
            return response
        else:
            raise CreateAccountException(self.last_error)

    @classmethod
    def all(cls, keys_only=False, **kwargs):
        """Get all accounts

        >>> Account.all(detail='basic')
        [{'account_id':12345,....}]

        >>> Account.all(keys_only=True)
        [12345]

        :param keys_only: Only return `account_id` instead of `Account` objects
        :type keys_only: bool.
        :param detail: The level of detail to return - `basic` or `extended`
        :type detail: str.
        :param cloud_id: Only show accounts tied to the given cloud
        :type cloud_id: int.
        :returns: `list` of :class:`Account` or :attr:`account_id`
        :raises: :class:`AccountException`
        """
        r = Resource(cls.PATH)
        params = {}

        if 'detail' in kwargs:
            r.request_details = kwargs['detail']
        else:
            r.request_details = 'basic'

        if 'cloud_id' in kwargs:
            params = {'cloudId': kwargs['cloud_id']}

        x = r.get(params=params)
        if r.last_error is None:
            if keys_only is True:
                return [i[camelize(cls.PRIMARY_KEY)]
                        for i in x[cls.COLLECTION_NAME]]
            else:
                return [type(cls.__name__, (object,), i)
                        for i in uncamel_keys(x)[cls.COLLECTION_NAME]]
        else:
            raise AccountException(r.last_error)

    def assign_cloud(self, cloud_id, account_number, api_key_id, api_key_secret):
        """ Associate this account with the cloud and supporting credentials specified.

        :param cloud_id: Cloud ID of the cloud that will be associated.
        :type cloud_id: int.
        :param account_number: Account number of the cloud credential.
        :type account_number: str.
        :param api_key_id: API access key of the cloud credential.
        :type api_key_id: str.
        :param api_key_secret: API secret key of the cloud credential.
        :type api_key_secret: str.
        :returns: cloud subscription ID.
        :raises: :class:`AssignCloudException`
        """

        p = "%s/%s" % (self.PATH, str(self.account_id))
        payload = {'assignCloud': {
            'accounts': {
                'cloudSubscription': {
                    'cloudId': cloud_id,
                    'accountNumber': account_number,
                    'apiKeyId': api_key_id,
                    'apiKeySecret': api_key_secret}}}}
        self.put(p, data=json.dumps(payload))
        if self.last_error is None:
            self.load()
            return self.cloud_subscription['cloud_subscription_id']
        else:
            raise AssignCloudException(self.last_error)


class AccountException(BaseException):
    pass


class AssignCloudException(AccountException):
    pass


class CreateAccountException(AccountException):
    pass
