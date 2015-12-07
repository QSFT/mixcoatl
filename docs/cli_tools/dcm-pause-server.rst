.. raw:: latex

      \newpage

.. _dcm_pause_server:

dcm-pause-server
----------------

Pauses a server.

Description
~~~~~~~~~~~

Pauses a server. The server will be paused. In some cloud environments, pausing may be different from stopping.

Syntax
~~~~~~

.. program-output:: dcm-pause-server -h

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

   dcm-pause-server --server_id 49680

   55832

Related Topics
~~~~~~~~~~~~~~

:ref:`List Servers <dcm_list_servers>`

:ref:`Start Server <dcm_start_server>`

:ref:`Stop Server <dcm_stop_server>`
