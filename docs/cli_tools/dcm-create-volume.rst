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

.. code-block:: bash

   usage: dcm-create-volume [-h] (--budgetid BUDGETID | --budgetname BUDGETNAME)
                            [--datacenter DATACENTER] [--description DESCRIPTION]
                            [--name NAME] [--size SIZE]
   
   optional arguments:

     -h, --help            show this help message and exit
     --budgetid BUDGETID, -b BUDGETID
                           Budget ID.
     --budgetname BUDGETNAME, -B BUDGETNAME
                           Budget name.
     --datacenter DATACENTER, -d DATACENTER
                           Data Center ID in which to create the volume.
     --description DESCRIPTION, -D DESCRIPTION
                           The description of the volume.
     --name NAME, -n NAME  The name of the volume.
     --size SIZE, -s SIZE  The size of the volume in GB.

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
