from mixcoatl.resource import Resource
from mixcoatl.admin.job import Job
from mixcoatl.utils import camelize, camel_keys, uncamel_keys
from mixcoatl.decorators.validations import required_attrs
from mixcoatl.decorators.lazy import lazy_property
import json, sys, time

class RelationalDatabase(Resource):
    """A relational database is a database as a service offering supporting a relational model."""
    PATH = 'platform/RelationalDatabase'
    COLLECTION_NAME = 'relational_databases'
    PRIMARY_KEY = 'relational_database_id'

    def __init__(self, relational_database_id=None, *args, **kwargs):
        Resource.__init__(self)
        self.__relational_database_id = relational_database_id

    @property
    def relational_database_id(self):
        """`int` - The DCM ID of this relational_database"""
        return self.__relational_database_id

    @lazy_property
    def label(self):
        """`str` - The label assigned to the relational_database"""
        return self.__label

    @label.setter
    def label(self, l):
        self.__label = l

    @lazy_property
    def account(self):
        """`int` - The DCM account under which the relational database is registered."""
        return self.__account

    @account.setter
    def account(self, a):
        self.__account = a

    @lazy_property
    def admin_password(self):
        """`str` - The password of an admin user of the database."""
        return self.__admin_password

    @admin_password.setter
    def admin_password(self, p):
        self.__admin_password = p

    @lazy_property
    def admin_user(self):
        """`str` - The username of an admin user of the database."""
        return self.__admin_user

    @admin_user.setter
    def admin_user(self, u):
        self.__admin_user = u

    @lazy_property
    def allocated_storage_in_gb(self):
        """`int` - The amount of storage allocated to the relational database in GB."""
        return self.__allocated_storage_in_gb

    @allocated_storage_in_gb.setter
    def allocated_storage_in_gb(self, g):
        self.__allocated_storage_in_gb = g

    @lazy_property
    def backup_window(self):
        """`str` - The time windows when automated snapshot backups happen."""
        return self.__backup_window

    @lazy_property
    def cloud(self):
        """`dict` - The cloud provided where the instance is located."""
        return self.__cloud

    @lazy_property
    def created_timestamp(self):
        """`str` - Creation timestamp of the database."""
        return self.__created_timestamp

    @lazy_property
    def current_recovery_point(self):
        """`str` - Specifies the latest time to which the database can be restored with point-in-time restore."""
        return self.__current_recovery_point

    @lazy_property
    def customer(self):
        """`dict` - The customer account for the relational_database."""
        return self.__customer

    @lazy_property
    def data_center(self):
        """`dict` - The specific datacenter where the instance is located."""
        return self.__data_center

    @data_center.setter
    def data_center(self, d):
        self.__data_center = {u'data_center_id': d}

    @lazy_property
    def description(self):
        """`str` - The description of the relational_database"""
        return self.__description

    @description.setter
    def description(self, d):
        self.__description = d

    @lazy_property
    def dns_name(self):
        """`str` - A DNS name associated with the relational database server."""
        return self.__dns_name

    @description.setter
    def dns_name(self, d):
        self.__dns_name = d

    @lazy_property
    def engine(self):
        """ `enum` - The database engine powering this relational database. examples: MYSQL, ORACLE11G"""
        return self.__engine

    @engine.setter
    def engine(self, e):
        self.__engine = e

    @lazy_property
    def ha(self):
        """`bool` - Indicates if high availability is enabled."""
        return self.__ha

    @ha.setter
    def ha(self, h):
        self.__ha = h

    @lazy_property
    def maintenance_window(self):
        """`str` - The time window when maintenance is allowed to happen."""
        return self.__maintenance_window

    @lazy_property
    def name(self):
        """`str` - A user-friendly name to describe this relational database."""
        return self.__name

    @name.setter
    def name(self, n):
        self.__name = n

    @lazy_property
    def owning_group(self):
        """`str` - The group who has ownership over this relational database."""
        return self.__owning_group

    @lazy_property
    def owning_user(self):
        """`str` - The user who is the owner of this relational database."""
        return self.__owning_user

    @lazy_property
    def port(self):
        """`int` - The port number the database is running on."""
        return self.__port

    @port.setter
    def port(self, n):
        self.__port = n

    @lazy_property
    def provider_id(self):
        """`str` - How this relational database is identified by cloud provider."""
        return self.__provider_id

    @lazy_property
    def rdbms_product(self):
        """`int` - The relational database product associated with this database."""
        return self.__rdbms_product

    @rdbms_product.setter
    def rdbms_product(self, r):
        self.__rdbms_product = r

    @lazy_property
    def region(self):
        """`dict` - The region this database is running in."""
        return self.__region

    @region.setter
    def region(self, r):
        self.__region = r

    @lazy_property
    def status(self):
        """`str` - The current status of the database *(i.e. `RUNNING` or `PAUSED`)*."""
        return self.__status

    def reload(self):
        """Reload resource data from API calls"""
        if self.relational_database_id is not None:
            self.load()
        elif self.current_job is None:
            self.load()
        else:
            if Job.wait_for(self.current_job):
                job = Job(self.current_job)
                self.__relational_database_id = job.message
                self.load()
            else:
                return self.last_error

    @required_attrs(['relational_database_id'])
    def destroy(self, reason='no reason provided'):
        """Terminate relational_database instance with reason :attr:`reason`

        :param reason: The reason for terminating the relational_database
        :type reason: str.
        :returns: bool -- Result of API call
        """
        p = self.PATH+"/"+str(self.relational_database_id)
        qopts = {'reason':reason}
        return self.delete(p, params=qopts)

    @required_attrs(['name', 'description', 'port', 'engine', 'rdbms_product', 'data_center',
                     'allocated_storage_in_gb', 'admin_user', 'admin_password'])
    def launch(self, callback=None):
        """Launches a relational database with the configured parameters

        >>> def cb(j): print(j)
        >>> r = RelationalDatabase()
        >>> r.name = 'relational_database-1-test'
        >>> r.description = 'my first database launch'
        >>> r.port = 3306
        >>> r.engine = 'MYSQL'
        >>> r.rdbms_product = ''
        >>> r.data_center = 3451
        >>> r.allocated_storage_in_gb = 5
        >>> r.admin_user = 'root'
        >>> r.admin_password = 'adminpassword'
        >>> r.launch(callback=cb)

        :param callback: Optional callback to send the results of the API call
        :type callback: func.
        :returns: int -- The job id of the launch request
        :raises: :class:`RelationalDatabaseLaunchException`, :class:`mixcoatl.decorators.validations.ValidationException`
        """
