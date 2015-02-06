"""Implements the DCM Group API"""
from mixcoatl.resource import Resource
from mixcoatl.decorators.lazy import lazy_property
from mixcoatl.decorators.validations import required_attrs
from mixcoatl.utils import camelize, camel_keys, uncamel_keys
from mixcoatl.infrastructure.snapshot import Snapshot
from mixcoatl.infrastructure.snapshot import SnapshotException
from mixcoatl.admin.job import Job
import json
import time


class Group(Resource):

    """A group is a collection of users. Groups map to roles that define what their access rights are for
    a specific account. Some operations may not be possible if your groups are being managed in
    LDAP or ActiveDirectory as Dell Cloud Manager is not the authority for that data in those
    instances. """
    PATH = 'admin/Group'
    COLLECTION_NAME = 'groups'
    PRIMARY_KEY = 'group_id'

    def __init__(self, group_id=None, *args, **kwargs):
        Resource.__init__(self)
        self.__group_id = group_id

    @property
    def group_id(self):
        """`int` - The unique id of this group in DCM"""
        return self.__group_id

    @lazy_property
    def description(self):
        """`str` - The user-friendly description of this group"""
        return self.__description

    @description.setter
    def description(self, b):
        # pylint: disable-msg=C0111,W0201
        self.__description = b

    @lazy_property
    def name(self):
        """`str` - The name of the group"""
        return self.__name

    @name.setter
    def name(self, b):
        # pylint: disable-msg=C0111,W0201
        self.__name = b

    @lazy_property
    def status(self):
        """`str` - The current status of the group in DCM"""
        return self.__status

    @lazy_property
    def customer(self):
        """`dict` - The customer to who this group belongs."""
        return self.__customer

    @lazy_property
    def customer_admin(self):
        """`bool` """
        return self.__customer_admin

    @lazy_property
    def user_admin(self):
        """`bool` """
        return self.__user_admin

    @lazy_property
    def configuration_management_admin(self):
        """`bool` """
        return self.__configuration_management_admin

    @lazy_property
    def configuration_management_qualifier(self):
        """`bool` """
        return self.__configuration_management_qualifier

    @lazy_property
    def group_account_budget_codes(self):
        """`list` """
        return self.__group_account_budget_codes

    @lazy_property
    def role_assignments(self):
        """`list` """
        return self.__role_assignments

    @classmethod
    def all(cls, keys_only=False, **kwargs):
        """Get all groups

        .. note::

            The keys used to make the request determine results visibility

        :param keys_only: Only return `group_id` instead of `Group` objects
        :type keys_only: bool.
        :param detail: The level of detail to return - `basic` or `extended`
        :type detail: str.
        :param account_id: Restrict results to `account_id`
        :type account_id: int.
        :returns: `list` - List of :class:`Group` or :attr:`group_id`
        :raises: :class:`GroupException`
        """
        r = Resource(cls.PATH)
        params = {}

        if 'detail' in kwargs:
            r.request_details = kwargs['detail']
        else:
            r.request_details = 'basic'

        if 'account_id' in kwargs:
            params = {'accountId': kwargs['account_id']}

        x = r.get(params=params)
        if r.last_error is None:
            if keys_only is True:
                return [i[camelize(cls.PRIMARY_KEY)]
                        for i in x[cls.COLLECTION_NAME]]
            else:
                return [type(cls.__name__, (object,), i)
                        for i in uncamel_keys(x)[cls.COLLECTION_NAME]]
        else:
            raise GroupException(r.last_error)

    @required_attrs(['group_id'])
    def set_role(self, role_id, account_id):
        """Updates the role applied to the group specified by group_id.
           account_id is technically optional, but we're making it required
           here because making it optional may result in user problems.

           It's complicated.

           If you don't specify an account then it'll find an account associated with the billing
           credentials for the given user."""

        p = '%s/%s' % (self.PATH, str(self.group_id))
        payload = {'setRole': {
            'group': {'role': {'roleId': role_id}, 'account': {'accountId': account_id}}}}

        return self.put(p, data=json.dumps(payload))

    @required_attrs(['group_id', 'name', 'description'])
    def update(self, name, description):
        """Updates the group name and description."""
        p = '%s/%s' % (self.PATH, str(self.group_id))
        payload = {'describeGroup': {
            'group': {'name': str(name), 'description': str(description)}}}

        return self.put(p, data=json.dumps(payload))

    @required_attrs(['group_id', 'name'])
    def update_name(self, name):
        """Updates the group name. An update to one parameter requires both arguments."""
        p = '%s/%s' % (self.PATH, str(self.group_id))
        payload = {'describeGroup': {
            'group': {'name': str(name), 'description': self.description}}}

        return self.put(p, data=json.dumps(payload))

    @required_attrs(['group_id', 'description'])
    def update_description(self, description):
        """Updates the group description. An update to one parameter requires both arguments."""
        p = '%s/%s' % (self.PATH, str(self.group_id))
        payload = {'describeGroup': {
            'group': {'name': self.name, 'description': str(description)}}}

        return self.put(p, data=json.dumps(payload))

    @required_attrs(['name', 'description'])
    def create(self, callback=None):
        """Creates a new group

        :param callback: Optional callback to send the resulting :class:`Job`
        :raises: :class:`GroupCreationException`
        """
        parms = {'group': {'name': self.name,
                           'description': self.description}}
        payload = {'addGroup': camel_keys(parms)}

        response = self.post(data=json.dumps(payload))
        if self.last_error is None:
            self.load()
            return response
        else:
            raise GroupCreationException(self.last_error)


class GroupException(BaseException):
    pass


class GroupCreationException(GroupException):

    """Group Creation Exception"""
    pass
