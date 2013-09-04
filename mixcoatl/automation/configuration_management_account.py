from mixcoatl.resource import Resource
from mixcoatl.decorators.lazy import lazy_property
from mixcoatl.utils import camelize

class ConfigurationManagementAccount(Resource):
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
        
    @classmethod
    def all(cls, **kwargs):
        r = Resource(cls.PATH)
        if 'details' in kwargs:
            r.request_details = kwargs['details']
        else:
            r.request_details = 'basic'

        x = r.get()
        if r.last_error is None:
            return [cls(i[camelize(cls.PRIMARY_KEY)]) for i in x[cls.COLLECTION_NAME]]
        else:
            return x.last_error
