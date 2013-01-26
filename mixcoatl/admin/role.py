"""
mixcoatl.admin.role
--------------------

Implements access to the enStratus Role API

"""
from mixcoatl.resource import Resource
from mixcoatl.decorators.lazy import lazy_property

class Role(Resource):
    """A role defines a common set of permissions that govern access into a given account"""

    PATH = 'admin/Role'
    COLLECTION_NAME = 'roles'
    PRIMARY_KEY = 'role_id'

    def __init__(self, role_id=None, *args, **kwargs):
        Resource.__init__(self)
        self.__role_id = role_id

    @property
    def role_id(self):
        """`int` - The unique id of the role"""
        return self.__role_id

    @lazy_property
    def acl(self):
        """`dict` - The access permissions associated with the role"""
        return self.__acl

    @lazy_property
    def description(self):
        """`str` - A user-friendly description of the role"""
        return self.__description

    @lazy_property
    def customer(self):
        """`dict` - The customer to whom this role belongs"""
        return self.__customer

    @lazy_property
    def name(self):
        """`str` - The name of the role"""
        return self.__name

    @lazy_property
    def status(self):
        """`str` - The status of the role in enStratus"""
        return self.__status

    @classmethod
    def all(cls, keys_only = False, **kwargs):
        """Get all roles

        .. note::

            The keys used to make the request determine results visibility

        :param keys_only: Only return :attr:`role_id` instead of :class:`Group` objects
        :type keys_only: bool.
        :param detail: The level of detail to return - `basic` or `extended`
        :type detail: str.
        :param account_id: List roles with mappings to groups in the specified account
        :type account_id: int.
        :param group_id: Provides the role associated with the specified group
        :type group_id: int.
        :returns: `list` of :attr:`role_id` or :class:`Role`
        :raises: :class:`RoleException`
        """
        r = Resource(cls.PATH)
        params = {}
        if 'details' in kwargs:
            r.request_details = kwargs['details']
        else:
            r.request_details = 'basic'

        if 'account_id' in kwargs:
            params['account_id'] = kwargs['account_id']

        if 'group_id' in kwargs:
            params['group_id'] = kwargs['group_id']

        x = r.get(params=params)
        if r.last_error is None:
            if keys_only is True:
                return [i['roleId'] for i in x[cls.COLLECTION_NAME]]
            else:
                return [cls(i['roleId']) for i in x[cls.COLLECTION_NAME]]
        else:
            raise RoleException(r.last_error)

class RoleException(BaseException): pass
