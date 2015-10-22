Mixcoatl Release Notes
==================
The CLI and Python library for interfacing with [Dell Cloud Manager](http://www.enstratius.com/)

![Mixcoatl Snake](http://mixcoatl.net/assets/images/mixcoatl_serpent.png)


1.4.2
=====

Release Date 2015-10-22

Use with DCM: 10.X, 11.X

Quick fix release for [#302][302].

Fixes
-----
- [#302][302] AttributeError with missing owning_user

[302]:https://github.com/enStratus/mixcoatl/issues/302

1.4.1
=====

Release Date 2015-10-21

Use with DCM: 10.X, 11.X

The [dcm-list-servers][dcm-list-servers] CLI tool now has a `--verbose` flag that gives you more detailed view of
current servers. This avoids the need, in many cases, to make a separate call to `dcm-describe-server` to get more
information about an individual server.

Features
--------
- [#292][292] dcm-put and dcm-post produces useful json parsing error messages.

Fixes
-----
- [#296][296] crash bug in dcm-list-subscriptions

[292]:https://github.com/enStratus/mixcoatl/issues/292
[296]:https://github.com/enStratus/mixcoatl/issues/296
[dcm-list-servers]:http://docs.mixcoatl.net/en/stable/cli_tools/dcm-list-servers.html

1.4.0
=====

Release Date 2015-10-05

Use with DCM: 10.X, 11.X

This [dcm-list-server-products][dcm-list-server-products] tool can now filter by external cloud provider region ID and
not just DCM internal IDs. This allows you filter server products like this:
`dcm-list-server-products --regionpid us-east-1`. We also now provide more useful json formatting error messages for
`dcm-put` and `dcm-post`, which is especially useful for developers working out how to format their DCM API payloads.

Features
--------
- [#281][281] dcm-put and dcm-post produces useful json parsing error messages. 
- [#286][286] dcm-list-server-products handles provider region IDs
- [#287][287] dcm-list-server-products displays CPU architecture

[281]:https://github.com/enStratus/mixcoatl/issues/281
[286]:https://github.com/enStratus/mixcoatl/issues/286
[287]:https://github.com/enStratus/mixcoatl/issues/287
[dcm-list-server-products]:http://docs.mixcoatl.net/en/stable/cli_tools/dcm-list-server-products.html

1.3.2
=====

Release Date 2015-09-24

Use with DCM: 10.X, 11.X

This release is a bug fix for [#282][282].

Fixes
-----

- [#282][282] dcm-list-jobs ignores --job-id

[282]:https://github.com/enStratus/mixcoatl/issues/282

1.3.1
=====

Release Date 2015-09-15

Use with DCM: 10.X, 11.X

This release is a quick fix for critical bug [#278][278].

Fixes
-----

- [#278][278] broken dcm-detach-volume 

[278]:https://github.com/enStratus/mixcoatl/issues/278

1.3.0
=====

Release Date 2015-09-08

Use with DCM: 10.X, 11.X

The dcm-create-account tool is now easier to use thanks to more reasonable defaults. Newly created accounts are added to
default admin customer and group. We also include a number of fixes to the CLI to make it easier to understand what
flags are required vs optional.

Features
--------
- [#270][270] [#271][271] , dcm-create-account easier to use with better defaults



Fixes
-----
- [#186][186] dcm-create-account accepts customer_id
- [#266][266],[#272][272] dcm-list-api-version didn't work with unsigned server certificates
- [#235][235] CLI tools don't differentiate between optional and required arguments
- [#274][274] fix broken dcm-update-group


[186]:https://github.com/enStratus/mixcoatl/issues/186
[235]:https://github.com/enStratus/mixcoatl/issues/235
[266]:https://github.com/enStratus/mixcoatl/issues/266
[270]:https://github.com/enStratus/mixcoatl/issues/270
[271]:https://github.com/enStratus/mixcoatl/pull/271
[272]:https://github.com/enStratus/mixcoatl/pull/272
[274]:https://github.com/enStratus/mixcoatl/issues/274

1.2.0
=====

Release Date 2015-08-28

Use with DCM: 10.X, 11.X

The release adds a new CLI utility [`dcm-update-server-group`][dcm-update-server-group] that allows you to easily change
the owning group of a sever. It also includes a number of bug fixes.

Features
--------
- [#263][263] dcm-update-server-group cli utility (thanks Brian Williams)

Fixes
-----
- [#264][264] Endpoint threading missing in firewall (thanks John Bresnahan)
- [#265][265] dcm-create-account crash bug (report from Shaun Marshall)
- [#268][268] documentation deficiencies 


[263]:https://github.com/enStratus/mixcoatl/pull/263
[264]:https://github.com/enStratus/mixcoatl/pull/264
[265]:https://github.com/enStratus/mixcoatl/issues/265
[268]:https://github.com/enStratus/mixcoatl/issues/268
[dcm-update-server-group]:http://docs.mixcoatl.net/en/stable/cli_tools/dcm-update-server-group.html


1.1.1
=====

Release Date 2015-08-10

Use with DCM: 10.X, 11.X

Primarily a documentation improvement release. Release not pushed to PyPI, but pushed to [ReadTheDocs.org][rtd].

Fixes
-----
- [#260][260] Several documentation deficiencies

[260]:https://github.com/enStratus/mixcoatl/pull/260

1.1.0
=====

Release Date: 2015-07-30

Use with DCM: 10.X, 11.X

In this release we move our documentation onto [docs.mixcoatl.net][rtd] and hosted with readthedocs.org. The docs are
versioned and automatically generated as the code is committed to the repository. All of our docs are consolidated here
as well, which should lead to better search engine results over time.

We have some new additions:

    $ dcm-describe-license
    Licensee: Dell Cloud Manager Production SaaS
    Days Until Expiration: 9819
    Expiration Date: 2042-06-18T16:07:21.311+0000
    Server Limit: 0
    License Valid: True
    
and dcm-list-api-versions which has been updated to be able to tell you which api version you are currently using, which
is the latest and what versions are available:

    $ dcm-list-api-versions --help
    usage: dcm-list-api-versions [-h] [--active | --latest | --supported]
                                 [--json | --xml | --csv]


We have also cut out BeautifulSoup and termcolor python dependencies, in the process of getting ready for deb and rpm
vendor native packaging.

Features
---------
- Add [#251][251] ability to get avalable API versions to the Endpoint class
- Add [#213][213] new command dcm-describe-license 


Fixes
-------
- Fixed [#250][250] InsecurePlatformWarning problem coming from request module
- Fixed [#252][252] Drop termcolor as dependency
- Fixed [#255][255] replace dicttoxml with xmltodict
- Fixed [#159][159] fix dcm-list-server-terminate
- Improved some faulty install docs (thanks Syam Puchakayala)

[159]:https://github.com/enStratus/mixcoatl/issues/159
[213]:https://github.com/enStratus/mixcoatl/issues/213
[250]:https://github.com/enStratus/mixcoatl/issues/250
[251]:https://github.com/enStratus/mixcoatl/issues/251
[252]:https://github.com/enStratus/mixcoatl/issues/252
[255]:https://github.com/enStratus/mixcoatl/issues/255
[rtd]:http://docs.mixcoatl.net



1.0.3
=====

Release Date: 2015-07-28

Use with DCM: 10.X, 11.X

- Changes to Install documentation only

1.0.2
=====

Release Date: 2015-07-23

Use with DCM: 10.X, 11.X

Fixes
-----

- Sphinx document generation for the move to readthedocs.org.

Note: changes in this release do not affect the python codebase, documentation only.


1.0.1
=======

Release Date: 2015-07-17

Use with DCM: 10.X, 11.X

Fixes
-----

- Broken `mixcoatl --version` function because of non pypi conforming A.B.C.D format.  

1.0.0
=============

Release Date: 2015-07-17

Use with DCM: 10.X, 11.X

Welcome to the 1.0.0 release. Mixcoatl will now follow semantic versioning with compatibility to DCM releases
documented. This release allows you to access multiple DCM endpoints using mutiple API keys simultaneously. For example,
within a single python program you can compare the states of two DCM instances and also assume different roles by using
different API keys. The functionality is provided via the new [Endpoint][endpointL15] object,  which also provides
facilities for loading multiple endpoints from json files.

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





