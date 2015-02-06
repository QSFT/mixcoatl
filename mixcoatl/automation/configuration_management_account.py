from mixcoatl.resource import Resource
from mixcoatl.decorators.lazy import lazy_property
from mixcoatl.utils import uncamel, camelize, camel_keys, uncamel_keys


class ConfigurationManagementAccount(Resource):

    """ A configuration management account is an account with a configuration management service.
    A typical Dell Cloud Manager installation will have any number of configuration management
    services for different configuration management systems (Chef, Puppet, etc.) installed."""
    PATH = 'automation/ConfigurationManagementAccount'
    COLLECTION_NAME = 'cmAccounts'
    PRIMARY_KEY = 'cm_account_id'

    def __init__(self, cm_account_id=None, *args, **kwargs):
        Resource.__init__(self)
        self.__cm_account_id = cm_account_id

    @property
    def cm_account_id(self):
        return self.__cm_account_id

    @lazy_property
    def account_number(self):
        return self.__account_number

    @lazy_property
    def budget(self):
        return self.__budget

    @lazy_property
    def cm_service(self):
        return self.__cm_service

    @lazy_property
    def created_timestamp(self):
        return self.__created_timestamp

    @lazy_property
    def description(self):
        return self.__description

    @lazy_property
    def guid(self):
        return self.__guid

    @lazy_property
    def last_modified_timestamp(self):
        return self.__last_modified_timestamp

    @lazy_property
    def name(self):
        return self.__name

    @lazy_property
    def removable(self):
        return self.__removable

    @lazy_property
    def status(self):
        return self.__status

    @lazy_property
    def customer(self):
        return self.__customer

    @lazy_property
    def label(self):
        return self.__label

    @lazy_property
    def owning_groups(self):
        return self.__owning_groups

    @lazy_property
    def owning_user(self):
        return self.__owning_user

    @classmethod
    def all(cls, **kwargs):
        r = Resource(cls.PATH)
        if 'details' in kwargs:
            r.request_details = kwargs['details']
        else:
            r.request_details = 'basic'

        if 'keys_only' in kwargs:
            keys_only = kwargs['keys_only']
        else:
            keys_only = False

        x = r.get()
        if r.last_error is None:
            if keys_only is True:
                return [i[camelize(cls.PRIMARY_KEY)] for i in x[cls.COLLECTION_NAME]]
            else:
                return [type(cls.__name__, (object,), i) for i in uncamel_keys(x)[uncamel(cls.COLLECTION_NAME)]]
        else:
            raise ConfigurationManagementAccountException(r.last_error)


class ConfigurationManagementAccountException(BaseException):
    pass
