from mixcoatl.resource import Resource
from mixcoatl.decorators.validations import required_attrs
from mixcoatl.decorators.lazy import lazy_property
from mixcoatl.utils import camelize, camel_keys, uncamel_keys
import json


class MachineImage(Resource):

    """ A machine image is the baseline image or template from which virtual machines may be
    provisioned. Some clouds allow machine image/template sharing. In those clouds, Dell Cloud
    Manager creates multiple machine image records referencing the shared machine image object
    to enable users to maintain separate meta-data over those shared images. """
    PATH = 'infrastructure/MachineImage'
    COLLECTION_NAME = 'images'
    PRIMARY_KEY = 'machine_image_id'

    def __init__(self, machine_image_id=None, *args, **kwargs):
        """A machine image is the baseline image or template from which
            virtual machines may be provisioned.
        """
        Resource.__init__(self, request_details='basic')
        self.__machine_image_id = machine_image_id

    @property
    def machine_image_id(self):
        """`int` - The unique DCM id for this machine image"""
        return self.__machine_image_id

    @lazy_property
    def architecture(self):
        """`str` - The underlying CPU architecture of the virtual machine in question"""
        return self.__architecture

    @lazy_property
    def legacy_owner_id(self):
        return self.__legacy_owner_id

    @lazy_property
    def cloud(self):
        """`dict` - The cloud in which this machine image is installed"""
        return self.__cloud

    @lazy_property
    def creation_timestamp(self):
        """`str` - The date and time this machine image was first created

        .. .note::

                Some clouds do not report his value and it may therefore be `00:00 UTC January 1, 1970

        """
        return self.__creation_timestamp

    @lazy_property
    def customer(self):
        """`dict` - The customer in whose library this machine image record is being managed"""
        return self.__customer

    @lazy_property
    def budget(self):
        """`int` - The id of the billing code against which costs associated are
            billed for this machine image
        """
        return self.__budget

    @lazy_property
    def name(self):
        """`str` - The user friendly name for the machine image"""
        return self.__name

    @name.setter
    def name(self, n):
        self.__name = n

    @lazy_property
    def description(self):
        """`str` - The description of the machine image established in DCM"""
        return self.__description

    @description.setter
    def description(self, d):
        self.__description = d

    @lazy_property
    def owning_account(self):
        """`dict` - The DCM cloud account that is the account under which
            the machine image is registered

            .. .note::

                This value may be empty if the machine image belongs to an account
                not using DCM
        """
        return self.__owning_account

    @lazy_property
    def owning_cloud_account_number(self):
        """`str` - The DCM cloud account that is the account under which
            the machine image is registered.

            .. .note::

                This value is empty for public images and in rare circumstances
                when DCM is unable to determine the ownership

        """
        return self.__owning_cloud_account_number

    @lazy_property
    def owning_user(self):
        """`dict` or `None` - The user who is the owner of record of this machine image.

            .. .note::

                The owner may be null in cases of auto-discovery or certain automated scenarios

        """
        return self.__owning_user

    @lazy_property
    def owning_groups(self):
        """`list` - The groups who have ownership over this machine image"""
        return self.__owning_groups

    @owning_groups.setter
    def owning_groups(self, d):
        self.__owning_groups = d

    @lazy_property
    def platform(self):
        """`str` - The operating system bundled into the machine image/template"""
        return self.__platform

    @lazy_property
    def provider_id(self):
        """`str` - The cloud provider's unique id for the machine image"""
        return self.__provider_id

    @lazy_property
    def region(self):
        """`dict` - The region in which this machine image is available"""
        return self.__region

    @lazy_property
    def removable(self):
        """`bool` - Whether or not this machine image can be deleted"""
        return self.__removable

    @lazy_property
    def sharable(self):
        """`bool` - Whether or not this image can be shared"""
        return self.__sharable

    @lazy_property
    def status(self):
        """`str` - The current status of this machine image"""
        return self.__status

    @lazy_property
    def label(self):
        """`str` - A color label assigned to this machine image"""
        return self.__label

    @lazy_property
    def products(self):
        """`list` - The server products that can be used to provision a virtual
            machine based on this machine image/template
        """
        return self.__products

    @lazy_property
    def agent_version(self):
        """`int` - The version of the DCM agent if installed on the machine image"""
        return self.__agent_version

    @lazy_property
    def public(self):
        """`bool` - Indicates whether or not this image is publicly shared. 
        This value may be modified only for machine images that belong to your account. """
        return self.__public

    @public.setter
    def public(self, p):
        self.__public = p

    @lazy_property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, b):
        self.__budget = b

    @required_attrs(['machine_image_id'])
    def destroy(self, reason='no reason provided'):
        """Deletes machine image with reason :attr:`reason`

        :param reason: The reason for removing the image
        :type reason: str.
        :returns: bool -- Result of API call
        """
        p = self.PATH + "/" + str(self.machine_image_id)
        qopts = {'reason': reason}
        return self.delete(p, params=qopts)

    @required_attrs(['server_id', 'name', 'budget', 'description', 'owning_groups'])
    def create(self, callback=None):
        """Creates a machine image from server_id

        >>> def cb(j): print(j)
        >>> m = MachineImage()
        >>> m.server_id = 12345
        >>> m.name = 'image-1-test'
        >>> m.budget = 12345
        >>> m.create(callback=cb)

        :returns: int -- The job id of the create request
        """
        payload = {'imageServer':
                   [{
                       'budget': int(self.budget),
                       'description': self.description,
                       'name': self.name,
                       'server': {"serverId": int(self.server_id)},
                       'owningGroups': [{"groupId": self.owning_groups}],
                   }]}

        self.post(data=json.dumps(payload))
        if self.last_error is None:
            if callback is not None:
                callback(self.current_job)
            else:
                return self.current_job
        else:
            raise MachineImageException(self.last_error)

    @required_attrs(['machine_image_id'])
    def update(self, **kwargs):
        """Updates meta-data for an image.

        :param description: The description of an image.
        :type description: str.
        :param name: The name of an image.
        :type name: str.
        :param label: The label of an image.
        :type label: str.
        :returns: True if successful or an error message if fails.
        """
        payload = {'describeImage': [{}]}

        if 'description' in kwargs:
            payload['describeImage'][0]['description'] = kwargs['description']
        if 'name' in kwargs:
            payload['describeImage'][0]['name'] = kwargs['name']
        if 'label' in kwargs:
            payload['describeImage'][0]['label'] = kwargs['label']

        p = self.PATH + "/" + str(self.machine_image_id)
        return self.put(p, data=json.dumps(payload))

    @classmethod
    def all(cls, **kwargs):
        """Return all machine images

        :param machine_image_id: The id of the machine image
        :type machine_image_id: int.
        :param region_id: The region to search for machine images
        :type region_id: int.
        :param keys_only: Return :attr:`machine_image_id` instead of :class:`MachineImage`
        :type keys_only: bool.
        :param available: Return only available images. Default is `true`
        :type available: str.
        :param registered: Return only images with the DCM agent installed. Default is `false`
        :type registered: str.
        :param detail: The level of detail to return - `basic` or `extended`
        :type detail: str.
        :returns: `list` of :class:`MachineImage` or :attr:`machine_image_id`
        :raises: :class:`MachineImageException`
        """
        if 'machine_image_id' in kwargs:
            r = Resource(cls.PATH + "/" + str(kwargs['machine_image_id']))
        else:
            r = Resource(cls.PATH)

        params = {}

        if 'keys_only' in kwargs:
            keys_only = kwargs['keys_only']
        else:
            keys_only = False

        if 'region_id' in kwargs:
            params['regionId'] = kwargs['region_id']

        if 'available' in kwargs:
            params['active'] = kwargs['available']

        if 'registered' in kwargs:
            params['registered'] = kwargs['registered']

        x = r.get(params=params)
        if r.last_error is None:
            if keys_only is True:
                return [i[camelize(cls.PRIMARY_KEY)]
                        for i in x[cls.COLLECTION_NAME]]
            else:
                return [type(cls.__name__, (object,), i)
                        for i in uncamel_keys(x)[cls.COLLECTION_NAME]]
        else:
            raise MachineImageException(r.last_error)


class MachineImageException(BaseException):
    pass
