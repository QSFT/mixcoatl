.. raw:: latex

      \newpage

.. _dcm_create_group:

dcm-create-group
----------------

Create a DCM group. 

Users can be assigned one or more groups. 

Each group can have 0 or 1 role applied to it.

Description
~~~~~~~~~~~

Creates a DCM group. Requires permission to create groups.

Syntax
~~~~~~

.. code-block:: bash

   dcm-create-group -n <group name> -d <group description>

Options
~~~~~~~

+--------------------+--------------------------------------------------------+
| Option             | Description                                            |
+====================+========================================================+
| -n, --name         | The name of the group                                  | 
|                    |                                                        |
|                    | Type: String                                           |
|                    |                                                        |
|                    | Default: None                                          |
|                    |                                                        |
|                    | Required: Yes                                          |
|                    |                                                        |
|                    | Example: 'Standard Group'                              |
+--------------------+--------------------------------------------------------+
| -d, --description  | The description of the group                           | 
|                    |                                                        |
|                    | Type: String                                           |
|                    |                                                        |
|                    | Default: None                                          |
|                    |                                                        |
|                    | Required: Yes                                          |
|                    |                                                        |
+--------------------+--------------------------------------------------------+
| -v, --verbose      | Print out verbose information about the group creation |
+--------------------+--------------------------------------------------------+

Common Options
~~~~~~~~~~~~~~

Deprecated Options
^^^^^^^^^^^^^^^^^^

None

Output
~~~~~~

The return value from this command the group ID of the created role.

Examples
~~~~~~~~

Create Group
^^^^^^^^^^^^

.. code-block:: bash

   dcm-create-group -n 'Standard Group' -d 'Standard Group'

   55324 

Related Topics
~~~~~~~~~~~~~~

:ref:`List Groups <dcm_list_groups>`

:ref:`Create Role <dcm_create_role>`

:ref:`List Roles <dcm_list_roles>`

:ref:`List Users <dcm_list_users>`

