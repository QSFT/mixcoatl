Mapping Patterns
----------------

This document covers common patterns, regardless of Resource type, that are
implemented and other general commonalities for using mixcoatl.

Module and Class Structure
~~~~~~~~~~~~~~~~~~~~~~~~~~

The module structure largely follows the conventions of the DCM API to minimize
disconnect between the API docs. To be more `pythonic` certain conventions and
transformations are done, however:

- camel-cased strings (such as attributes and query parameters) are replaced by
  snake-cased versions. 

- attributes with nested structures are returned as dictionaries

- CRUD operations are implemented primarily as class methods and, where
  appropriate, return an instance of the given resource type. These operations
  are named as snake-cased versions of the operation (i.e. `describeServer`
  becomes `describe_server()`.

- All attributes are normally lazy loaded except for the DCM unique identifier
  for a resource.

- All resources support calling `.all()`

- Resources can be requested in `basic` or `extended` form

- By default, all resources are returned in `extended` form which is a much
  longer API call but reduces the need to requery the API endpoint to denormalize
  certain attributes. Greedy fetch if you will.

- Resources always return a resource-specific exception with any API call error
  messages as the error message when available

- Results from `.all()` support returning either a `list` of resource objects
  or the ids only (`keys_only=True` parameter)

.. note::

   Regardless of asking for keys only or full objects, the same amount of data
   is returned as there is no DCM API mechanism for only returning ids. This is
   simply a convenience done on the python side.


Examples
~~~~~~~~

Using the `geography/DataCenter` API for instance:

Import Module
^^^^^^^^^^^^^

.. code-block:: bash

   >>> from mixcoatl.geography.data_center import DataCenter

Return details for a single data center
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   >>> dc = DataCenter(12345)
   >>> dc.data_center_id
   12345
   >>> dc.name

.. note::

   At this point, an actual API call is made to the DCM endpoints

List All Data Centers
^^^^^^^^^^^^^^^^^^^^^

.. note:: requires a `region_id`

.. code-block:: bash

   >>> DataCenter.all(region_id=12345)
   [{'data_center_id':1,...},{'data_center_id':2,...}]

List all data centers ('basic' detail)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   >>> DataCenter.all(region_id=12345, detail=`basic`)
   [{'data_center_id':1},{'data_center_id':2}]

Return IDs
^^^^^^^^^^

.. code-block:: bash

   >>> DataCenter.all(region_id=12345, keys_only=True)
   [1, 2, 3, 4, 5]

Creating New Resource
^^^^^^^^^^^^^^^^^^^^^

.. note::

   In this case, we show the classmethod `generate_api_key` which maps to
   the `generateApiKey` POST operation in the API.

.. code-block:: bash

   >>> from mixcoatl.admin.api_key import ApiKey
   >>> a = ApiKey.generate_api_key('my-test-apikey', 'a test api generated from mixcoatl')
   >>> a
   {'access_key':'ABCDEFGHIJKL',.....}
   >>> a.__class__
   mixcoatl.admin.api_key.ApiKey

Alternately, you can invoke this on an instance of `ApiKey`:

.. code-block:: bash

   >>> a = ApiKey()
   >>> a.name = 'another-test-key'
   >>> a.description = 'this is a test key'
   >>> a.create()
   >>> a
   {'access_key':'ABCDEFGHIKL',....}
