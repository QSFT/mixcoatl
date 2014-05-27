.. raw:: latex

      \newpage

.. _dcm_stop_server:

dcm-stop-server
---------------

Stops a server.

Description
~~~~~~~~~~~

Stops a server. The server will not be terminated but will be paused.

Syntax
~~~~~~

.. code-block:: bash

   dcm-stop-server <server_id>

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

   dcm-stop-server 47382

   54833

Related Topics
~~~~~~~~~~~~~~

:ref:`List Servers <dcm_list_servers>`
:ref:`Start Server <dcm_start_server>`

