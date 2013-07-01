from mixcoatl.resource import Resource
from mixcoatl.decorators.lazy import lazy_property
from mixcoatl.utils import camelize

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

    @lazy_property
    def owning_groups(self):
        return self.__owning_groups

    @lazy_property
    def owning_user(self):
        return self.__owning_user

    @lazy_property
    def regions(self):
        return self.__regions

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
