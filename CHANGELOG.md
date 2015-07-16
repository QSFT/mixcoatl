Mixcoatl ChangeLog
==================

![Mixcoatl Snake](http://mixcoatl.net/assets/images/mixcoatl_serpent.png)

Unreleased
===========
Placeholder for changes pending in the next release

Release Date: pending

You can now configure multiple alternate DCM endpoint via a new python object Endpoint.

Features
---------
- Added [#225][225]: multiple endpoint support

Fixes
--------
- Fixed [#207][207]: allow configuration via python

[207]:https://github.com/enStratus/mixcoatl/issues/207
[225]:https://github.com/enStratus/mixcoatl/pull/225


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





