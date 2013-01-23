"""Implements the enStratus Volume API"""
from mixcoatl.resource import Resource
from mixcoatl.decorators.lazy import lazy_property
from mixcoatl.utils import camelize

class Volume(Resource):
    """A volume is a block storage device that may be mounted by servers"""
    PATH = 'infrastructure/Volume'
    COLLECTION_NAME = 'volumes'
    PRIMARY_KEY = 'volume_id'

    def __init__(self, volume_id=None, *args, **kwargs):
        # pylint: disable-msg=W0613
        Resource.__init__(self)
        self.__volume_id = volume_id

    @property
    def volume_id(self):
        """`str` - The unique enStratus id of the volume"""
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

    @lazy_property
    def encrypted(self):
        """`bool` - Indicates if the volume is known by enStratus as encrypted"""
        return self.__encrypted

    @lazy_property
    def region(self):
        """`dict` - The region in which this volume is stored"""
        return self.__region

    @lazy_property
    def budget(self):
        """`int` - The ID of the billing code against which costs are billed"""
        return self.__budget

    @lazy_property
    def server(self):
        """`dict` or `None` - The server to which this volume is attached if any"""
        return self.__server

    @lazy_property
    def owning_groups(self):
        """`list` - The groups who have ownership of this volume in enStratus"""
        return self.__owning_groups

    @lazy_property
    def size_in_gb(self):
        """`int` - The size of the volume if reported by the cloud provider"""
        return self.__size_in_gb

    @lazy_property
    def status(self):
        """`str` - The status of the volume in enStratus"""
        return self.__status

    @lazy_property
    def removable(self):
        """`bool` - If this volume is removable or not"""
        return self.__removable

    @lazy_property
    def data_center(self):
        """`dict` - The data center where this volume is stored"""
        return self.__data_center

    @lazy_property
    def owning_account(self):
        """`dict` - the enStratus account under which this volume is registered"""
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
        """`dict` - The enStratus user who is the owner of this volume"""
        return self.__owning_user

    @lazy_property
    def cloud(self):
        """`dict` - The cloud where this volume is stored"""
        return self.__cloud

    @lazy_property
    def description(self):
        """`str` - The description of the volume in enStratus"""
        return self.__description

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
        params = {}
        r = Resource(cls.PATH)
        r.request_details = 'basic'
        if 'detail' in kwargs:
            request_details = kwargs['detail']
        else:
            request_details = 'extended'

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
                volumes = [i[camelize(cls.PRIMARY_KEY)] for i in x[cls.COLLECTION_NAME]]
            else:
                volumes = []
                for i in x[cls.COLLECTION_NAME]:
                    volume = cls(i[camelize(cls.PRIMARY_KEY)])
                    volume.request_details = request_details
                    volume.load()
                    volumes.append(volume)
            return volumes
        else:
            raise VolumeException(r.last_error['error']['message'])

    @classmethod
    def assign_budget(cls, volume_id, budget, callback=None):
        """Change the budget associated with a volume"""
        pass

    @classmethod
    def assign_groups(cls, volume_id, group_id):
        """Change the group ownership of a volume"""
        pass

    @classmethod
    def attach(cls, volume_id, server_id, device_id=None):
        """Attach a volume to a server"""
        pass

    @classmethod
    def describe_volume(cls, volume_id, **kwargs):
        """Change the enStratus meta-data of a volume"""
        pass

    @classmethod
    def detach(cls, volume_id, reason):
        """Detach a volume from a server"""
        pass

class VolumeException(BaseException):
    """Generic Volume Exception"""
    pass
