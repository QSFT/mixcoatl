Read Me
=======

Mixcoatl was the father of Quetzalcoatl. His name means "Cloud Serpent". Fitting for a Python library for the DCM API.

Build Status
------------

.. image:: https://secure.travis-ci.org/enStratus/mixcoatl.png
        :target: http://travis-ci.org/enStratus/mixcoatl

Word of warning
~~~~~~~~~~~~~~~

This repository is not feature complete in that not all operations are
supported. At this point read access to all resources documented in the API doc
are working.

Usage notes
~~~~~~~~~~~

The following environment variables will need to be set:

- ``DCM_SECRET_KEY``
- ``DCM_ACCESS_KEY``

By default, API calls will be made against the DCM production SaaS and API
version ``2014-07-30``. These can be overridden with the following variables:

- ``DCM_ENDPOINT``
- ``DCM_API_VERSION``

When overriding the endpoint, it should be in the form:

``http[s]://api.endpoint.domain/api/enstratus/<api version>``

Note that setting both ``DCM_API_VERSION`` and ``DCM_ENDPOINT`` is not
cumulative. If you wish to use a private endpoint, it must include the version
in the URL.

- ``DCM_SSL_VERIFY``

By default, SSL certificate verification is required against HTTPS endpoint. To disable the verfication in case you use a self-signed certificate, set the value to 0. For example, ``DCM_SSL_VERIFY=0``

- ``DCM_DEBUG``

If you desire the ability to see debug information about specific calls, you may set `DCM_DEBUG=1`.  This will provide information such as headers, endpoint, and time to completion information.  Defaults to off.

**Configuration File(s) (Optional)**

A mixcoatl (~/.mixcoatl) directory can be created and contain files in the format of name.config.

Example:  Create a file called ~/.mixcoatl/MyDCM.config with the following format:

.. code-block:: bash

          DCM_ACCESS_KEY=EQJPYTDIXFIKDHUEZOPR
          DCM_SECRET_KEY=1Wy1pISoTLwL3ZqeJ5K6JWyTF8=klphOCIZ4C2pl
          DCM_ENDPOINT=https://your.dcm.endpoint/api/enstratus/2014-07-30
          DCM_SSL_VERIFY=0

``dcm-get``
-----------

``mixcoatl`` also ships with a small script for querying arbitrary objects via
the DCM API called ``dcm-get``. It's very minimal and only dumps the JSON
results of your query:

example:

.. code-block:: bash

        dcm-get admin/Job

.. code-block:: json

        {
          "jobs": []
        }

It can also accept query parameters in the form of a python ``dictionary`` (the
same format the ``requests`` library uses:

.. code-block:: bash

        dcm-get geography/DataCenter "{'regionId':19344}"

.. code-block:: json

        {
          "dataCenters": [
            {
              "dataCenterId": 64351, 
              "description": "us-west-2a", 
              "name": "us-west-2a", 
              "providerId": "us-west-2a", 
              "region": {
                "cloud": {
                  "cloudId": 1
                }, 
                "customer": {
                  "customerId": 14334
                }, 
                "description": "AWS Western United States (2)", 
                "jurisdiction": "US", 
                "name": "Oregon (us-west-2)", 
                "providerId": "us-west-2", 
                "regionId": 19344, 
                "status": "ACTIVE"
              }, 
              "status": "ACTIVE"
            }
          ]
        }

You'll need to set the environment variables as described above.

Lazy loading
------------

By default, any object you request by its id will not actually hit the
endpoint. Only when you request the object in full or a specific attribute,
will it actually make the API call. If the API call fails, the error will be
returned to you. You can always check the object's ``last_error`` attribute to
determine if it failed or not.

example:

.. code-block:: bash

   >>> from mixcoatl.geography.cloud import Cloud
   >>> c = Cloud(1)
   >>> # returns immediately
   >>> c.cloud_id
   1
   >>> c.name
   >>> # api call is made.
   u'Amazon Web Services'

``.all()``
----------

Returns an object list of resource results.

Pretty-printing
---------------

Every resource has a ``.pprint()`` function available which returns the
'prettyprinted' object

example:

.. code-block:: bash

   >>> from mixcoatl.geography.cloud import Cloud
   >>> c = Cloud(1)
   >>> c
   >>> c.pprint()
   >>> # pretty print representation

Other notes
~~~~~~~~~~~

In general, most resources should support read-only access. If you know the id
of an resource, you can simply request the resource by name with the id as a
parameter:

.. code-block:: bash

   >>> from mixcoatl.infrastructure.server import Server
   >>> s = Server(12345)
   >>> s

Importing resources generally follows the API directly i.e.:

.. code-block:: bash

   >>> from mixcoatl.scope.resource import ResourceName

For Firewalls
^^^^^^^^^^^^^

.. code-block:: bash

   >>> from mixcoatl.network.firewall import Firewall
   >>> f = Firewall(12345)
   >>> f

For Servers
^^^^^^^^^^^


.. code-block:: bash

   >>> from mixcoatl.infrastucture.server import Server
   >>> s = Server(12345)
   >>> s

Further Reading
~~~~~~~~~~~~~~~

For specific examples per resource, see the `wiki
<https://github.com/enStratus/mixcoatl/wiki>`_ or the `documentation
<http://enstratus.github.com/mixcoatl>`_
