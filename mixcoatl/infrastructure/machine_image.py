from mixcoatl.resource import Resource
from mixcoatl.decorators.lazy import lazy_property

# TODO: certain images cause weird redirect
# m = MachineImage(284555) redirect loop
# m = MachineImage(284831) no loop
class MachineImage(Resource):
    path = 'infrastructure/MachineImage'
    collection_name = 'images'
    primary_key = 'machine_image_id'

    def __init__(self, machine_image_id = None, *args, **kwargs):
        Resource.__init__(self, request_details='basic')
        self.__machine_image_id = machine_image_id

    @property
    def machine_image_id(self):
        return self.__machine_image_id
    
    @lazy_property
    def architecture(self):
        return self.__architecture

    @lazy_property
    def cloud(self):
        return self.__cloud

    @lazy_property
    def creation_timestamp(self):
        return self.__creation_timestamp

    @lazy_property
    def customer(self):
        return self.__customer

    @lazy_property
    def budget(self):
        return self.__budget

    @lazy_property
    def description(self):
        return self.__description

    @lazy_property
    def name(self):
        return self.__name

    @lazy_property
    def owning_account(self):
        return self.__owning_account

    @lazy_property
    def owning_cloud_account_number(self):
        return self.__owning_cloud_account_number

    @lazy_property
    def owning_user(self):
        return self.__owning_user

    @lazy_property
    def platform(self):
        return self.__platform

    @lazy_property
    def provider_id(self):
        return self.__provider_id

    @lazy_property
    def region(self):
        return self.__region

    @lazy_property
    def removable(self):
        return self.__removable

    @lazy_property
    def sharable(self):
        return self.__sharable

    @lazy_property
    def status(self):
        return self.__status

    @lazy_property
    def label(self):
        return self.__label

    @lazy_property
    def products(self):
        return self.__products

    @lazy_property
    def agent_version(self):
        return self.__agent_version

    @classmethod
    def all(cls, region_id):
        from mixcoatl.utils import uncamel_keys
        r = Resource(cls.path, request_details='basic')
        params = {'regionId':region_id}
        c = r.get(params=params)
        if r.last_error is None:
            #images = [i['machineImageId'] for i in c[cls.collection_name]]
            #return images
            return [cls(i['machineImageId']) for i in c[cls.collection_name]]
            #return uncamel_keys(c)
        else:
            return r.last_error