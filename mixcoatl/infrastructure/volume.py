"""Implements the DCM Volume API"""
from mixcoatl.resource import Resource
from mixcoatl.decorators.lazy import lazy_property
from mixcoatl.decorators.validations import required_attrs
from mixcoatl.utils import camelize, camel_keys, uncamel_keys
from mixcoatl.infrastructure.snapshot import Snapshot
from mixcoatl.infrastructure.snapshot import SnapshotException
from mixcoatl.admin.job import Job
import json
import time


class Volume(Resource):

    """A volume is a block storage device that may be mounted by servers"""
    PATH = 'infrastructure/Volume'
    COLLECTION_NAME = 'volumes'
    PRIMARY_KEY = 'volume_id'

    def __init__(self, volume_id=None, **kwargs):
        # pylint: disable-msg=W0613
        Resource.__init__(self)
        if 'detail' in kwargs:
            self.request_details = kwargs['detail']
        self.__volume_id = volume_id

    @property
    def volume_id(self):
        """`str` - The unique DCM id of the volume"""
        return self.__volume_id

    @lazy_property
    def array(self):
        """`dict` or `None` - The array, if any, that this volume belongs to"""
        return self.__array

    @lazy_property
    def available(self):
        """`bool` - Indicates if this volume is available for attachment"""
        return self.__available

    @lazy_property
    def customer(self):
        """`dict` - The customer to which this volume belongs"""
        return self.__customer

    @lazy_property
    def provider_id(self):
        """`str` - The unique cloud provider ID for this volume"""
        return self.__provider_id

    @lazy_property
    def size_string(self):
        """`str` - User-friendly string representing the size of the volume"""
        return self.__size_string

    @lazy_property
    def name(self):
        """`str` - A user-friendly name for the volume"""
        return self.__name

    @name.setter
    def name(self, b):
        # pylint: disable-msg=C0111,W0201
        self.__name = b

    @lazy_property
    def label(self):
        """`str` - A user-friendly label for the volume"""
        return self.__label

    @label.setter
    def label(self, b):
        # pylint: disable-msg=C0111,W0201
        self.__label = b

    @lazy_property
    def encrypted(self):
        """`bool` - Indicates if the volume is known by DCM as encrypted"""
        return self.__encrypted

    @lazy_property
    def region(self):
        """`dict` - The region in which this volume is stored"""
        return self.__region

    @lazy_property
    def budget(self):
        """`int` - The ID of the billing code against which costs are billed"""
        return self.__budget

    @budget.setter
    def budget(self, b):
        # pylint: disable-msg=C0111,W0201
        self.__budget = b

    @lazy_property
    def server(self):
        """`dict` or `None` - The server to which this volume is attached if any"""
        return self.__server

    @lazy_property
    def owning_groups(self):
        """`list` - The groups who have ownership of this volume in DCM"""
        return self.__owning_groups

    @lazy_property
    def size_in_gb(self):
        """`int` - The size of the volume if reported by the cloud provider"""
        return self.__size_in_gb

    @size_in_gb.setter
    def size_in_gb(self, size):
        self.__size_in_gb = size

    @lazy_property
    def status(self):
        """`str` - The status of the volume in DCM"""
        return self.__status

    @lazy_property
    def removable(self):
        """`bool` - If this volume is removable or not"""
        return self.__removable

    @lazy_property
    def data_center(self):
        """`dict` - The data center where this volume is stored"""
        return self.__data_center

    @data_center.setter
    def data_center(self, dc):
        self.__data_center = {'data_center_id': dc}

    @lazy_property
    def owning_account(self):
        """`dict` - the DCM account under which this volume is registered"""
        return self.__owning_account

    @lazy_property
    def device_id(self):
        """`str` or `None` - The OS device id of this volume if attached"""
        return self.__device_id

    @lazy_property
    def creation_timestamp(self):
        """`str` - The timestamp when this volume was created"""
        return self.__creation_timestamp

    @lazy_property
    def owning_user(self):
        """`dict` - The DCM user who is the owner of this volume"""
        return self.__owning_user

    @lazy_property
    def cloud(self):
        """`dict` - The cloud where this volume is stored"""
        return self.__cloud

    @lazy_property
    def description(self):
        """`str` - The description of the volume in DCM"""
        return self.__description

    @description.setter
    def description(self, b):
        # pylint: disable-msg=C0111,W0201
        self.__description = b

    @required_attrs(['volume_id'])
    def attach(self, server_id, device_id=None, callback=None):
        """Attach a volume to a server

        :param server_id: Server to attach the volume
        :type server_id: int.
        :param callback: Optional callback to send the results
        :returns: :class:`Volume`
        :raises: :class:`VolumeException`
        """
        payload = {'attach': [{'server': {'server_id': server_id}}]}

        if device_id is not None:
            payload['attach'][0]['device_id'] = device_id

        self.put(self.PATH + '/' + str(self.volume_id),
                 data=json.dumps(camel_keys(payload)))

        if self.last_error is None:
            if callback is None:
                return self
            else:
                callback(self)
        else:
            raise VolumeException(self.last_error)

    def detach(self, callback=None):
        """Detach a volume from a server

        :param callback: Optional callback to send the results
        :returns: :class:`Volume`
        :raises: :class:`VolumeException`
        """
        payload = '{"detach":[{}]}'
        path = self.PATH + '/' + str(self.volume_id)
        s = self.put(path, data=payload)
        if self.last_error is None:
            self.load()
            if callback is None:
                return s
            else:
                callback(s)
        else:
            raise VolumeException(self.last_error)

    @required_attrs(['budget', 'size_in_gb', 'description', 'data_center', 'name'])
    def create(self, callback=None):
        """Creates a new volume

        :param callback: Optional callback to send the resulting :class:`Job`
        :type callback: func.
        :returns: :class:`Job`
        :raises: :class:`VolumeCreationException`
        """
        optional_attrs = ['label']
        if self.volume_id is not None:
            raise VolumeCreationException(
                'Cannot create an already created volume: %s' % self.volume_id)

        parms = {'name': self.name, 'description': self.description, 'data_center': self.data_center,
                 'size_in_gb': self.size_in_gb, 'budget': self.budget}

        for oa in optional_attrs:
            try:
                if getattr(self, oa) is not None:
                    parms[0].update({oa: getattr(self, oa)})
            except AttributeError:
                pass

        payload = {'addVolume': [camel_keys(parms)]}
        self.post(data=json.dumps(payload))
        if self.last_error is None:
            j = Job(self.current_job)
            j.load()
            if callback is not None:
                callback(j)
            else:
                return j
        else:
            raise VolumeCreationException(self.last_error)

    def update(self):
        """Updates a volume with changed values

        :returns: `bool`
        :raises: :class:`VolumeException`
        """

        if self.pending_changes is None:
            pass
        elif 'budget' in self.pending_changes:
            self._change_budget()
        else:
            self._change_metadata()

    def destroy(self, reason=None):
        """Deletes the volume

        :param reason: Reason for removing the volume
        :type reason: str.
        :returns: `bool`
        :raises: :class:`VolumeException`
        """
        p = self.PATH + "/" + str(self.volume_id)
        qopts = {'reason': reason}
        return self.delete(p, params=qopts)

    def _change_metadata(self):
        """Changes metadata"""
        new_vals = {}
        for x in ['name', 'description', 'label']:
            if x in self.pending_changes:
                new_val = self.pending_changes[x]['new']
                new_vals[camel_keys(x)] = new_val
                self.pending_changes.pop(x, None)
        if len(new_vals) == 0:
            pass
        else:
            payload = {'describeVolume': [new_vals]}
            self.put(
                self.PATH + '/' + str(self.volume_id), data=json.dumps(payload))
            if self.last_error is None:
                self.load()
                return True
            else:
                raise VolumeException(self.last_error)

    @required_attrs(['budget'])
    def _change_budget(self):
        """Changes budget"""
        changes = self.pending_changes.pop('budget', None)
        if changes is None:
            pass
        else:
            payload = {'assignBudget': [{'budget': self.budget}]}
            self.put(
                self.PATH + '/' + str(self.volume_id), data=json.dumps(payload))
            if self.last_error is None:
                self.load()
                return True
            else:
                raise VolumeException(self.last_error)

    def snapshot(self, **kwargs):
        """Make a snapshot from a volume

        *This is not a part of the DCM API for Volume resources.
        It is a convenience wrapper around the Snapshot API from the
        perspective of an individual* :class:`Volume`

            .. warning::

                Snapshot creation is an asynchronous task.
                Specifying a callback will cause a blocking operation while the snapshot completes
                When using the callback, execution could block for a **VERY** long time.


        :param name: The name to assign the Snapshot. Default: `snap-<volume_id>-timestamp`
        :type name: str.
        :param description: Description of the snapshot. Default: `mixcoatl snapshot`
        :type description: str.
        :param budget: Budget to assign the snapshot. Default: :attr:`budget` of the current :class:`Volume`
        :type budget: int.
        :param callback: Optional callback to return the results.
        :type callback: func.
        :returns: :class:`Snapshot`
        :raises: :class:`VolumeSnapshotException`
        """
        tstamp = str(int(time.time()))
        if 'name' in kwargs:
            name = kwargs['name']
        else:
            name = 'snap-%s-%s' % (self.volume_id, tstamp)
        if 'description' in kwargs:
            description = kwargs['description']
        else:
            description = 'mixcoat snapshot'
        if 'budget' in kwargs:
            budget = kwargs['budget']
        else:
            budget = self.budget
        if 'callback' in kwargs:
            callback = kwargs['callback']
        else:
            callback = None
        try:
            return Snapshot.add_snapshot(self.volume_id,
                                         name,
                                         description,
                                         budget,
                                         callback=callback)
        except SnapshotException, e:
            raise VolumeSnapshotException(str(e))

    @classmethod
    def all(cls, **kwargs):
        """List all volumes
        :param account_id: Restrict to volumes owned by `account_id`
        :type account_id: int.
        :param datacenter_id: Restrict to volumes based in `datacenter_id`
        :type datacenter_id: int.
        :param region_id: Restrict to volumes in `region_id`
        :type region_id: int.
        :param keys_only: Return :attr:`snapshot_id` or :class:`Snapshot`
        :type keys_only: bool.
        :param detail: Level of detail to return - `basic` or `extended`
        :type detail: str.
        :returns: `list` of :attr:`volume_id` or :class:`Volume`
        :raises: :class:`VolumeException`
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

        if 'datacenter_id' in kwargs:
            params['dataCenterId'] = kwargs['datacenter_id']
        if 'region_id' in kwargs:
            params['regionId'] = kwargs['region_id']
        if 'account_id' in kwargs:
            params['accountId'] = kwargs['account_id']

        x = r.get(params=params)
        if r.last_error is None:
            if keys_only is True:
                return [i[camelize(cls.PRIMARY_KEY)] for i in x[cls.COLLECTION_NAME]]
            else:
                return [type(cls.__name__, (object,), i) for i in uncamel_keys(x)[cls.COLLECTION_NAME]]
        else:
            raise VolumeException(r.last_error)

    @classmethod
    def assign_budget(cls, volume_id, budget):
        """Change the budget associated with a volume

        :param volume_id: The volume id to work with
        :type volume_id: int.
        :param budget: The budget code to assign
        :type budget: int.
        :returns: `bool`
        :raises: :class:`VolumeException`
        """
        v = Volume(volume_id)
        v.budget = budget
        return v.update()

    @classmethod
    def assign_groups(cls, volume_id, group_id):
        """Change the group ownership of a volume

        :param volume_id: The volume id to work with
        :type volume_id: int.
        :param group_id: The group id to assign
        :type group_id: int.
        :returns: bool.
        :raises: :class:`VolumeException`
        """
        pass

    @classmethod
    def attach_volume(cls, volume_id, server_id, device_id=None, callback=None):
        """Attach a volume to a server

            .. note::

                Attaching a volume is an asynchronous task.

        :param volume_id: The volume id to work with
        :type volume_id: int.
        :param server_id: The server to attach the volume
        :type server_id: int.
        :param device_id: Optional device id to assign the volume on the system
        :type device_id: str.
        :param callback: Optional callback to call with the results
        :type callback: func.
        :returns: :class:`Job`
        :raises: :class:`VolumeException`
        """
        v = Volume(volume_id)
        v.request_details = 'basic'
        v.attach(server_id, device_id, callback)

    @classmethod
    def describe_volume(cls, volume_id, **kwargs):
        """Change the DCM meta-data of a volume

        :param volume_id: The volume to modify
        :type volume_id: int.
        :param description: Change the description
        :type description: str.
        :param name: Change the name
        :type name: str.
        :param label: Change the label. To remove the label, set to `None`
        :type label: str.
        :returns: :class:`Volume`
        :raises: :class:`VolumeException`
        """
        if kwargs is None:
            pass
        else:
            v = Volume(volume_id)
            v.request_details = 'basic'
            for attr in kwargs:
                setattr(v, attr, kwargs[attr])
            v.update()
            return v

    @classmethod
    def add_volume(cls, **kwargs):
        """Create a new volume

        :param name: The name of the new volume
        :param size_in_gb: The size for the new volume
        :param data_center: The location of the new volume
        :param budget: The budget code for the new volume
        :param description: The description of the new volume
        :param callback: Optional callback to recieve the created Job
        :returns: :class:`Job`
        :raises: :class:`VolumeCreationException`
        """
        v = Volume()
        cb = kwargs.pop('callback', None)

        for attr in kwargs:
            setattr(v, attr, kwargs[attr])

        v.create(callback=cb)

    @classmethod
    def detach_volume(cls, volume_id, callback=None):
        """Detach a volume from a server

        :param volume_id: The volume to detach
        :type volume_id: int.
        :param callback: Optional callback to send the results
        :returns: :class:`Volume`
        :raises: :class:`VolumeException`
        """
        v = Volume(volume_id)
        v.detach(callback=callback)


class VolumeException(BaseException):

    """Generic Volume Exception"""
    pass


class VolumeSnapshotException(VolumeException):

    """Volume Snapshot Exception"""
    pass


class VolumeCreationException(VolumeException):

    """Volume Creation Exception"""
    pass
