"""Implements the enStratus Group API"""
from mixcoatl.resource import Resource
from mixcoatl.decorators.lazy import lazy_property
from mixcoatl.decorators.validations import required_attrs
from mixcoatl.utils import camelize, camel_keys
from mixcoatl.infrastructure.snapshot import Snapshot
from mixcoatl.infrastructure.snapshot import SnapshotException
from mixcoatl.admin.job import Job

import json
import time

class Group(Resource):
    PATH = 'admin/Group'
    COLLECTION_NAME = 'groups'
    PRIMARY_KEY = 'group_id'

    def __init__(self, group_id=None, *args, **kwargs):
        Resource.__init__(self)
        self.__group_id = group_id

    @property
    def group_id(self):
        """`int` - The unique id of this group in enStratus"""
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
        """`str` - The current status of the group in enStratus"""
        return self.__status

    @lazy_property
    def customer(self):
        """`dict` - The customer to who this group belongs."""
        return self.__customer

    @classmethod
    def all(cls, keys_only=False, **kwargs):
        """Get all groups

        .. note::

            The keys used to make the request determine results visibility

        :param keys_only: Only return `group_id` instead of `Group` objects
        :type keys_only: bool.
        :param detail: The level of detail to return - `basic` or `extended`
        :type detail: bool.
        :param account_id: Restrict results to `account_id`
        :type account_id: int.
        :returns: `list` - List of :class:`Group` or :attr:`group_id`
        :raises: :class:`GroupException`
        """
        r = Resource(cls.PATH)
        if 'details' in kwargs:
            r.request_details = kwargs['details']
        else:
            r.request_details = 'basic'

        if 'account_id' in kwargs:
            params = {'accountId': kwargs['account_id']}
        else:
            params = {}

        x = r.get(params=params)
        if r.last_error is None:
            if keys_only is True:
                return [i['groupId'] for i in x[cls.COLLECTION_NAME]]
            else:
                return [cls(i['groupId']) for i in x[cls.COLLECTION_NAME]]
        else:
            raise GroupException(r.last_error)

    @required_attrs(['name', 'description'])
    def create(self, callback=None):
        """Creates a new group

        :param callback: Optional callback to send the resulting :class:`Job`
        :raises: :class:`GroupCreationException`
        """

        parms = {'group': {'name': self.name,
                    'description': self.description}}

        payload = {'addGroup':camel_keys(parms)}

        print json.dumps(payload)
        self.post(data=json.dumps(payload))
        if self.last_error is None:
            self.load()
        else:
            raise GroupCreationException(self.last_error)

class GroupException(BaseException): pass

class GroupCreationException(GroupException):
    """Group Creation Exception"""
    pass
