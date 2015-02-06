"""
mixcoatl.admin.billing_code
---------------------------

Implements access to the DCM Billingcode API
"""
from mixcoatl.resource import Resource
from mixcoatl.decorators.lazy import lazy_property
from mixcoatl.decorators.validations import required_attrs
from mixcoatl.utils import uncamel, camelize, camel_keys, uncamel_keys
import json


class BillingCode(Resource):

    """A billing code is a budget item with optional hard and soft quotas
    against which cloud resources may be provisioned and tracked."""
    PATH = 'admin/BillingCode'
    COLLECTION_NAME = 'billingCodes'
    PRIMARY_KEY = 'billing_code_id'

    def __init__(self, billing_code_id=None, *args, **kwargs):
        Resource.__init__(self)
        self.__billing_code_id = billing_code_id

    @property
    def billing_code_id(self):
        """`int` - The unique id of this billing code"""
        return self.__billing_code_id

    @lazy_property
    def budget_state(self):
        """`str` - The ability of users to provision against this budget"""
        return self.__budget_state

    @lazy_property
    def current_usage(self):
        """`dict` - The month-to-data usage across all clouds for this code"""
        return self.__current_usage

    @lazy_property
    def customer(self):
        """`dict` - The customer to whom this code belongs"""
        return self.__customer

    @lazy_property
    def description(self):
        """`str` - User-friendly description of this code"""
        return self.__description

    @description.setter
    def description(self, d):
        self.__description = d

    @lazy_property
    def finance_code(self):
        """`str` - The alphanumeric identifier of this billing code"""
        return self.__finance_code

    @finance_code.setter
    def finance_code(self, f):
        self.__finance_code = f

    @lazy_property
    def name(self):
        """`str` - User-friendly name for this billing code"""
        return self.__name

    @name.setter
    def name(self, n):
        self.__name = n

    @lazy_property
    def projected_usage(self):
        """`dict` - Estimated end-of-month total to be charged against this budget"""
        return self.__projected_usage

    @lazy_property
    def status(self):
        """`str` - The status of this billing code"""
        return self.__status

    @lazy_property
    def hard_quota(self):
        """`dict` - Cutoff point where no further resources can be billed to this code"""
        return self.__hard_quota

    @hard_quota.setter
    def hard_quota(self, h):
        self.__hard_quota = h

    @lazy_property
    def soft_quota(self):
        """`dict` - Point where budget alerts will be triggered for this billing code"""
        return self.__soft_quota

    @soft_quota.setter
    def soft_quota(self, s):
        self.__soft_quota = s

    @classmethod
    def all(cls, keys_only=False, **kwargs):
        """Get all visible billing codes

        .. note::

            The keys used to make the original request determine result visibility

        :param keys_only: Only return :attr:`billing_code_id` instead of :class:`BillingCode` objects
        :type keys_only: bool.
        :param detail: The level of detail to return - `basic` or `extended`
        :type detail: str.
        :returns: `list` - of :class:`BillingCode` or :attr:`billing_code_id`
        :raises: :class:`BillingCodeException`
        """
        r = Resource(cls.PATH)
        params = {}

        if 'details' in kwargs:
            r.request_details = kwargs['details']
        else:
            r.request_details = 'basic'

        x = r.get()
        if r.last_error is None:
            if keys_only is True:
                return [i[camelize(cls.PRIMARY_KEY)] for i in x[cls.COLLECTION_NAME]]
            else:
                return [type(cls.__name__, (object,), i) for i in uncamel_keys(x)[uncamel(cls.COLLECTION_NAME)]]
        else:
            raise BillingCodeException(r.last_error)

    @required_attrs(['soft_quota', 'hard_quota', 'name', 'finance_code', 'description'])
    def add(self):
        """Add a new billing code. """
        payload = {"addBillingCode": [{
            "softQuota": {"value": self.soft_quota, "currency": "USD"},
            "hardQuota": {"value": self.hard_quota, "currency": "USD"},
            "status": "ACTIVE",
            "name": self.name,
            "financeCode": self.finance_code,
            "description": self.description}]}
        response = self.post(data=json.dumps(payload))
        if self.last_error is None:
            return response
        else:
            raise BillingCodeAddException(self.last_error)

    @required_attrs(['billing_code_id'])
    def destroy(self, reason, replacement_code):
        """Destroy billing code with a specified reason :attr:`reason`

        :param reason: The reason of destroying the billing code.
        :type reason: str.
        :param replacement_code: The replacement code.
        :type replacement_code: int.
        :returns: bool -- Result of API call
        """
        p = self.PATH + "/" + str(self.billing_code_id)
        qopts = {'reason': reason, 'replacementCode': replacement_code}
        self.delete(p, params=qopts)
        if self.last_error is None:
            return True
        else:
            raise BillingCodeDestroyException(self.last_error)


class BillingCodeException(BaseException):
    pass


class BillingCodeAddException(BillingCodeException):
    pass


class BillingCodeDestroyException(BillingCodeException):
    pass
