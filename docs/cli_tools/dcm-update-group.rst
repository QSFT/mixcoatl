.. raw:: latex
  
      \newpage

.. _dcm_update_group:

dcm-update-group
----------------

Update DCM group.

Description
~~~~~~~~~~~

Update DCM group's name or description. 

Syntax
~~~~~~

.. code-block:: bash

   dcm-update-group -g <group_id> -n <name> -d <description>

Options
~~~~~~~

+---------------------+-------------------------------------------------------+
| Option              | Description                                           |
+=====================+=======================================================+
| -g, --groupid       | Group ID of the group to be updated.                  |
|                     |                                                       |
|                     | Type: Integer                                         |
|                     |                                                       |
|                     | Default: None                                         |
|                     |                                                       |
|                     | Required: Yes                                         |
|                     |                                                       |
+---------------------+-------------------------------------------------------+
| -n, --name          | Group's new name.                                     | 
|                     |                                                       |
|                     | Type: String                                          |
|                     |                                                       |
|                     | Default: None                                         |
|                     |                                                       |
|                     | Required: No                                          |
|                     |                                                       |
+---------------------+-------------------------------------------------------+
| -d, --description   | Group's new description.                              |
|                     |                                                       |
|                     | Type: String                                          |
|                     |                                                       |
|                     | Default: None                                         |
|                     |                                                       |
|                     | Required: No                                          |
|                     |                                                       |
+---------------------+-------------------------------------------------------+

Output
~~~~~~

None


Examples
~~~~~~~~

.. code-block:: bash

   dcm-update-group -g 105 -n 'Tester' -d 'Tester group'

Related Topics
~~~~~~~~~~~~~~

:ref:`List Groups  <dcm_list_groups>`

