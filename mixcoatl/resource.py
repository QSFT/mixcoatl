"""
mixcoatl.resource
------------------
"""
import os
import requests as r
import mixcoatl.auth as auth
from mixcoatl.settings.load_settings import settings
from mixcoatl.decorators.lazy import lazy_property
from mixcoatl.utils import camel_keys


class Resource(object):

    """The base class for all resources returned from an DCM API call
    By default all resources are largely represented as a `dict`-alike object
    that mirrors the JSON response from the DCM API with keys converted
    from camel-case to snake-case.

    For instance:

        * The DCM API JSON for a resource looks something like this:

            .. code-block:: yaml

                {
                  'someId':1,
                  'name':'my-name',
                  'cloud':{'cloudId':12345}
                }

        * All keys (nested or top-level) will be converted to snake-case:
            - `someId` becomes `some_id`
            - `cloudId` becomes `cloud_id`
        * The top-level keys will be converted to getters (and in some cases - setters) on the Resource.
            - `some_id` will now be the resource's primary identifier: `resource.some_id`
            - `name` will likely be a getter and a setter as `name` is usually a mutable attributes
            - `cloud` will be converted to a setter with a value of `{'cloud_id':123345}`
        * In cases where a setter would actually need to set a nested value, it will do so. However
            the getter will still return the original data structure as appropriate

        .. warning::

            The Resource object, while looking much like a `dict`, is not a `dict` proper.
            If you need an actual `dict`, call `to_dict()` on your instance.
    """

    #: The base request path of the resource
    PATH = None
    #: The top-level grouping of a resource in the API response
    COLLECTION_NAME = None
    #: The unique identifier of an individual resource
    PRIMARY_KEY = None

    def __init__(self, base_path=None, request_details='basic', **kwargs):
        if base_path is None:
            try:
                self.__path = self.__class__.PATH
            except:
                raise AttributeError('you must override base_path')
        else:
            self.__path = base_path

        if 'request_details' in kwargs:
            self.__request_details = kwargs['request_details']
            del kwargs['request_details']
        else:
            self.__request_details = 'basic'

        if 'params' in kwargs:
            self.__params = kwargs['params']
        else:
            self.__params = {}

        self.__last_request = None
        self.__last_error = None
        self.__current_job = None
        self.__status_code = None
        self.__payload_format = 'json'
        self.__request_details = request_details
        self.pending_changes = {}

    def __props(self):
        """List of properties and lazy properties for a given resource"""
        p = [k for k, v in self.__class__.__dict__.items() if type(
            v) in [lazy_property, property]]
        rp = ['last_error', 'path', 'last_request',
              'current_job', 'request_details']
        return p + rp

    def __repr__(self):
        from mixcoatl.utils import convert
        d = {}
        for x in self.__props():
            try:
                if x == 'last_request':
                    d[x] = str(getattr(self, x))
                else:
                    d[x] = getattr(self, x)
            except AttributeError:
                d[x] = None
            except KeyError:
                d[x] = None
        return repr(convert(d))

    @property
    def status_code(self):
        return self.__status_code

    @property
    def request_details(self):
        """The level of detail used in the API call: `basic` or `extended`"""
        return self.__request_details

    @request_details.setter
    def request_details(self, level):
        self.__request_details = level

    @property
    def payload_format(self):
        """The format of the payload: `json` or `xml`"""
        return self.__payload_format

    @payload_format.setter
    def payload_format(self, p_format):
        self.__payload_format = p_format

    @property
    def path(self):
        """The path used in the API request (e.g. ``admin/Job``)"""
        return self.__path

    @path.setter
    def path(self, p):
        self.__path = p

    @property
    def last_request(self):
        """The :class:`Request` object of the most recent API call"""
        return self.__last_request

    @last_request.setter
    def last_request(self, lr):
        self.__last_request = lr

    @property
    def last_error(self):
        """The last error message, if any, returned from the most recent API call"""
        return self.__last_error

    @last_error.setter
    def last_error(self, le):
        self.__last_error = le

    @property
    def current_job(self):
        """The current :class:`Job`, if any, of an asynchronous API call"""
        return self.__current_job

    @current_job.setter
    def current_job(self, cj):
        self.__current_job = cj

    @property
    def params(self):
        return self.__params

    @params.setter
    def params(self, p):
        self.__params = p

    def load(self, **kwargs):
        """(Re)load the current object's attributes from an API call"""
        from mixcoatl.utils import uncamel_keys
        reserved_words = ['type']
        p = self.PATH + "/" + str(getattr(self, self.__class__.PRIMARY_KEY))

        if 'params' in kwargs:
            params = kwargs['params']
        else:
            params = camel_keys(self.params)

        s = self.get(p, params=params)
        if self.last_error is None:
            scope = uncamel_keys(s[self.__class__.COLLECTION_NAME][0])
            for k in scope.keys():
                if k in reserved_words:
                    the_key = 'e_' + k
                else:
                    the_key = k
                nk = '_%s__%s' % (self.__class__.__name__, the_key)
                if the_key not in self.__props():
                    raise AttributeError('Key found without accessor: %s' % k)
                else:
                    setattr(self, nk, scope[k])
                    self.loaded = True
        else:
            return self.last_error

    def __doreq(self, method, **kwargs):
        """Performs the actual API call

        * calls `auth.get_sig` for signed headers
        * issues the requested :attr:`method` against the API endpoint
        * Handles requests appropriately based on sync/async nature of the call
            based on DCM API documentation
        """
        failures = [400, 403, 404, 409, 500, 501, 503]
        sig = auth.get_sig(method, self.path)
        url = settings.endpoint + '/' + self.path
        ssl_verify = settings.ssl_verify

        if self.payload_format == 'xml':
            payload_format = 'application/xml'
        elif self.payload_format == 'json':
            payload_format = 'application/json'
        else:
            raise AttributeError(
                'Wrong payload format: %s' % self.payload_format)

        headers = {'x-esauth-access': sig['access_key'],
                   'x-esauth-timestamp': str(sig['timestamp']),
                   'x-esauth-signature': str(sig['signature']),
                   'x-es-details': self.request_details,
                   'Accept': payload_format,
                   'User-Agent': sig['ua']}

        results = r.request(
            method, url, headers=headers, verify=ssl_verify, **kwargs)

        if 'DCM_DEBUG' in os.environ:
            print "URL: %s" % (url)
            print "method: %s" % (method)
            for key, value in kwargs.iteritems():
                print "%s = %s" % (key, value)
            for key, value in results.headers.iteritems():
                print "headers: %s = %s" % (key, value)

        self.last_error = None
        self.last_request = results
        self.__status_code = results.status_code

        if self.payload_format == 'xml':
            return results

        if results.status_code in failures:
            try:
                err = results.json()
                self.last_error = err['error']['message']
            except ValueError:
                self.last_error = results.content
            return self.last_error

        if method == 'GET':
            try:
                results.raise_for_status()
                self.last_error = None
                return results.json()
            except r.exceptions.HTTPError:
                try:
                    err = results.json()
                    self.last_error = err['error']['message']
                except ValueError:
                    self.last_error = results.content
                return False
        if method == 'DELETE':
            if results.status_code == 202:
                self.current_job = results.json()['jobs'][0]['jobId']
                return results.json()
            elif results.status_code != 204:
                try:
                    err = results.json()
                    self.last_error = err['error']['message']
                except ValueError:
                    self.last_error = results.content
                return False
            else:
                return True
        if method == 'PUT':
            if results.status_code == 202:
                self.current_job = results.json()['jobs'][0]['jobId']
                return results.json()
            elif results.status_code == 204:
                return True
            else:
                try:
                    err = results.json()
                    self.last_error = err['error']['message']
                except ValueError:
                    self.last_error = results.content
                return False
        if method == 'POST':
            if results.status_code in [201, 202]:
                if results.status_code == 202:
                    self.current_job = results.json()['jobs'][0]['jobId']
                return results.json()
            else:
                try:
                    err = results.json()
                    self.last_error = err['error']['message']
                except ValueError:
                    self.last_error = results.content
                return False
        if method == 'HEAD':
            if results.status_code in [200]:
                try:
                    err = results.json()
                    self.last_error = err['error']['message']
                except ValueError:
                    self.last_error = results.content
                return False

    def set_path(self, path=None):
        if path is not None:
            self.path = path

    def get(self, path=None, **kwargs):
        """Perform an HTTP `GET` against the API endpoint for the current resource"""
        self.set_path(path)
        return self.__doreq('GET', **kwargs)

    def post(self, path=None, **kwargs):
        """Perform an HTTP `POST` against the API endpoint for the current resource"""
        self.set_path(path)
        return self.__doreq('POST', **kwargs)

    def put(self, path=None, **kwargs):
        """Perform an HTTP `PUT` against the API endpoint for the current resource"""
        self.set_path(path)
        return self.__doreq('PUT', **kwargs)

    def head(self, path=None, **kwargs):
        """Perform an HTTP `HEAD` against the API endpoint for the current resource"""
        self.set_path(path)
        return self.__doreq('HEAD', **kwargs)

    def delete(self, path=None, **kwargs):
        """Perform an HTTP `DELETE` against the API endpoint for the current resource"""
        self.set_path(path)
        return self.__doreq('DELETE', **kwargs)

    def pprint(self):
        """The prettyprint formatted representation of the current resource"""
        import pprint
        pprint.pprint(eval(repr(self)))

    def to_dict(self):
        """The `dict` representation of the current resource"""
        return eval(repr(self))

    def track_change(self, var, prev, new):
        if prev == new:
            pass
        else:
            self.pending_changes[var] = {'old': prev, 'new': new}
