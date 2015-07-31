"""
mixcoatl.admin.license
---------------------------

Implements access to the DCM License API
"""
from mixcoatl.resource import Resource
from mixcoatl.decorators.lazy import lazy_property
from mixcoatl.decorators.validations import required_attrs
from mixcoatl.utils import uncamel, camelize, camel_keys, uncamel_keys
import json


class License(Resource):
    """License object encapsulates data about DCM Licensing. This information can only be pulled from the DCM API not
    written to it. Note that this class is different from many of the Resource sub classes in that it does not have a
    PRIMARY_KEY since there can be only one License per DCM instance.
    """

    PATH = 'admin/License'
    COLLECTION_NAME = 'license'

    def __init__(self, endpoint=None):
        Resource.__init__(self, endpoint=endpoint)

    @lazy_property
    def expiration_date_time(self):
        """The DCM expiration date and time in format 2015-06-24T00:49:25.757+0000"""
        return self.__expiration_date_time

    @lazy_property
    def days_until_expiration(self):
        """The Number of days until the DCM license expires"""
        return self.__days_until_expiration

    @lazy_property
    def licensee(self):
        """The DCM licensee"""
        return self.__licensee

    @lazy_property
    def server_limit(self):
        """The number of allowed servers with this license"""
        return self.__server_limit

    @lazy_property
    def valid(self):
        """Is the license presently valid"""
        return self.__valid

    def __props(self):
        """List of the names of DCM license properties"""
        return [k for k, v in self.__class__.__dict__.items() if type(
            v) in [lazy_property, property]]

    def prop_dict(self):
        """A dictionary of the DCM license properties"""
        thedict = {}
        for key in self.__props():
            thedict[key] = getattr(self, key)
        return thedict

    def to_json(self):
        """A json string of the DCM license properties"""
        return json.dumps(self.prop_dict(), indent=4, sort_keys=True)

    def load(self, **kwargs):
        """(Re)load the current object's attributes from an API call"""
        from mixcoatl.utils import uncamel_keys

        reserved_words = ['type']
        p = self.PATH

        if 'params' in kwargs:
            params = kwargs['params']
        else:
            params = camel_keys(self.params)

        s = self.get(p, params=params)
        if self.last_error is None:
            scope = uncamel_keys(s)
            for k in scope.keys():
                if k in reserved_words:
                    the_key = 'e_' + k
                else:
                    the_key = k
                nk = '_%s__%s' % (self.__class__.__name__, the_key)
                # nk = '__%s' %  the_key
                if the_key not in self._Resource__props():
                    self.add_property(k)
                setattr(self, nk, scope[k])
                self.loaded = True
        else:
            return self.last_error
