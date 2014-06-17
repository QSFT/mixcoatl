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

.. code-block:: bash

   usage: dcm-terminate-server [-h] [--serverid SERVERID] [--reason REASON]

   optional arguments:
     -h, --help            show this help message and exit
     --serverid SERVERID, -s SERVERID
                           Server ID
     --reason REASON, -r REASON
                           The reason for terminating the server.

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
