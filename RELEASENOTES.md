Mixcoatl Release Notes
==================
The CLI and Python library for interfacing with [Dell Cloud Manager](http://www.enstratius.com/)

![Mixcoatl Snake](http://mixcoatl.net/assets/images/mixcoatl_serpent.png)

0.11.1
=============

Release Date: 2015-07-17

The release allows you to access multiple DCM endpoints using mutiple API keys simultaneously. For example, within a
single python program you can compare the states of two DCM instances and also assume different roles by using different
API keys. The functionality is provided via the new [Endpoint][endpointL15] object,  which also provides facilities for
loading multiple endpoints from json files.

Here's an example of how you could use endpoints to identify servers simultaneously managed by two DCM instances:

```python
from mixcoatl.infrastructure.server import Server
from mixcoatl.resource import Endpoint

saas_endpoint = Endpoint(nickname="saas",
                         url="https://dcm.enstratius.com/api/enstratus/2015-05-25",
                         api_version="2015-05-25",
                         access_key="POIUYTREQ",
                         secret_key="ukjdf8HydvkLlki=4hfksj")

vagrant_endpoint = Endpoint(nickname="vagrant",
                            url="https://vagrant.vm/api/enstratus/2015-05-25",
                            api_version="2015-05-25",
                            access_key="LKJHGFDSAQ",
                            secret_key="ht748fbsd974d=t874gDFb",
                            ssl_verify=False)


saas_servers = Server.all(endpoint=saas_endpoint)
vagrant_servers = Server.all(endpoint=vagrant_endpoint)

# find all the servers managed by two DCM instances
for s in saas_servers:
    for v in vagrant_servers:
        if s.provider_id == v.provider_id:
            print "SaaS: %s Vagrant: %s, Provider ID %s" % (s.server_id, v.server_id, v.provider_id)
```

You can load load multiple endpoints from a simple json file:

```python
# load a dictionary of endpoints which you can index by nickname
endpoints = Endpoint.multiple_from_file("endpoints.json")

print endpoints['saas'].url
print endpoints['vagrant'].url
```

The `endpoints.json` looks like this:

```json
[
  {
    "nickname": "saas",
    "url": "https://dcm.enstratius.com/api/enstratus/2015-05-25",
    "api_version": "2015-05-25",
    "access_key": "POIUYTREQ",
    "secret_key": "ukjdf8HydvkLlki=4hfksj",
    "ssl_verify": true
  },
  {
    "nickname": "vagrant",
    "url": "https://vagrant.vm/api/enstratus/2015-05-25",
    "api_version": "2015-05-25",
    "access_key": "LKJHGFDSAQ",
    "secret_key": "ht748fbsd974d=t874gDFb",
    "ssl_verify": false
  }
]
```

Features
---------
- Added [#225][225]: multiple endpoint support using new Endpoint class
- Added live endpoint testing for server and volume operations using new Endpoint class
- Added loading of properties from json file for Server and Volume
- Added user friendly release notes
- Added [#233][233] add Job.latest_message() to force reloading of job message from the API.


Fixes
--------
- Fixed [#207][207]: allow configuration via python
- Fix pretty printing of dcm-describe-server

[207]:https://github.com/enStratus/mixcoatl/issues/207
[225]:https://github.com/enStratus/mixcoatl/pull/225
[233]:https://github.com/enStratus/mixcoatl/issues/233

[endpointL15]:[https://github.com/enStratus/mixcoatl/blob/feature/multi-endpoint/mixcoatl/resource.py#L15]


0.10.50.2
=============

Release Date: 2015-07-16

Fixes
------
- Fixed [#234][234]: fix missing import statement in dcm-list-datacenters. Thanks Jim Sander for the 
  report.

[234]:https://github.com/enStratus/mixcoatl/issues/234

0.10.50.1
=============

Release Date: 2015-07-10

Fixes
------
- Fixed [#216][216]: add network and subnet to the server class and dcm-create-server cli. Thanks to
  Eoin Kennet at HEAnet for the bug report.

[216]:https://github.com/enStratus/mixcoatl/issues/216

0.10.50
=============

Release Date: 2015-07-07

Features
--------
- Added [#202][202]: dcm-create-user support for ssh key
- Added [#214][214]: handsfree installer support for ldap dirsync, saml config, private cloud pricing, and marketplace setup
- Added [#229][229]: runtime adding of access methods for new API attributes

Fixes
------
- Fixed [#217][217] [#221][221]:  some dcm-* cli tools crash when pretty printing missing attributes
- Fixed [#226][226]: dcm-list-volumes not reporting server ID
- Fixed [#212][212]: default DCM_ENDPOINT for dcm.enstratius.com

[202]:https://github.com/enStratus/mixcoatl/pull/202
[214]:https://github.com/enStratus/mixcoatl/pull/214
[229]:https://github.com/enStratus/mixcoatl/issues/229
[217]:https://github.com/enStratus/mixcoatl/pull/217
[221]:https://github.com/enStratus/mixcoatl/issues/221
[226]:https://github.com/enStratus/mixcoatl/issues/226
[229]:https://github.com/enStratus/mixcoatl/issues/229
[212]:https://github.com/enStratus/mixcoatl/pull/212





