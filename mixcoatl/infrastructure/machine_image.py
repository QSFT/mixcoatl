from mixcoatl.resource import Resource
from mixcoatl.decorators.lazy import lazy

# TODO: certain images cause weird redirect
# m = MachineImage(284555) redirect loop
# m = MachineImage(284831) no loop
@lazy(key='machine_image_id')
class MachineImage(Resource):
    path = 'infrastructure/MachineImage'
    collection_name = 'images'

    def __init__(self, machine_image_id = None, *args, **kwargs):
        Resource.__init__(self)
        if machine_image_id is None:
            pass
        self.__machine_image_id = machine_image_id

    @property
    def architecture(self):
        return self.__architecture

    @property
    def cloud(self):
        return self.__cloud

    @property
    def creation_timestamp(self):
        return self.__creation_timestamp

    @property
    def customer(self):
        return self.__customer

    @property
    def description(self):
        return self.__description

    @property
    def machine_image_id(self):
        return self.__machine_image_id

    @property
    def name(self):
        return self.__name

    @property
    def owning_account(self):
        return self.__owning_account

    @property
    def owning_cloud_account_number(self):
        return self.__owning_cloud_account_number

    @property
    def owning_user(self):
        return self.__owning_user

    @property
    def platform(self):
        return self.__platform

    @property
    def provider_id(self):
        return self.__provider_id

    @property
    def region(self):
        return self.__region

    @property
    def removable(self):
        return self.__removable

    @property
    def sharable(self):
        return self.__sharable

    @property
    def status(self):
        return self.__status

    @property
    def label(self):
        return self.__label

    @property
    def products(self):
        return self.__products

    @property
    def agent_version(self):
        return self.__agent_version

    @classmethod
    def all(cls, region_id):
        from mixcoatl.utils import uncamel_keys
        r = Resource(cls.path)
        params = {'regionId':region_id}
        c = r.get(params=params)
        if r.last_error is None:
            #return [cls(i['machineImageId']) for i in c[cls.collection_name]]
            return uncamel_keys(c)
        else:
            return r.last_error