from mixcoatl.resource import Resource
from mixcoatl.decorators.lazy import lazy_property
from mixcoatl.utils import camelize

class LoadBalancer(Resource):
    PATH = 'network/LoadBalancer'
    COLLECTION_NAME = 'loadBalancers'
    PRIMARY_KEY = 'load_balancer_id'

    def __init__(self, load_balancer_id=None, *args, **kwargs):
        Resource.__init__(self)
        self.__load_balancer_id = load_balancer_id

    @property
    def load_balancer_id(self):
        return self.__load_balancer_id

    @lazy_property
    def customer(self):
        return self.__customer

    @lazy_property
    def status(self):
        return self.__status

    @lazy_property
    def provider_id(self):
        return self.__provider_id

    @lazy_property
    def description(self):
        return self.__description

    @lazy_property
    def region(self):
        return self.__region

    @lazy_property
    def budget(self):
        return self.__budget

    @lazy_property
    def owning_groups(self):
        return self.__owning_groups

    @lazy_property
    def cname_based(self):
        return self.__cname_based

    @lazy_property
    def address(self):
        return self.__address

    @lazy_property
    def owning_account(self):
        return self.__owning_account

    @lazy_property
    def owning_user(self):
        return self.__owning_user

    @lazy_property
    def cloud(self):
        return self.__cloud

    @lazy_property
    def name(self):
        return self.__name

    @lazy_property
    def data_centers(self):
        return self.__data_centers

    @lazy_property
    def servers(self):
        return self.__servers

    @lazy_property
    def listeners(self):
        return self.__listeners


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
