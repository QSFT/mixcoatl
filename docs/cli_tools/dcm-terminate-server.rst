.. raw:: latex
  
      \newpage

.. _dcm_terminate_server:

dcm-terminate-server
--------------------

Terminates a server.

Description
~~~~~~~~~~~

Terminates a server.

Syntax
~~~~~~

.. program-output:: dcm-terminate-server -h

Options
~~~~~~~

+--------------------+--------------------------------------------------------------+
| Option             | Description                                                  |
+====================+==============================================================+
| -s, --serverid     | Server ID of the server to be deleted.                       |
|                    |                                                              |
|                    | Type: Integer                                                |
|                    |                                                              |
|                    | Default: None                                                |
|                    |                                                              |
|                    | Required: Yes                                                |
|                    |                                                              |
|                    | Example: 28371                                               |
+--------------------+--------------------------------------------------------------+
| -r, --reason       | The reason for terminating the server.                       |
|                    |                                                              |
|                    | Type: String                                                 |
|                    |                                                              |
|                    | Default: None                                                |
|                    |                                                              |
|                    | Required: No                                                 |
|                    |                                                              |
|                    | Example: Test completed.                                     |
+--------------------+--------------------------------------------------------------+

Common Options
~~~~~~~~~~~~~~

Deprecated Options
~~~~~~~~~~~~~~~~~~

None

Output
~~~~~~

Job ID.

Examples
~~~~~~~~

Example 1
^^^^^^^^^

.. code-block:: bash

   dcm-terminate-server -s 46372

Output
%%%%%%

.. code-block:: bash
   
   173829
