.. raw:: latex

      \newpage

.. _dcm_delete_group:

dcm-delete-group
----------------

Delete a DCM group. 

Description
~~~~~~~~~~~

Deletes a DCM group.

Syntax
~~~~~~

.. program-output:: dcm-delete-group -h

Options
~~~~~~~

+--------------------+--------------------------------------------------------+
| Option             | Description                                            |
+====================+========================================================+
| No flag needed     | Group ID                                               | 
|                    |                                                        |
|                    | Type: Integer                                          |
|                    |                                                        |
|                    | Default: None                                          |
|                    |                                                        |
|                    | Required: Yes                                          |
|                    |                                                        |
+--------------------+--------------------------------------------------------+

Output
~~~~~~

message

Examples
~~~~~~~~

.. code-block:: bash

   dcm-delete-group 12345

   Group deleted.

Related Topics
~~~~~~~~~~~~~~

:ref:`List groups <dcm_list_groups>`

:ref:`Create a group <dcm_create_group>`

