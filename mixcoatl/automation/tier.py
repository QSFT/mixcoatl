from mixcoatl.resource import Resource
from mixcoatl.decorators.lazy import lazy_property
from mixcoatl.decorators.validations import required_attrs
from mixcoatl.utils import camelize, camel_keys
from mixcoatl.admin.job import Job

import json
import time

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
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, b):
        # pylint: disable-msg=C0111,W0201
        self.__budget = b

    @lazy_property
    def breach_increment(self):
        return self.__breach_increment

    @breach_increment.setter
    def breach_increment(self, b):
        self.__breach_increment = b

    @lazy_property
    def breach_period_in_minutes(self):
        return self.__breach_period_in_minutes

    @breach_period_in_minutes.setter
    def breach_period_in_minutes(self,b):
        self.__breach_period_in_minutes = b

    @lazy_property
    def cooldown_period_in_minutes(self):
        return self.__cooldown_period_in_minutes

    @cooldown_period_in_minutes.setter
    def cooldown_period_in_minutes_in_minutes(self, m):
        self.__cooldown_period_in_minutes = m

    @lazy_property
    def deployment(self):
        return self.__deployment

    @deployment.setter
    def deployment(self, d):
        # pylint: disable-msg=C0111,W0201
        self.__deployment = d

    @lazy_property
    def label(self):
        return self.__label

    @label.setter
    def label(self, l):
        self.__label = l

    @lazy_property
    def description(self):
        return self.__description

    @description.setter
    def description(self, d):
        # pylint: disable-msg=C0111,W0201
        self.__description = d

    @lazy_property
    def last_breach_change_timestamp(self):
        return self.__last_breach_change_timestamp

    @lazy_property
    def lower_cpu_threshold(self):
        return self.__lower_cpu_threshold

    @lower_cpu_threshold.setter
    def lower_cpu_threshold(self, c):
        self.__lower_cpu_threshold = c

    @lazy_property
    def lower_ram_threshold(self):
        return self.__lower_ram_threshold

    @lower_ram_threshold.setter
    def lower_ram_threshold(self, l):
        self.__lower_ram_threshold = l

    @lazy_property
    def minimum_servers(self):
        return self.__minimum_servers

    @minimum_servers.setter
    def minimum_servers(self, m):
        self.__minimum_servers = m

    @lazy_property
    def maximum_servers(self):
        return self.__maximum_servers

    @maximum_servers.setter
    def maximum_servers(self, m):
        self.__maximum_servers = m

    @lazy_property
    def name(self):
        return self.__name

    @name.setter
    def name(self, n):
        # pylint: disable-msg=C0111,W0201
        self.__name = n

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

    @upper_cpu_threshold.setter
    def upper_cpu_threshold(self, u):
        self.__upper_cpu_threshold = u

    @lazy_property
    def upper_ram_threshold(self):
        return self.__upper_ram_threshold

    @upper_ram_threshold.setter
    def upper_ram_threshold(self, u):
        self.__upper_ram_threshold = u

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

    @required_attrs(['name',
										 'description',
										 'budget',
										 'deployment',
										 'minimum_servers',
										 'maximum_servers',
										 'breach_period_in_minutes',
										 'cooldown_period_in_minutes',
										 'lower_cpu_threshold',
										 'upper_cpu_threshold',
										 'lower_ram_threshold',
										 'upper_ram_threshold' ])

    def create(self, callback=None):
        """Creates a new tier

        :param callback: Optional callback to send the resulting :class:`Job`
        :raises: :class:`TierCreationException`
        """

        parms = [{'budget': self.budget,
                    'deployment': {'deploymentId': self.deployment},
                    'description': self.description,
                    'name': self.name,
                    'minimumServers': self.minimum_servers,
                    'maximumServers': self.maximum_servers,
                    'breachIncrement': self.breach_increment,
                    'breachPeriodInMinutes': self.breach_period_in_minutes,
                    'cooldownPeriodInMinutes': self.cooldown_period_in_minutes,
                    'lowerCpuThreshold': self.lower_cpu_threshold,
                    'upperCpuThreshold': self.upper_cpu_threshold,
                    'lowerRamThreshold': self.lower_ram_threshold,
                    'upperRamThreshold': self.upper_ram_threshold}]

        payload = {'addTier':camel_keys(parms)}

        response=self.post(data=json.dumps(payload))
        if self.last_error is None:
            self.load()
            return response
        else:
            raise TierCreationException(self.last_error)

class TierException(BaseException): pass

class TierCreationException(TierException):
    """Tier Creation Exception"""
    pass
