.. raw:: latex

      \newpage

.. _dcm_create_server:

dcm-create-server
----------------

Creates a server.

Description
~~~~~~~~~~~

Creates a server from a specified machine image.

Syntax
~~~~~~

.. code-block:: bash

   dcm-create-server -p <product_id> -m <machine_image_id> -d <datacenter_id>
                     -n <server_name> -b <budget_id> -k <keypair_name>
                     -v <vlan>

Options
~~~~~~~

+--------------------+--------------------------------------------------------+
| Option             | Description                                            |
+====================+========================================================+
| -p, --productid    | Provider's product ID                                  | 
|                    |                                                        |
|                    | Type: String                                           |
|                    |                                                        |
|                    | Default: None                                          |
|                    |                                                        |
|                    | Required: Yes                                          |
|                    |                                                        |
|                    | Example: 'm1.small'                                    |
+--------------------+--------------------------------------------------------+
| -m, --machineimage | Machine image ID                                       | 
|                    |                                                        |
|                    | Type: Integer                                          |
|                    |                                                        |
|                    | Default: None                                          |
|                    |                                                        |
|                    | Required: Yes                                          |
|                    |                                                        |
+--------------------+--------------------------------------------------------+
| -d, --datacenter   | Data center ID                                         | 
|                    |                                                        |
|                    | Type: Integer                                          |
|                    |                                                        |
|                    | Default: None                                          |
|                    |                                                        |
|                    | Required: Yes                                          |
|                    |                                                        |
+--------------------+--------------------------------------------------------+
| -D, --description  | Description of the server                              | 
|                    |                                                        |
|                    | Type: String                                           |
|                    |                                                        |
|                    | Default: None                                          |
|                    |                                                        |
|                    | Required: Yes                                          |
|                    |                                                        |
+--------------------+--------------------------------------------------------+
| -n, --name         | Name of the server                                     | 
|                    |                                                        |
|                    | Type: String                                           |
|                    |                                                        |
|                    | Default: None                                          |
|                    |                                                        |
|                    | Required: Yes                                          |
|                    |                                                        |
+--------------------+--------------------------------------------------------+
| -b, --budgetid     | Budget ID                                              | 
|                    |                                                        |
|                    | Type: Integer                                          |
|                    |                                                        |
|                    | Default: Default budget code                           |
|                    |                                                        |
|                    | Required: No                                           |
|                    |                                                        |
+--------------------+--------------------------------------------------------+
| -k, --keypair      | Keypair Name                                           | 
|                    |                                                        |
|                    | Type: String                                           |
|                    |                                                        |
|                    | Default: None                                          |
|                    |                                                        |
|                    | Required: No                                           |
|                    |                                                        |
+--------------------+--------------------------------------------------------+
| -v, --vlan         | VLAN ID                                                | 
|                    |                                                        |
|                    | Type: Integer                                          |
|                    |                                                        |
|                    | Default: None                                          |
|                    |                                                        |
|                    | Required: No                                           |
|                    |                                                        |
+--------------------+--------------------------------------------------------+

Output
~~~~~~

Job ID

Examples
~~~~~~~~

.. code-block:: bash

   dcm-create-server -m 34251 -d 7659 -n 'linux-demo-server' -D 'Linux demonstration server' -b 100

   54830

Related Topics
~~~~~~~~~~~~~~

:ref:`List Servers <dcm_list_servers>`

