from mixcoatl.resource import Resource
from mixcoatl.decorators.lazy import lazy_property
from mixcoatl.utils import camelize

class Service(Resource):
    PATH = 'automation/Service'
    COLLECTION_NAME = 'services'
    PRIMARY_KEY = 'service_id'

    def __init__(self, service_id=None, *args, **kwargs):
        Resource.__init__(self)
        self.__service_id = service_id

    @property
    def service_id(self):
        return self.__service_id

    @lazy_property
    def backup_interval_in_minutes(self):
        return self.__backup_interval_in_minutes

    @lazy_property
    def budget(self):
        return self.__budget

    @lazy_property
    def description(self):
        return self.__description

    @lazy_property
    def name(self):
        return self.__name

    @lazy_property
    def owning_group(self):
        return self.__owning_group

    @lazy_property
    def owning_user(self):
        return self.__owning_user

    @lazy_property
    def run_as_user(self):
        return self.__run_as_user

    @lazy_property
    def scaling_model(self):
        return self.__scaling_model

    @lazy_property
    def status(self):
        return self.__status

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
