.. raw:: latex

      \newpage

.. _dcm_create_network:

dcm-create-network
------------------

Creates a network.

Description
~~~~~~~~~~~

Creates a network.

Syntax
~~~~~~

.. code-block:: bash

   usage: dcm-create-network [-h] [--budgetid BUDGETID] [--name NAME]
                             [--netaddress NETADDRESS] [--regionid REGIONID]
                             [--description DESCRIPTION] [--dnsserver DNSSERVER]
                             [--groupid GROUPID]

   optional arguments:
     -h, --help            show this help message and exit
     --budgetid BUDGETID, -b BUDGETID
                           Budget ID
     --name NAME, -n NAME  Network Name
     --netaddress NETADDRESS, -a NETADDRESS
                           Network address such as 192.168.0.0/24
     --regionid REGIONID, -r REGIONID
                           Region ID
     --description DESCRIPTION, -D DESCRIPTION
                           Description
     --dnsserver DNSSERVER, -d DNSSERVER
                           DNS Server
     --groupid GROUPID, -g GROUPID
                           Owning Group ID

Options
~~~~~~~

+--------------------+--------------------------------------------------------+
| Option             | Description                                            |
+====================+========================================================+
| -b, --budgetid     | Budget ID                                              | 
|                    |                                                        |
|                    | Type: Integer                                          |
|                    |                                                        |
|                    | Default: None                                          |
|                    |                                                        |
|                    | Required: Yes                                          |
|                    |                                                        |
|                    | Example: 303                                           |
+--------------------+--------------------------------------------------------+
| -n, --name         | Network Name                                           | 
|                    |                                                        |
|                    | Type: String                                           |
|                    |                                                        |
|                    | Default: None                                          |
|                    |                                                        |
|                    | Required: Yes                                          |
|                    |                                                        |
+--------------------+--------------------------------------------------------+
| -a, --netaddress   | Network address                                        | 
|                    |                                                        |
|                    | Type: String                                           |
|                    |                                                        |
|                    | Default: None                                          |
|                    |                                                        |
|                    | Required: Yes                                          |
|                    |                                                        |
|                    | Example: 192.168.0.0/24                                |
+--------------------+--------------------------------------------------------+
| -r, --regionid     | Region ID                                              | 
|                    |                                                        |
|                    | Type: Integer                                          |
|                    |                                                        |
|                    | Default: None                                          |
|                    |                                                        |
|                    | Required: Yes                                          |
|                    |                                                        |
+--------------------+--------------------------------------------------------+
| -D, --description  | Description                                            | 
|                    |                                                        |
|                    | Type: String                                           |
|                    |                                                        |
|                    | Default: None                                          |
|                    |                                                        |
|                    | Required: Yes                                          |
|                    |                                                        |
+--------------------+--------------------------------------------------------+
| -d, --dnsserver    | DNS Server                                             | 
|                    |                                                        |
|                    | Type: String                                           |
|                    |                                                        |
|                    | Default: None                                          |
|                    |                                                        |
|                    | Required: No                                           |
|                    |                                                        |
+--------------------+--------------------------------------------------------+
| -g, --groupid      | Owning Group ID                                        | 
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

   dcm-create-network -b 300 -n 'test-network' -a '192.168.30.0/24' -r 305 -D 'DCM test network'

Output
%%%%%%

.. code-block:: bash

   54830

Related Topics
~~~~~~~~~~~~~~

:ref:`List Networks <dcm_list_networks>`

