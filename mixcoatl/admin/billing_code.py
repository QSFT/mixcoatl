from mixcoatl.resource import Resource
from mixcoatl.decorators.lazy import lazy_property

class BillingCode(Resource):

    path = 'admin/BillingCode'
    collection_name = 'billingCodes'
    primary_key = 'billing_code_id'

    def __init__(self, billing_code_id = None, *args, **kwargs):
        Resource.__init__(self)
        self.__billing_code_id = billing_code_id

    @property
    def billing_code_id(self):
        return self.__billing_code_id

    @lazy_property
    def budget_state(self):
        return self.__budget_state
    
    @lazy_property
    def current_usage(self):
        return self.__current_usage
    
    @lazy_property
    def customer(self):
        return self.__customer
    
    @lazy_property
    def description(self):
        return self.__description
    
    @lazy_property
    def finance_code(self):
        return self.__finance_code
    
    @lazy_property
    def name(self):
        return self.__name 
    
    @lazy_property
    def projected_usage(self):
        return self.__projected_usage
    
    @lazy_property
    def status(self):
        return self.__status

    @classmethod
    def all(cls, **kwargs):
        r = Resource(cls.path)
        if 'details' in kwargs:
            r.request_details = kwargs['details']
        else:
            r.request_details = 'basic'

        x = r.get()
        if r.last_error is None:
            return [cls(i['billingCodeId']) for i in x[cls.collection_name]]
        else:
            return x.last_error