#        optional_attrs = ['vlan', 'firewalls', 'keypair', 'label', 'cmAccount', 'environment', 'cm_scripts', 'p_scripts', 'volumeConfiguration']
#        if self.relational_database_id is not None:
#            raise RelationalDatabaseLaunchException('Cannot launch an already running relational_database: %s' % self.relational_database_id)
#
#        payload = {'launch':
#                    [{
#                        'productId': self.provider_product_id,
#                        'budget': self.budget,
#                        'machineImage': camel_keys(self.machine_image),
#                        'description': self.description,
#                        'name': self.name,
#                        'dataCenter': camel_keys(self.data_center)
#                    }]}
#
#        for oa in optional_attrs:
#            try:
#                if getattr(self, oa) is not None:
#                    if oa == 'cm_scripts':
#                        payload['launch'][0].update({'scripts':getattr(self, oa)})
#                    elif oa == 'p_scripts':
#                        payload['launch'][0].update({'personalities':getattr(self, oa)})
#                    elif oa == 'volumeConfiguration':
#                        payload['launch'][0].update({'volumeConfiguration':{u'raidlevel':'RAID0', u'volumeCount':1, u'volumeSize':2, u'fileSystem':'ext3', u'mountPoint':'/mnt/data'}})
#                    elif oa == 'vlan':
#                        payload['launch'][0].update({'vlan':camel_keys(getattr(self, oa))})
#                    else:
#                        payload['launch'][0].update({oa:getattr(self, oa)})
#            except AttributeError:
#                pass

        self.post(data=json.dumps(payload))
        if self.last_error is None:
            if callback is not None:
                callback(self.current_job)
            else:
                return self.current_job
        else:
            raise RelationalDatabaseLaunchException(self.last_error)

    def wait_for(self, status='RUNNING', callback = None):
        """Blocks execution until the current relational_database has status of :attr:`status`

        :param status: The status to expect before continuing *(i.e. `RUNNING` or `PAUSED`)*
        :type status: str.
        :param callback: Optional callback to be called with the final :class:`RelationalDatabase`` when ``status`` is reached
        :type callback: func.
        :raises: `RelationalDatabaseException`
        """
        if self.relational_database_id is None:
            raise RelationalDatabaseException('Must be called with an existing relational_database.')
        initial_status = self.status
        if self.last_error is None:
            if initial_status == status:
                return self
            while self.status != status:
                time.sleep(5)
                self.load()
                if self.last_error is not None:
                    raise RelationalDatabaseException(self.last_error)
                else:
                    continue
            if callback is not None:
                callback(self)
            else:
                return self

    @classmethod
    def all(cls, **kwargs):
        r = Resource(cls.PATH)
        params = {}
        if 'detail' in kwargs:
            r.request_details = kwargs['detail']
        else:
            r.request_details = 'basic'

        if 'keys_only' in kwargs:
            keys_only = kwargs['keys_only']
        else:
            keys_only = False

        if 'params' in kwargs:
            params = kwargs['params']

        x = r.get(params=params)
        if r.last_error is None:
            if keys_only is True:
                results = [i[camelize(cls.PRIMARY_KEY)] for i in x[cls.COLLECTION_NAME]]
            else:
                results = [type(cls.__name__, (object,), i) for i in uncamel_keys(x)[cls.COLLECTION_NAME]]
            return results
        else:
            raise RelationalDatabaseException(r.last_error)


class RelationalDatabaseException(BaseException):
    pass


class RelationalDatabaseLaunchException(RelationalDatabaseException):
    pass
