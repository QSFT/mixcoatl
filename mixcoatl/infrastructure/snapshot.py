from mixcoatl.resource import Resource
from mixcoatl.decorators.lazy import lazy_property

class Snapshot(Resource):
    path = 'infrastructure/Snapshot'
    collection_name = 'snapshots'
    primary_key = 'snapshot_id'

    def __init__(self, snapshot_id = None, *args, **kwargs):
        Resource.__init__(self)
        self.__snapshot_id = snapshot_id

    @property
    def snapshot_id(self):
        return self.__snapshot_id

    @lazy_property
    def available(self):
        return self.__available

    @lazy_property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, budget):
        self.__budget == budget

    @lazy_property
    def cloud(self):
        return self.__cloud

    @lazy_property
    def created_timestamp(self):
        return self.__created_timestamp

    @lazy_property
    def customer(self):
        return self.__customer

    @lazy_property
    def description(self):
        return self.__description

    @description.setter
    def description(self, desc):
        self.__description = desc

    @lazy_property
    def encrypted(self):
        return self.__encrypted

    @lazy_property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @lazy_property
    def label(self):
        return self.__label

    @label.setter
    def label(self, label):
        self.__label = label

    @lazy_property
    def owning_account(self):
        return self.__owning_account

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
    def size_in_gb(self):
        return self.__size_in_gb

    @lazy_property
    def status(self):
        return self.__status

    @lazy_property
    def volume(self):
        return self.__volume

    @classmethod
    def all(cls, region_id=None):
        r = Resource(cls.path)
        if region_id is not None:
            params = {'regionId':region_id}
            c = r.get(params=params)
        else:
            c = r.get()
        if r.last_error is None:
            return [cls(i['snapshotId']) for i in c[cls.collection_name]]
        else:
            return r.last_error