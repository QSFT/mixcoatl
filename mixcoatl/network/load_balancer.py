from mixcoatl.resource import Resource
from mixcoatl.decorators.lazy import lazy_property
from mixcoatl.utils import uncamel, camelize, camel_keys, uncamel_keys


class LoadBalancer(Resource):

    """ A load balancer is a virtual load balancer such as an AWS Elastic Load Balancer. It is specifically
    not a VM-hosted load balancer. Load balancers vary wildly from cloud provider to cloud
    provider. As a result, you should check with your cloud meta-data to see what elements are
    necessary in order to create a load balancer. """
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
            raise LoadBalancerException(r.last_error)


class LoadBalancerException(BaseException):
    pass
