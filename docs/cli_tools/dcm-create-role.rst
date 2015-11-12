.. raw:: latex
  
      \newpage

.. _dcm_create_role:

dcm-create-role
---------------

Create a DCM role. Roles are used to control access and action to DCM resources.

Description
~~~~~~~~~~~

Creates a DCM role. Requires permission to create roles.

Syntax
~~~~~~

.. program-output:: dcm-create-role -h

Options
~~~~~~~

+--------------------+-------------------------------------------------------+
| Option             | Description                                           |
+====================+=======================================================+
| -n, --name         | The name of the role                                  | 
|                    |                                                       |
|                    | Type: String                                          |
|                    |                                                       |
|                    | Default: None                                         |
|                    |                                                       |
|                    | Required: Yes                                         |
|                    |                                                       |
|                    | Example: 'Standard Role'                              |
+--------------------+-------------------------------------------------------+
| -d, --description  | The description of the role                           | 
|                    |                                                       |
|                    | Type: String                                          |
|                    |                                                       |
|                    | Default: None                                         |
|                    |                                                       |
|                    | Required: Yes                                         |
|                    |                                                       |
+--------------------+-------------------------------------------------------+
| -v, --verbose      | Print out verbose information about the role creation |
+--------------------+-------------------------------------------------------+

Common Options
~~~~~~~~~~~~~~

Deprecated Options
^^^^^^^^^^^^^^^^^^

None

Output
~~~~~~

The return value from this command will be the role ID of the created role.

Examples
~~~~~~~~

Example 1
^^^^^^^^^

.. code-block:: bash

   dcm-create-role -n 'Standard Role' -d 'Standard Role'

   55123

Related Topics
~~~~~~~~~~~~~~

:ref:`List Groups <dcm_list_groups>`

:ref:`Create Group <dcm_create_group>`

:ref:`List Roles <dcm_list_roles>`

:ref:`List Users <dcm_list_users>`
