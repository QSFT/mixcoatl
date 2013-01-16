from mixcoatl.resource import Resource
from mixcoatl.decorators.lazy import lazy_property
from mixcoatl.utils import camelize

class Tier(Resource):
    PATH = 'automation/Tier'
    COLLECTION_NAME = 'tiers'
    PRIMARY_KEY = 'tier_id'

    def __init__(self, tier_id=None, *args, **kwargs):
        Resource.__init__(self)
        self.__tier_id = tier_id

    @property
    def tier_id(self):
        return self.__tier_id

    @lazy_property
    def breach_increment(self):
        return self.__breach_increment

    @lazy_property
    def breach_period_in_minutes(self):
        return self.__breach_period_in_minutes

    @lazy_property
    def cooldown_period_in_minutes(self):
        return self.__cooldown_period_in_minutes

    @lazy_property
    def deployment(self):
        return self.__deployment

    @lazy_property
    def label(self):
        return self.__label

    @lazy_property
    def description(self):
        return self.__description

    @lazy_property
    def last_breach_change_timestamp(self):
        return self.__last_breach_change_timestamp

    @lazy_property
    def lower_cpu_threshold(self):
        return self.__lower_cpu_threshold

    @lazy_property
    def lower_ram_threshold(self):
        return self.__lower_ram_threshold

    @lazy_property
    def maximum_servers(self):
        return self.__maximum_servers

    @lazy_property
    def minimum_servers(self):
        return self.__minimum_servers

    @lazy_property
    def name(self):
        return self.__name

    @lazy_property
    def removable(self):
        return self.__removable

    @lazy_property
    def scaling_rules(self):
        return self.__scaling_rules

    @lazy_property
    def status(self):
        return self.__status

    @lazy_property
    def upper_cpu_threshold(self):
        return self.__upper_cpu_threshold

    @lazy_property
    def upper_ram_threshold(self):
        return self.__upper_ram_threshold

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
