# Mixcoatl
Mixcoatl was the father of Quetzalcoatl. His name means "Cloud Serpent". Fitting for a Python library for the enStratus API.

## Word of warning
This repo is not feature complete. Preference is being given to API interactions that are most useful in conjuction with Fabric:

- Managing running instances
- Managing firewalls
- Interacting with Jobs
- Support for the above (budget codes, regions, datacenters)

Also the final API is being fleshed out based on how it is being used. There are no proper objects for the various resource types per se. It is, however, usable.

Right now most things return either a `dict` or a `bool` based on the task. In the future, these will return proper objects i.e. a `Server` object or a `Firewall` object

# Example usages
Just a few quick example usages.

## Servers
Some server interaction

### Listing all servers
Returns a list of dicts each representing a server

```python
from mixcoatl.infrastructure import server
server.list_all()
>>> [{u'agentVersion': 0,
 u'budget': 10287,
 u'cloud': {u'cloudId': 1},
 u'customer': {u'customerId': 14334},
 u'dataCenter': {u'dataCenterId': 64351},
 u'description': u'mixcoatl server launch',
 u'machineImage': {u'machineImageId': 284555},
 u'name': u'mixcoatl-jvincent-1356376972009',
 u'platform': u'UNKNOWN',
 u'privateIpAddresses': [u'10.252.192.45'],
 u'providerId': u'i-5e3bf56c',
 u'providerProductId': u't1.micro',
 u'publicIpAddress': u'50.112.61.79',
 u'region': {u'regionId': 19344},
 u'serverId': 334003,
 u'startDate': u'2012-12-24T19:22:53.000+0000',
 u'status': u'RUNNING'}]
```

### Getting a server
Returns a dict representation of the request server
```python
from mixcoatl.infrastructure import server
server.get(334003)
>>> {u'agentVersion': 0,
 u'budget': 10287,
 u'cloud': {u'cloudId': 1},
 u'customer': {u'customerId': 14334},
 u'dataCenter': {u'dataCenterId': 64351},
 u'description': u'mixcoatl server launch',
 u'machineImage': {u'machineImageId': 284555},
 u'name': u'mixcoatl-jvincent-1356376972009',
 u'platform': u'UNKNOWN',
 u'privateIpAddresses': [u'10.252.192.45'],
 u'providerId': u'i-5e3bf56c',
 u'providerProductId': u't1.micro',
 u'publicIpAddress': u'50.112.61.79',
 u'region': {u'regionId': 19344},
 u'serverId': 334003,
 u'startDate': u'2012-12-24T19:22:53.000+0000',
 u'status': u'RUNNING'}
```

### Launching a server
Returns either the job id for the launch operation or, if `wait` is set to true, the server dict when complete.

```python
# blocking launch
from mixcoatl.infrastructure import server
# params are (machine image id, provider product name, datacenter id, firewall id, optional keypair name, optional wait)
server.launch(284555, 'm1.large', 64351, 116387, 'jv-cse-uswest2-kp', True)
# After job is complete
>>> {u'agentVersion': 0,
 u'budget': 10287,
 u'cloud': {u'cloudId': 1},
 u'customer': {u'customerId': 14334},
 u'dataCenter': {u'dataCenterId': 64351},
 u'description': u'mixcoatl server launch',
 u'machineImage': {u'machineImageId': 284555},
 u'name': u'mixcoatl-jvincent-1356377595244',
 u'platform': u'UNKNOWN',
 u'privateIpAddresses': [u'10.252.43.205'],
 u'providerId': u'i-5239f760',
 u'providerProductId': u't1.micro',
 u'publicIpAddress': u'50.112.59.140',
 u'region': {u'regionId': 19344},
 u'serverId': 334367,
 u'startDate': u'2012-12-24T19:33:19.000+0000',
 u'status': u'RUNNING'}
```

```python
# non-blocking launch (returns job id)
server.launch(284555, 'm1.large', 64351, 116387, 'jv-cse-uswest2-kp')
>>> 76113
from mixcoatl.admin import job
job.get(76113)
>>> {u'description': u'Launch Server mixcoatl-jvincent-1356377753158',
 u'jobId': 76113,
 u'startDate': u'2012-12-24T19:35:54.255+0000',
 u'status': u'RUNNING'}
```

### Terminating a server
Returns `True` or `False` depending on result
```python
server.terminate(334367)
>>> True
job.list()
>>> [{u'description': u'Terminate 334367',
  u'jobId': 76114,
  u'startDate': u'2012-12-24T19:38:26.552+0000',
  u'status': u'RUNNING'}]
from mixcoatl.utils import wait_for_job
# block until job is complete
wait_for_job(76114)
>>> True
job.get(76114)
>>> {u'description': u'Terminate 334367',
 u'endDate': u'2012-12-24T19:40:04.294+0000',
 u'jobId': 76114,
 u'startDate': u'2012-12-24T19:38:26.552+0000',
 u'status': u'COMPLETE'}
```
