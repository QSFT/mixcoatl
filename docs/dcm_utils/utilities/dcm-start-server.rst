.. raw:: latex

      \newpage

.. _dcm_start_server:

dcm-start-server
----------------

Start a server.

Description
~~~~~~~~~~~

Start a server that is in stopped/paused status.

Syntax
~~~~~~

.. code-block:: bash

   dcm-start-server <server_id>

Options
~~~~~~~

+--------------------+--------------------------------------------------------+
| Option             | Description                                            |
+====================+========================================================+
| No flag needed     | Server ID                                              | 
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

Job ID

Examples
~~~~~~~~

.. code-block:: bash

   dcm-start-server 47382

   54834

Related Topics
~~~~~~~~~~~~~~

:ref:`List Servers <dcm_list_servers>`
:ref:`Stop Server <dcm_stop_server>`

