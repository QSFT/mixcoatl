.. raw:: latex
  
      \newpage

.. _dcm_list_storage_objects:

dcm-list-storage-objects
------------------------

List storage objects.

Description
~~~~~~~~~~~

Returns a list of storage objects.

Syntax
~~~~~~

.. program-output:: dcm-list-storage-objects -h

Options
~~~~~~~

+--------------------+---------------------------------------------------------------+
| Option             | Description                                                   |
+====================+===============================================================+
| -r, --regionid     | Region ID.                                                    |
|                    |                                                               |
|                    | Type: Integer                                                 |
|                    |                                                               |
|                    | Default: None                                                 |
|                    |                                                               |
|                    | Required: Yes                                                 |
|                    |                                                               |
|                    | Example: 201                                                  |
+--------------------+---------------------------------------------------------------+
| -v, --verbose      | Print out verbose information while listing storage objects.  |
+--------------------+---------------------------------------------------------------+

Common Options
~~~~~~~~~~~~~~

Deprecated Options
^^^^^^^^^^^^^^^^^^

None

Output
~~~~~~

The return value from this command is a list of storage objects.

Examples
~~~~~~~~

Example 1
^^^^^^^^^

.. code-block:: bash

   dcm-list-storage-objects -r 201
   
Output
%%%%%%

.. code-block:: bash

   +-------------------+-----------+---------------------+---------------------+----------+-----------+------------+-------------+-----------+------------+-------------+
   | Storage Object ID |    Type   |         Name        |     Provider ID     | Read Any | Read Code | Read Group | Read Public | Write Any | Write Code | Write Group |
   +-------------------+-----------+---------------------+---------------------+----------+-----------+------------+-------------+-----------+------------+-------------+
   |       183539      | container | es-c300-svcimages-1 | es-c300-svcimages-1 |   True   |    True   |    True    |    False    |    True   |    True    |     True    |
   +-------------------+-----------+---------------------+---------------------+----------+-----------+------------+-------------+-----------+------------+-------------+
