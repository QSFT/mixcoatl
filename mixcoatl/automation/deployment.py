"""Implements the enStratus Deployment API"""
from mixcoatl.resource import Resource
from mixcoatl.decorators.lazy import lazy_property
from mixcoatl.decorators.validations import required_attrs
from mixcoatl.utils import camelize, camel_keys
from mixcoatl.admin.job import Job

import json
import time

class Deployment(Resource):
    PATH = 'automation/Deployment'
    COLLECTION_NAME = 'deployments'
    PRIMARY_KEY = 'deployment_id'

    def __init__(self, deployment_id=None, *args, **kwargs):
        Resource.__init__(self)
        self.__deployment_id = deployment_id

    @property
    def deployment_id(self):
        return self.__deployment_id

    @lazy_property
    def backup_window(self):
        return self.__backup_window

    @lazy_property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, b):
        # pylint: disable-msg=C0111,W0201
        self.__budget = b

    @lazy_property
    def label(self):
        return self.__label

    @lazy_property
    def creation_timestamp(self):
        return self.__creation_timestamp

    @lazy_property
    def customer(self):
        return self.__customer

    @lazy_property
    def description(self):
        return self.__description

    @description.setter
    def description(self, d):
        # pylint: disable-msg=C0111,W0201
        self.__description = d

    @lazy_property
    def for_service_catalog(self):
        return self.__for_service_catalog

    @lazy_property
    def launch_timestamp(self):
        return self.__launch_timestamp

    @lazy_property
    def maintenance_window(self):
        return self.__maintenance_window

    @lazy_property
    def name(self):
        return self.__name

    @name.setter
    def name(self, n):
        # pylint: disable-msg=C0111,W0201
        self.__name = n

    @lazy_property
    def owning_groups(self):
        return self.__owning_groups

    @lazy_property
    def owning_user(self):
        return self.__owning_user

    @lazy_property
    def regions(self):
        return self.__regions

    @regions.setter
    def regions(self, r):
        # pylint: disable-msg=C0111,W0201
        self.__regions = r

    @lazy_property
    def removable(self):
        return self.__removable

    @lazy_property
    def load_balancers(self):
        return self.__load_balancers

    @lazy_property
    def reason_not_removable(self):
        return self.__reason_not_removable

    @lazy_property
    def status(self):
        return self.__status

    @lazy_property
    def e_type(self):
        return self.__e_type

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
            return r.last_error

    @required_attrs(['name', 'description','budget','region'])
    def create(self, callback=None):
        """Creates a new deployment

        :param callback: Optional callback to send the resulting :class:`Job`
        :raises: :class:`DeploymentCreationException`
        """

        parms = [{'budget': self.budget,
                    'regionId': self.region,
                    'description': self.description,
										'name': self.name}]


        payload = {'addDeployment':camel_keys(parms)}

        response=self.post(data=json.dumps(payload))
        if self.last_error is None:
            self.load()
            return response
        else:
            raise DeploymentCreationException(self.last_error)

class DeploymentException(BaseException): pass

class DeploymentCreationException(DeploymentException):
    """Deployment Creation Exception"""
    pass
