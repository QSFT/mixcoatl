from mixcoatl.settings.load_settings import settings
import mixcoatl.auth as auth
import requests as r
from mixcoatl.decorators.lazy import lazy_property

class Resource(object):
    def __init__(self, base_path=None, request_details = 'extended'):
        if base_path is None:
            try:
                self.__path = self.__class__.path
            except:
                raise AttributeError('you must override base_path')
        else:
            self.__path = base_path
        self.__last_request = None
        self.__last_error = None
        self.__current_job = None
        self.__request_details = request_details
        self.pending_changes = {}

    def __props(self):
        p = [k for k,v in self.__class__.__dict__.items() if type(v) in [lazy_property, property]]
        rp = ['last_error', 'path', 'last_request', 'current_job']
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
    def request_details(self):
        return self.__request_details

    @request_details.setter
    def request_details(self, level):
        self.__request_details = level

    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, p):
        self.__path = p

    @property
    def last_request(self):
        return self.__last_request

    @last_request.setter
    def last_request(self, lr):
        self.__last_request = lr

    @property
    def last_error(self):
        return self.__last_error

    @last_error.setter
    def last_error(self, le):
        self.__last_error = le

    @property
    def current_job(self):
        return self.__current_job

    @current_job.setter
    def current_job(self, cj):
        self.__current_job = cj

    def load(self):
        from mixcoatl.utils import uncamel_keys
        reserved_words = ['type']
        p = self.path+"/"+str(getattr(self, self.__class__.primary_key))

        #self.request_details = 'extended'
        s = self.get(p)
        if self.last_error is None:
            scope = uncamel_keys(s[self.__class__.collection_name][0])
            for k in scope.keys():
                if k in reserved_words:
                    the_key = 'e_'+k
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

    def __doreq(self, method, *args, **kwargs):
        failures = [400, 403, 404, 409, 500, 501, 503]
        sig = auth.get_sig(method, self.path)
        url = settings.endpoint+'/'+self.path

        headers = {'x-esauth-access': sig['access_key'],
        'x-esauth-timestamp': str(sig['timestamp']),
        'x-esauth-signature': str(sig['signature']),
        'x-es-details': self.__request_details,
        'Accept': 'application/json',
        'User-Agent': sig['ua']}

        results = getattr(r, method.lower())(url, headers=headers, *args, **kwargs)

        self.last_error = None
        self.last_request = results
        if results.status_code in failures:
            self.last_error = results.json()
            return self.last_error

        if method == 'GET':
            try:
                results.raise_for_status()
                self.last_error = None
                return results.json()
            except r.exceptions.HTTPError:
                self.last_error = results.json()
                return False
        if method == 'DELETE':
            if results.status_code !=204:
                self.last_error = results.json()
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
                self.last_error = results.json()
                return self.last_error
        if method == 'POST':
            if results.status_code in [201,202]:
                if results.status_code == 202:
                    self.current_job = results.json()['jobs'][0]['jobId']
                return results.json()
            else:
                self.last_error = results.json()
                return False

    def set_path(self, path=None):
        if path is None:
            path = self.path
        else:
            self.path = path

    def get(self, path=None, *args, **kwargs):
        self.set_path(path)
        return self.__doreq('GET', *args, **kwargs)

    def post(self, path=None, *args, **kwargs):
        self.set_path(path)
        return self.__doreq('POST', *args, **kwargs)

    def put(self, path=None, *args, **kwargs):
        self.set_path(path)
        return self.__doreq('PUT', *args, **kwargs)

    def delete(self, path=None, *args, **kwargs):
        self.set_path(path)
        return self.__doreq('DELETE', *args, **kwargs)

    def pprint(self):
        import pprint
        pprint.pprint(eval(repr(self)))

    def to_dict(self):
        return eval(repr(self))

    def track_change(self, var, new_value):
        prev = getattr(self, var)
        self.pending_changes[var] = {'old': prev, 'new':new_value}
