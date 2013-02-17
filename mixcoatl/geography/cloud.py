"""Implements the enStratus Cloud API"""
from mixcoatl.resource import Resource
from mixcoatl.decorators.lazy import lazy_property
from mixcoatl.utils import camelize

class Cloud(Resource):
    PATH = 'geography/Cloud'
    COLLECTION_NAME = 'clouds'
    PRIMARY_KEY = 'cloud_id'

    def __init__(self, cloud_id = None, *args, **kwargs):
        Resource.__init__(self)
        self.__cloud_id = cloud_id

    @property
    def cloud_id(self):
        """`int` - The unique enStratus id for this cloud"""
        return self.__cloud_id

    @lazy_property
    def cloud_provider_console_url(self):
        """`str` - URL of the cloud provider's own console"""
        return self.__cloud_provider_console_url

    @lazy_property
    def cloud_provider_logo_url(self):
        """`str` - enStratus installation URL to this cloud's logo"""
        return self.__cloud_provider_logo_url

    @lazy_property
    def cloud_provider_name(self):
        """`str` - The name of the vendor providing the cloud"""
        return self.__cloud_provider_name

    @lazy_property
    def compute_account_number_label(self):
        """`str` - enStratus localized label key for the cloud's user account number"""
        return self.__compute_account_number_label

    @lazy_property
    def compute_access_key_label(self):
        """`str` - enStratus localized label key for the cloud's API key"""
        return self.__compute_access_key_label

    @lazy_property
    def compute_x509_cert_label(self):
        """`str` - enStratus localized label key for the cloud's X509 certificate"""
        return self.__compute_x509_cert_label

    @lazy_property
    def compute_x509_key_label(self):
        """`str` - enStratus localized label key for the cloud's X509 key"""
        return self.__compute_x509_key_label

    @lazy_property
    def compute_delegate(self):
        """`str` - Dasein Cloud API Java class for interacting with this cloud"""
        return self.__compute_delegate

    @lazy_property
    def compute_endpoint(self):
        """`str` - Comma-separated list of cloud API endpoints"""
        return self.__compute_endpoint

    @lazy_property
    def compute_secret_key_label(self):
        """`str` - enStratus localized label key for the cloud's API secret key"""
        return self.__compute_secret_key_label

    @lazy_property
    def documentation_label(self):
        """`str` - enStratus localized label key"""
        return self.__documentation_label

    @lazy_property
    def name(self):
        """`str` - The enStratus name of the cloud"""
        return self.__name

    @lazy_property
    def private_cloud(self):
        """`bool` - If the cloud is a private cloud or not"""
        return self.__private_cloud

    @lazy_property
    def status(self):
        """`str` - Status of the cloud in enStratus"""
        return self.__status

    @classmethod
    def all(cls, keys_only=False, **kwargs):
        """Return all clouds

        :param keys_only: Return :attr:`cloud_id` instead of :class:`Cloud`
        :type keys_only: bool.
        :param detail: The level of detail to return - `basic` or `extended`
        :type detail: str.
        :returns: `list` of :class:`Cloud` or :attr:`cloud_id`
        """
        r = Resource(cls.PATH)
        r.request_details = 'basic'
        params = {}

        if 'public_only' in kwargs:
            params['publicOnly'] = kwargs['public_only']
        if 'status' in kwargs:
            params['status'] = kwargs['status']

        c = r.get(params=params)

        if r.last_error is None:
            if keys_only is True:
                return [i['cloudId'] for i in c[cls.COLLECTION_NAME]]
            else:
                clouds = []
                for i in c[cls.COLLECTION_NAME]:
                    cloud = cls(i['cloudId'])
                    if 'detail' in kwargs:
                        cloud.request_details = kwargs['detail']
                    cloud.params = params
                    cloud.load()
                    clouds.append(cloud)
                return clouds
        else:
            return r.last_error
