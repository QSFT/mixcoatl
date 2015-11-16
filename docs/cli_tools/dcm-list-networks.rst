.. raw:: latex
  
      \newpage

.. _dcm_list_networks:

dcm-list-networks
-----------------

List networks.

Description
~~~~~~~~~~~

Returns a list of networks.

Syntax
~~~~~~

.. program-output:: dcm-list-networks -h

Options
~~~~~~~

+--------------------+--------------------------------------------------------------+
| Option             | Description                                                  |
+====================+==============================================================+
| -i, --accountid    | Account ID of networks to be listed.                         |
|                    |                                                              |
|                    | Type: Integer                                                |
|                    |                                                              |
|                    | Default: None                                                |
|                    |                                                              |
|                    | Required: No                                                 |
|                    |                                                              |
|                    | Example: 200                                                 |
+--------------------+--------------------------------------------------------------+
| -r, --regionid     | Region ID of networks to be listed.                          |
|                    |                                                              |
|                    | Type: Integer                                                |
|                    |                                                              |
|                    | Default: None                                                |
|                    |                                                              |
|                    | Required: No                                                 |
|                    |                                                              |
|                    | Example: 301                                                 |
+--------------------+--------------------------------------------------------------+
| -a, --all          | List all networks.                                           |
+--------------------+--------------------------------------------------------------+

Common Options
~~~~~~~~~~~~~~

Deprecated Options
~~~~~~~~~~~~~~~~~~

None

Output
~~~~~~

The return value from this command is a list of networks.

Examples
~~~~~~~~

Example 1
^^^^^^^^^

.. code-block:: bash

   dcm-list-networks --all

Output
%%%%%%

.. code-block:: bash

   +------------+-----------+-------------+--------------+----------+-----------------+
   | Network ID | Region ID |     Name    | Provider ID  |   Type   | Network Address |
   +------------+-----------+-------------+--------------+----------+-----------------+
   |    800     |    200    | Gollum VPC  | vpc-735ace52 | STANDARD | 192.168.10.0/24 |
   +------------+-----------+-------------+--------------+----------+-----------------+
   |    801     |    200    | Baggins VPC | vpc-93e3ace0 | STANDARD | 192.168.20.0/24 |
   +------------+-----------+-------------+--------------+----------+-----------------+
