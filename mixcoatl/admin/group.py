from mixcoatl.resource import Resource
from mixcoatl.decorators.lazy import lazy_property

class Group(Resource):
    path = 'admin/Group'
    collection_name = 'groups'
    primary_key = 'groupId'

    def __init__(self, group_id=None, *args, **kwargs):
        Resource.__init__(self)
        self.__group_id = group_id

    @property
    def group_id(self):
        return self.__group_id

    @classmethod
    def all(cls, **kwargs):
        r = Resource(cls.path)
        if 'details' in kwargs:
            r.request_details = kwargs['details']
        else:
            r.request_details = 'basic'

        x = r.get()
        if r.last_error is None:
            return [cls(i['groupId']) for i in x[cls.collection_name]]
        else:
            return x.last_error