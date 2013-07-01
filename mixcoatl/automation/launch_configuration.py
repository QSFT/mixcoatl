from mixcoatl.resource import Resource
from mixcoatl.decorators.lazy import lazy_property
from mixcoatl.decorators.validations import required_attrs
from mixcoatl.utils import camelize, camel_keys
from mixcoatl.admin.job import Job

import json
import time

class LaunchConfiguration(Resource):
    PATH = 'automation/LaunchConfiguration'
    COLLECTION_NAME = 'launchConfigurations'
    PRIMARY_KEY = 'launch_configuration_id'

    def __init__(self, launch_configuration_id=None, *args, **kwargs):
        Resource.__init__(self)
        self.__launch_configuration_id = launch_configuration_id

    @property
    def launch_configuration_id(self):
        return self.__launch_configuration_id

    @property
    def deployment(self):
        return self.__deployment

    @property
    def array_volume_capacity(self):
        return self.__array_volume_capacity

    @property
    def array_volume_count(self):
        return self.__array_volume_count

    @lazy_property
    def label(self):
        return self.__label

    @label.setter
    def label(self, l):
        self.__label = l

    @lazy_property
    def customer(self):
        return self.__customer

    @lazy_property
    def created_timestamp(self):
        return self.__created_timestamp

    @lazy_property
    def created(self):
        return self.__created

    @lazy_property
    def cm_account(self):
        return self.__cm_account

    @lazy_property
    def firewalls(self):
        return self.__firewalls

    @firewalls.setter
    def firewalls(self, f):
        self.__firewalls = f

    @lazy_property
    def network(self):
        return self.__network

    @network.setter
    def network(self, n):
        self.__network = n

    @lazy_property
    def personalities(self):
        return self.__personalities

    @personalities.setter
    def personalities(self, p):
        self.__personalities = p

    @lazy_property
    def primary_machine_image(self):
        return self.__primary_machine_image

    @primary_machine_image.setter
    def primary_machine_image(self, p):
        self.__primary_machine_image = p

    @lazy_property
    def primary_product(self):
        return self.__primary_product

    @primary_product.setter
    def primary_product(self, p):
        self.__primary_product = p

    @lazy_property
    def raid_level(self):
        return self.__raid_level

    @raid_level.setter
    def raid_level(self, r):
        self.__raid_level = r

    @lazy_property
    def recovery_delay_in_minutes(self):
        return self.__recovery_delay_in_minutes

    @recovery_delay_in_minutes.setter
    def recovery_delay_in_minutes(self, d):
        self.__recovery_delay_in_minutes = d

    @lazy_property
    def region(self):
        return self.__region

    @region.setter
    def region(self, r):
        self.__region = r

    @lazy_property
    def scripts(self):
        return self.__scripts

    @scripts.setter
    def scripts(self, s):
        self.__scripts = s

    @lazy_property
    def secondary_machine_image(self):
        return self.__secondary_machine_image

    @secondary_machine_image.setter
    def secondary_machine_image(self, s):
        self.__secondary_machine_image = s

    @lazy_property
    def secondary_product(self):
        return self.__secondary_product

    @secondary_product.setter
    def secondary_product(self, s):
        self.__secondary_product = s

    @lazy_property
    def server_name_template(self):
        return self.__server_name_template

    @server_name_template.setter
    def server_name_template(self, l):
        self.__server_name_template = l

    @lazy_property
    def server_type(self):
        return self.__server_type

    @server_type.setter
    def server_type(self, s):
        self.__server_type = s

    @lazy_property
    def snapshot_interval_in_minutes(self):
        return self.__snapshot_interval_in_minutes

    @snapshot_interval_in_minutes.setter
    def snapshot_interval_in_minutes(self, l):
        self.__snapshot_interval_in_minutes = l

    @lazy_property
    def subnet(self):
        return self.__subnet

    @subnet.setter
    def subnet(self, s):
        self.__subnet = s

    @property
    def tier(self):
        return self.__tier

    @tier.setter
    def tier(self, t):
        self.__tier = t

    @lazy_property
    def use_encrypted_volumes(self):
        return self.__use_encrypted_volumes

    @use_encrypted_volumes.setter
    def use_encrypted_volumes(self, u):
        self.__use_encrypted_volumes = u

    @lazy_property
    def use_hypervisor_stats(self):
        return self.__use_hypervisor_stats

    @use_hypervisor_stats.setter
    def use_hypervisor_stats(self, l):
        self.__use_hypervisor_stats = l

    @lazy_property
    def removable(self):
        return self.__removable

    @lazy_property
    def status(self):
        return self.__status

    @classmethod
    def all(cls, **kwargs):
        r = Resource(cls.PATH)
        if 'details' in kwargs:
            r.request_details = kwargs['details']
        else:
            r.request_details = 'basic'

        x = r.get()
        if r.last_error is None:
            return [cls(i[camelize(cls.PRIMARY_KEY)]) for i in x[cls.COLLECTION_NAME]]
        else:
            return r.last_error

    @required_attrs(['tier',
										 'region',
										 'primary_machine_image',
										 'primary_product_id'
										 ])

    def create(self, callback=None):
        """Creates a new launch configuration

        :param callback: Optional callback to send the resulting :class:`Job`
        :raises: :class:`TierCreationException`
        """
        #lc.name = name
        #lc.region = region
        #lc.primary_product = primary_product_id
        #lc.secondary_product = secondary_product_id
        #lc.primary_machine_image = primary_machine_image
        #lc.secondary_machine_image = secondary_machine_image
        #lc.server_name_template = server_name_template
        #lc.tier = tier
        #lc.firewall = firewall
        #lc.region = region

        parms = [{'tier':{'tierId':self.tier},
                 'primaryMachineImage':{'machineImageId':self.primary_machine_image},
                 'primaryProduct':{'productId':self.primary_product_id},
                 'firewalls':[{'firewallId':self.firewalls}],
                 'region':{'regionId':self.region}}]

        payload = {'addLaunchConfiguration':camel_keys(parms)}

        response=self.post(data=json.dumps(payload))
        if self.last_error is None:
            self.load()
            print response
            return response
        else:
            raise LaunchConfigurationCreationException(self.last_error)

class LaunchConfigurationException(BaseException): pass

class LaunchConfigurationCreationException(LaunchConfigurationException):
    """Launch Configuration Creation Exception"""
    pass
