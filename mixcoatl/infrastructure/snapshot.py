"""Implements access to the enStratus Snapshot API"""
from mixcoatl.resource import Resource
from mixcoatl.decorators.lazy import lazy_property

class Snapshot(Resource):
    PATH = 'infrastructure/Snapshot'
    COLLECTION_NAME = 'snapshots'
    PRIMARY_KEY = 'snapshot_id'

    def __init__(self, snapshot_id = None, *args, **kwargs):
        Resource.__init__(self)
        self.__snapshot_id = snapshot_id

    @property
    def snapshot_id(self):
        """`int` - The unique enStratus id for this snapshot"""
        return self.__snapshot_id

    @lazy_property
    def available(self):
        """`bool` - Identifies if the snapshot is available for creating volumes"""
        return self.__available

    @lazy_property
    def budget(self):
        """`int` - The id of the billing code against which costs will be associated"""
        return self.__budget

    @budget.setter
    def budget(self, budget):
        self.__budget == budget

    @lazy_property
    def cloud(self):
        """`dict` - The cloud in which this snapshot is stored"""
        return self.__cloud

    @lazy_property
    def created_timestamp(self):
        return self.__created_timestamp

    @lazy_property
    def customer(self):
        """`dict` - The customer to which the snapshot belongs"""
        return self.__customer

    @lazy_property
    def description(self):
        """`str` - The description of the snapshot established in enStratus"""
        return self.__description

    @description.setter
    def description(self, desc):
        self.__description = desc

    @lazy_property
    def encrypted(self):
        """`bool` - Is the snapshot known to be encrypted by enStratus"""
        return self.__encrypted

    @lazy_property
    def name(self):
        """`str` - The user-friendly name of the snapshot"""
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @lazy_property
    def label(self):
        """`str` - The label assigned to the snapshot"""
        return self.__label

    @label.setter
    def label(self, label):
        self.__label = label

    @lazy_property
    def owning_account(self):
        """`dict` or `None` - The enStratus account where the snapshot is registered"""
        return self.__owning_account

    @lazy_property
    def owning_groups(self):
        """`dict` - The enStratus groups who have ownership of this snapshot"""
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
        """`str` - The enStratus status of the snapshot *(`ACTIVE`|`INACTIVE`)*"""
        return self.__status

    @lazy_property
    def volume(self):
        """`dict` or `None` - The volume, if known, from which the snapshot was created"""
        return self.__volume

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
        r.request_details = 'basic'
        params = {}
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
        c = r.get(params=params)
        if r.last_error is None:
            if keys_only is True:
                snapshots = [item['snapshotId'] for item in c[cls.COLLECTION_NAME]]
            else:
                snapshots = []
                for i in c[cls.COLLECTION_NAME]:
                    snapshot = cls(i['snapshotId'])
                    if 'detail' in kwargs:
                        snapshot.request_details = kwargs['detail']
                    snapshot.load()
                    snapshots.append(snapshot)
            return snapshots
        else:
            raise SnapshotException(r.last_error['error']['message'])

class SnapshotException(BaseException): pass
