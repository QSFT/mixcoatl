from mixcoatl.resource import Resource
from mixcoatl.decorators.lazy import lazy_property
from mixcoatl.decorators.validations import required_attrs
from mixcoatl.utils import uncamel, camelize, camel_keys, uncamel_keys
import json


class ConfigurationManagementService(Resource):

    """ A configuration management service is an actual service endpoint running a supported
    configuration management system. Some services like the public OpsCode Platform for Chef
    may be available to all customers, or you may define your own configuration management
    service for your companys private use. """
    PATH = 'automation/ConfigurationManagementService'
    COLLECTION_NAME = 'cmServices'
    PRIMARY_KEY = 'cm_system_id'

    def __init__(self, cm_account_id=None, *args, **kwargs):
        Resource.__init__(self)

    @lazy_property
    def cm_system(self):
        return self.__cm_system

    @lazy_property
    def service_endpoint(self):
        return self.__service_endpoint

    @lazy_property
    def properties(self):
        return self.__properties

    @lazy_property
    def cm_service_id(self):
        return self.__cm_service_id

    @lazy_property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, b):
        self.__budget = b

    @lazy_property
    def removable(self):
        return self.__removable

    @lazy_property
    def description(self):
        return self.__description

    @description.setter
    def description(self, b):
        self.__description = b

    @lazy_property
    def name(self):
        return self.__name

    @name.setter
    def name(self, b):
        self.__name = b

    @lazy_property
    def status(self):
        return self.__status

    @lazy_property
    def customer(self):
        return self.__customer

    @required_attrs(['budget', 'description', 'name', 'endpoint', 'cm_system_id'])
    def create(self):
        """Creates a new CM service."""
        parms = [{"budget": self.budget,
                  "serviceEndpoint": self.endpoint,
                  "description": self.description,
                  "name": self.name,
                  "label": "red",
                  "cmSystem": {"cmSystemID": self.cm_system_id}}]

        payload = {"addService": camel_keys(parms)}
        print json.dumps(payload)

        response = self.post(data=json.dumps(payload))
        if self.last_error is None:
            self.load()
            return response
        else:
            raise CMCreationException(self.last_error)

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
            raise CMException(r.last_error)


class CMException(BaseException):
    pass


class CMCreationException(CMException):

    """CM Creation Exception"""
    pass
