"""Implements access to the DCM Snapshot API"""
from mixcoatl.resource import Resource
from mixcoatl.decorators.lazy import lazy_property
from mixcoatl.decorators.validations import required_attrs
from mixcoatl.utils import camelize, camel_keys, uncamel_keys
from mixcoatl.admin.job import Job
import json


class Snapshot(Resource):

    """A snapshot is a point-in-time snapshot of a volume"""
    PATH = 'infrastructure/Snapshot'
    COLLECTION_NAME = 'snapshots'
    PRIMARY_KEY = 'snapshot_id'

    def __init__(self, snapshot_id=None, *args, **kwargs):
        # pylint: disable-msg=W0613
        Resource.__init__(self)
        self.__snapshot_id = snapshot_id

    @property
    def snapshot_id(self):
        """`int` - The unique DCM id for this snapshot"""
        return self.__snapshot_id

    @lazy_property
    def available(self):
        """`bool` - Identifies if the snapshot is available for creating volumes"""
        return self.__available

    @lazy_property
    def budget(self):
        """`int` - The id of the billing code against which costs will be associated"""
        # pylint: disable-msg=E0202
        return self.__budget

    @budget.setter
    def budget(self, budget):
        # pylint: disable-msg=C0111,W0201
        self.__budget = budget

    @lazy_property
    def cloud(self):
        """`dict` - The cloud in which this snapshot is stored"""
        return self.__cloud

    @lazy_property
    def created_timestamp(self):
        """`str` - The timestamp when the snapshot was created"""
        return self.__created_timestamp

    @lazy_property
    def customer(self):
        """`dict` - The customer to which the snapshot belongs"""
        return self.__customer

    @lazy_property
    def description(self):
        """`str` - The description of the snapshot established in DCM"""
        # pylint: disable-msg=E0202
        return self.__description

    @description.setter
    def description(self, desc):
        # pylint: disable-msg=C0111,W0201
        self.__description = desc

    @lazy_property
    def encrypted(self):
        """`bool` - Is the snapshot known to be encrypted by DCM"""
        return self.__encrypted

    @lazy_property
    def name(self):
        """`str` - The user-friendly name of the snapshot"""
        # pylint: disable-msg=E0202
        return self.__name

    @name.setter
    def name(self, name):
        # pylint: disable-msg=C0111,W0201
        self.__name = name

    @lazy_property
    def label(self):
        """`str` - The label assigned to the snapshot"""
        return self.__label

    @label.setter
    def label(self, label):
        # pylint: disable-msg=C0111,W0201
        self.__label = label

    @lazy_property
    def owning_account(self):
        """`dict` or `None` - The DCM account where the snapshot is registered"""
        return self.__owning_account

    @lazy_property
    def owning_user(self):
        """`dict` or `None` - The DCM user who has ownership of this snapshot"""
        return self.__owning_user

    @lazy_property
    def owning_groups(self):
        """`dict` - The DCM groups who have ownership of this snapshot"""
        return self.__owning_groups

    @lazy_property
    def provider_id(self):
        """`str` - The cloud provider's unique id for the snapshot"""
        return self.__provider_id

    @lazy_property
    def region(self):
        """`dict` - The cloud region where the snapshot is stored"""
        return self.__region

    @lazy_property
    def removable(self):
        """`bool` - Indicates if this snapshot can be removed"""
        return self.__removable

    @lazy_property
    def sharable(self):
        """`bool` - Indicates if this snapshot can be shared"""
        return self.__sharable

    @lazy_property
    def size_in_gb(self):
        """`int` - The size of the snapshot in GB"""
        return self.__size_in_gb

    @lazy_property
    def status(self):
        """`str` - The DCM status of the snapshot *(`ACTIVE`|`INACTIVE`)*"""
        return self.__status

    @lazy_property
    def volume(self):
        """`dict` or `None` - The volume, if known, from which the snapshot was created"""
        # pylint: disable-msg=E0202
        return self.__volume

    @volume.setter
    def volume(self, volume_id):
        # pylint: disable-msg=C0111,W0201
        self.__volume = {'volume_id': volume_id}

    @required_attrs(['snapshot_id'])
    def destroy(self, reason='No reason given'):
        """delete a snapshot

        :param reason: A reason for deleting the snapshot
        :type reason: str.
        :returns: `bool`
        :raises: :class:`SnapshotException`
        """
        params = {'reason': reason}

        try:
            return self.delete(self.PATH + '/' + str(self.snapshot_id), params=params)
        except:
            raise SnapshotException(self.last_error)

    def update(self):
        """Updates a snapshot with changed values

        :returns: :class:`Snapshot`
        :raises: :class:`SnapshotException`
        """

        if self.pending_changes is None:
            pass
        else:
            payload = {'describeSnapshot': [{}]}
            for x in ['name', 'description', 'label']:
                if x in self.pending_changes:
                    new_val = self.pending_changes[x]['new']
                    payload['describeSnapshot'][0][camel_keys(x)] = new_val
                    self.pending_changes.pop(x, None)
            if len(payload['describeSnapshot'][0]) == 0:
                pass
            else:
                self.put(
                    self.PATH + '/' + str(self.snapshot_id), data=json.dumps(payload))

            if self.last_error is None:
                self.load()
                return self
            else:
                raise SnapshotException(self.last_error)

    @required_attrs(['volume', 'name', 'description', 'budget'])
    def create(self, callback=None):
        """Creates a snapshot

        :returns: :class:`Snapshot`
        :raises: :class:`SnapshotException`
        """

        if self.snapshot_id is not None:
            raise SnapshotException(
                'Cannot snapshot a snapshot: %s' % self.snapshot_id)

        payload = {'addSnapshot': [{}]}
        payload['addSnapshot'][0]['volume'] = camel_keys(self.volume)
        payload['addSnapshot'][0]['name'] = self.name
        payload['addSnapshot'][0]['description'] = self.description
        payload['addSnapshot'][0]['budget'] = self.budget
        optional_attrs = ['label']

        for oa in optional_attrs:
            try:
                if getattr(self, oa) is not None:
                    payload['addSnapshot'][0].update(
                        camel_keys({oa: getattr(self, oa)}))
            except AttributeError:
                # We did say optional....
                pass
        self.post(self.PATH, data=json.dumps(payload))
        if self.last_error is None:
            if callback is not None:
                callback(self)
            else:
                return self
        else:
            raise SnapshotException(self.last_error)

    @classmethod
    def all(cls, **kwargs):
        """Return a list of snapshots

        :param account_id: Restrict to snapshots owned by `account_id`
        :type account_id: int.
        :param volume_id: Restrict to snapshots based on `volume_id`
        :type volume_id: int.
        :param region_id: Restrict to snapshots in `region_id`
        :type region_id: int.
        :param keys_only: Return :attr:`snapshot_id` or :class:`Snapshot`
        :type keys_only: bool.
        :param detail: Level of detail to return - `basic` or `extended`
        :type detail: str.
        :returns: `list` of :attr:`snapshot_id` or :class:`Snapshot`
        :raises: :class:`SnapshotException`
        """
        r = Resource(cls.PATH)
        params = {}

        if 'detail' in kwargs:
            r.request_details = kwargs['detail']
        else:
            r.request_details = 'basic'

        if 'keys_only' in kwargs:
            keys_only = kwargs['keys_only']
        else:
            keys_only = False

        if 'region_id' in kwargs:
            params['regionId'] = kwargs['region_id']
        if 'account_id' in kwargs:
            params['accountId'] = kwargs['account_id']
        if 'volume_id' in kwargs:
            params['volumeId'] = kwargs['volume_id']

        x = r.get(params=params)
        if r.last_error is None:
            if keys_only is True:
                return [i[camelize(cls.PRIMARY_KEY)] for i in x[cls.COLLECTION_NAME]]
            else:
                return [type(cls.__name__, (object,), i) for i in uncamel_keys(x)[cls.COLLECTION_NAME]]
        else:
            raise SnapshotException(r.last_error)

    @classmethod
    def describe_snapshot(cls, snapshot_id, **kwargs):
        """Changes the basic metadata for a snapshot

        :param id: The snapshot to modify
        :type id: int.
        :param description: Change the description.
        :type description: str.
        :param name: Change the name.
        :type name: str.
        :param label: Change the label. To remove the label, set to `None`
        :type label: str.
        :returns: :class:`Snapshot`
        :raises: :class:`SnapshotException`
        """
        s = cls(snapshot_id)
        for x in ['name', 'description', 'label']:
            if x in kwargs:
                setattr(s, x, kwargs[x])
        s.update()
        return s

    @classmethod
    def delete_snapshot(cls, snapshot_id, reason):
        """delete a snapshot

        :param snapshot_id: The DCM snapshot id
        :type snapshot_id: int
        :param reason: A reason for deleting the snapshot
        :type reason: str.
        :returns: `bool`
        :raises: :class:`SnapshotException`
        """
        s = cls(snapshot_id)
        return s.destroy(reason=reason)

    @classmethod
    def add_snapshot(cls, volume_id, name, description, budget, callback=None):
        """Creates a snapshot from `volume_id`

            .. warning::

                Snapshot creation is an asynchronous task.
                Specifying a callback will cause a blocking operation while the snapshot completes.
                When using the callback, execution could block for a **VERY** long time depending on the time it takes to make the snapshot.

        :param volume_id: The volume to snapshot
        :type volume_id: int.
        :param name: The name for the snapshot
        :type name: str.
        :param description: Description of the snapshot
        :type description: str.
        :param budget: The billing code for the snapshot
        :type budget: int.
        :param callback: An optional callback to send the final :class:`Snapshot`.
        :type callback: func.
        :returns: :class:`Snapshot`
        :raises: :class:`SnapshotException`
        """

        s = cls()
        s.volume = volume_id
        s.name = name
        s.budget = budget
        s.description = description
        s.create()
        if s.current_job is None:
            raise SnapshotException('No job found. This is...odd')
        else:
            if callback is not None:
                job = Job.wait_for(s.current_job)
                if job is True:
                    try:
                        j = Job(s.current_job)
                        snapshot = cls(j.message)
                        snapshot.load()
                        callback(snapshot)
                    except:
                        raise SnapshotException("Unhandled error in callback")
            else:
                return s


class SnapshotException(BaseException):

    """Generic exception for Snapshots"""
    pass
