from mixcoatl.resource import Resource
from mixcoatl.decorators.lazy import lazy_property
from mixcoatl.utils import camelize

class TierAnalytics(Resource):
    PATH = 'analytics/TierAnalytics'
    COLLECTION_NAME = 'analytics'
    PRIMARY_KEY = 'tier_id'

    def __init__(self, tier_id=None, endpoint=None, *args, **kwargs):
        Resource.__init__(self, endpoint=endpoint)
        self.__tier_id = tier_id

    @property
    def tier_id(self):
        return self.__tier_id

    @lazy_property
    def data_points(self):
        return self.__data_points

    @lazy_property
    def period_start(self):
        return self.__period_start

    @lazy_property
    def period_end(self):
        return self.__period_end

    @lazy_property
    def interval_in_minutes(self):
        return self.__interval_in_minutes

    @classmethod
    def all(cls, tier_id, endpoint=None, **kwargs):
        r = Resource(cls.PATH+'/'+str(tier_id), endpoint=endpoint)
        if 'details' in kwargs:
            r.request_details = kwargs['details']
        else:
            r.request_details = 'basic'

        x = r.get()
        if r.last_error is None:
            return [cls(i[camelize(cls.PRIMARY_KEY)]) for i in x[cls.COLLECTION_NAME]]
        else:
            return r.last_error
