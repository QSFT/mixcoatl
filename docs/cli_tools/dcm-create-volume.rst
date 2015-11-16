.. raw:: latex
  
      \newpage

.. _dcm_create_volume:

dcm-create-volume
-----------------

Create a volume. 

Volumes represent block storage. Conceptually, storage devices can be used to
store data in a persistent manner in the cloud.

Creating a volume also creates a `job`. 

Description
~~~~~~~~~~~

Creates a volume. Requires permission to create volumes.

Syntax
~~~~~~

.. program-output:: dcm-create-volume -h

Options
~~~~~~~

+--------------------+---------------------------------------------------------+
| Option             | Description                                             |
+====================+=========================================================+
| -b, --budgetid     | The budget code to which the volume is assigned         | 
|                    |                                                         |
|                    | Type: Integer                                           |
|                    |                                                         |
|                    | Default: None                                           |
|                    |                                                         |
|                    | Required: Yes, if no budget name (-B)                   |
|                    |                                                         |
|                    | Example: 200                                            |
+--------------------+---------------------------------------------------------+
| -B, --budgetname   | The budget name of the volume                           | 
|                    |                                                         |
|                    | Type: String                                            |
|                    |                                                         |
|                    | Default: None                                           |
|                    |                                                         |
|                    | Required: Yes, if no budget id (-d)                     |
|                    |                                                         |
|                    | Example: 'Default'                                      |
+--------------------+---------------------------------------------------------+
| -d, --datacenter   | The data center ID in which the volume is created       | 
|                    |                                                         |
|                    | Type: Integer                                           |
|                    |                                                         |
|                    | Default: None                                           |
|                    |                                                         |
|                    | Required: Yes                                           |
|                    |                                                         |
|                    | Example: 302                                            |
+--------------------+---------------------------------------------------------+
| -n, --name         | The name of the volume                                  | 
|                    |                                                         |
|                    | Type: String                                            |
|                    |                                                         |
|                    | Default: None                                           |
|                    |                                                         |
|                    | Required: Yes                                           |
|                    |                                                         |
|                    | Example: 'data volume'                                  |
+--------------------+---------------------------------------------------------+
| -D, --description  | The size, given in GB, of the volume                    | 
|                    |                                                         |
|                    | Type: Integer                                           |
|                    |                                                         |
|                    | Default: None                                           |
|                    |                                                         |
|                    | Required: Yes                                           |
|                    |                                                         |
|                    | Example: 'data volume test'                             |
+--------------------+---------------------------------------------------------+
| -s, --size         | The size, given in GB, of the volume                    | 
|                    |                                                         |
|                    | Type: Integer                                           |
|                    |                                                         |
|                    | Default: None                                           |
|                    |                                                         |
|                    | Required: Yes                                           |
|                    |                                                         |
|                    | Example: 1                                              |
+--------------------+---------------------------------------------------------+
| -v, --verbose      | Print out verbose information about the volume creation |
+--------------------+---------------------------------------------------------+

Common Options
~~~~~~~~~~~~~~

Deprecated Options
^^^^^^^^^^^^^^^^^^

None

Output
~~~~~~

The return value from this command will be the job ID.

Examples
~~~~~~~~

Example 1
^^^^^^^^^

.. code-block:: bash

   dcm-create-volume -b 200 --datacenter 204 -D 'data volume' -n 'test3' -s 1

   201

Related Topics
~~~~~~~~~~~~~~

:ref:`List Volumes <dcm_list_volumes>`

:ref:`List Regions <dcm_list_regions>`

:ref:`List Data Centers <dcm_list_datacenters>`

:ref:`List Jobs <dcm_list_jobs>`
