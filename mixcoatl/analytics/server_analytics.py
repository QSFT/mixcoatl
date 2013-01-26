"""
mixcoatl.analytics.server_analytics
-----------------------------------

Implements access to the enStratus ServerAnalytics API

.. note::

    Unlike other objects, ServerAnalytics only applies to a single server.
    There is no concept of 'all analytics across all servers'

"""
from mixcoatl.resource import Resource
from mixcoatl.decorators.lazy import lazy_property
from mixcoatl.utils import camelize

class ServerAnalytics(Resource):
    """Server analytics represent the performance of an individual server over
        a specified period of time

    :param server_id: The server represented in the analytics
    :type server_id: int.
    :param interval: The interval in minutes for the requested data points
    :type interval: int.
    :param period_start: The start time in UNIX milliseconds for the first datapoint
    :param period_start: int.
    :param period_end: The end time in UNIX milliseconds for the last datapoint
    :param period_end: int.
    """

    PATH = 'analytics/ServerAnalytics'
    COLLECTION_NAME = 'analytics'
    PRIMARY_KEY = 'server_id'

    def __init__(self, server_id=None, **kwargs):
        Resource.__init__(self, kwargs)
        self.__server_id = server_id

    @property
    def server_id(self):
        """`int` The unique enStratus id for the server in the request"""
        return self.__server_id

    @lazy_property
    def data_points(self):
        """`list` Data points representing a snapshot of the server's state
            at a given interval point
        """
        return self.__data_points

    @lazy_property
    def period_start(self):
        """`str` The actual date and time when the data set begins"""
        return self.__period_start

    @lazy_property
    def period_end(self):
        """`str` The date and time for the last data point in the response"""
        return self.__period_end

    @lazy_property
    def interval_in_minutes(self):
        """`int` The interval between data points in minutes delivered in this response"""
        return self.__interval_in_minutes

    @classmethod
    def all(cls, server_id, data_only=False, **kwargs):
        """Get all analytics for `server_id`

        :param server_id: The server represented in the analytics
        :type server_id: int.
        :param data_only: Return only the datapoints
        :type data_only: bool.
        :param interval: The interval in minutes for the requested data points
        :type interval: int.
        :param period_start: The start time in UNIX milliseconds for the first datapoint
        :param period_start: int.
        :param period_end: The end time in UNIX milliseconds for the last datapoint
        :param period_end: int.
        :returns: :class:`ServerAnalytics` or `list` of :attr:`data_points`
        """

        params = {}
        if 'interval' in kwargs:
            params['interval'] = kwargs['interval']
        if 'period_end' in kwargs:
            params['periodEnd'] = kwargs['period_end']
        if 'period_start' in kwargs:
            params['periodStart'] = kwargs['period_start']
        s = cls(server_id)
        if 'details' in kwargs:
            s.request_details = kwargs['details']
        else:
            s.request_details = 'basic'
        s.params = params
        s.load()
        if s.last_error is None:
            if data_only is True:
                return s.data_points
            else:
                return s
        else:
            raise ServerAnalyticsException(s.last_error)

class ServerAnalyticsException(BaseException): pass
