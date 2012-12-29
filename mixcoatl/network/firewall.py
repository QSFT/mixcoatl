from mixcoatl.resource import Resource
from mixcoatl.decorators.lazy import lazy

@lazy(key='firewall_id')
class Firewall(Resource):
    path = 'network/Firewall'
    collection_name = 'firewalls'

    def __init__(self, firewall_id = None, *args, **kwargs):
        Resource.__init__(self)
        if firewall_id is None:
            pass
        self.__firewall_id = firewall_id

    @property
    def firewall_id(self):
        return self.__firewall_id

    @property
    def status(self):
        return self.__status

    @property
    def label(self):
        return self.__label

    @property
    def owning_account(self):
        return self.__owning_account

    @property
    def name(self):
        return self.__name

    @property
    def owning_user(self):
        return self.__owning_user

    @property
    def description(self):
        return self.__description

    @property
    def cloud(self):
        return self.__cloud

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
    def budget(self):
        return self.__budget

    @property
    def customer(self):
        return self.__customer

    @classmethod
    def all(cls, region_id):
        from mixcoatl.utils import uncamel_keys
        r = Resource(cls.path)
        r.request_details = 'extended'
        params = {'regionId':region_id}
        c = r.get(params=params)
        if r.last_error is None:
            return [cls(i['firewallId']) for i in c[cls.collection_name]]
            #return c
        else:
            return r.last_error

    def get_firewall(self, firewall_id):
        p = self.path+"/"+str(firewall_id)
        return self.get(path=p)

    def del_firewall(self, firewall_id, reason):
        p = self.path+"/"+str(firewall_id)
        params = {'reason':reason}
        return self.delete(path=p, params=params)

def list_all(region_id):
    f = Firewall()
    firewalls = f.get(params={'regionId':region_id})
    if f.last_error is None:
        return firewalls['firewalls']
    else:
        return f.last_error

def show(firewall_id):
    f = Firewall()
    firewall = f.get_firewall(firewall_id)
    if f.last_error is None:
        return firewall['firewalls'][0]
    else:
        return f.last_error

def create(region_id, budget_id, wait=False):
    f = Firewall()
    now = int(round(time.time() * 1000))
    whoami = os.environ['USER']

    payload = {'addFirewall':[{
        'region':{'regionId':region_id},
        'budget':budget_id,
        'description':'mixcoatl-generated firewall',
        'name':'mixcoatl-'+whoami+'-'+str(now)}]}

    f.post(data=json.dumps(payload))
    if f.last_error is None:
        if wait is True:
            w = wait_for_job(f.current_job)
            if w == True:
                fwid = job.get(f.current_job)['message']
                return show(fwid)
            else:
                return job.get(f.current_job)
        else:
            return f.current_job
    else:
        return f.last_error
