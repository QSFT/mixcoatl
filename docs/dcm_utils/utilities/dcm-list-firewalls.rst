.. raw:: latex
  
      \newpage

.. _dcm_list_firewalls:

dcm-list-firewalls
------------------

Lists firwalls.

Description
~~~~~~~~~~~

Returns a list of firewalls.

Syntax
~~~~~~

.. code-block:: bash

   usage: dcm-list-firewalls [-h] [--accountid ACCOUNTID | --regionid REGIONID | --all]
   
   optional arguments:
     -h, --help            show this help message and exit
     --accountid ACCOUNTID, -i ACCOUNTID
                           Account ID
     --regionid REGIONID, -r REGIONID
                           Region ID
     --all, -a

Options
~~~~~~~

+--------------------+------------------------------------------------------------+
| Option             | Description                                                |
+====================+============================================================+
| -i, --accountid    | Account ID.                                                |
|                    |                                                            |
|                    | Type: Integer                                              |
|                    |                                                            |
|                    | Default: None                                              |
|                    |                                                            |
|                    | Required: No                                               |
|                    |                                                            |
|                    | Example: 300                                               |
+--------------------+------------------------------------------------------------+
| -r, --regionid     | Region ID.                                                 |
|                    |                                                            |
|                    | Type: Integer                                              |
|                    |                                                            |
|                    | Default: None                                              |
|                    |                                                            |
|                    | Required: No                                               |
|                    |                                                            |
|                    | Example: 203                                               |
+--------------------+------------------------------------------------------------+
| -a, --all          | List all firewalls.                                        |
+--------------------+------------------------------------------------------------+
| -v, --verbose      | Produce verbose output                                     |
+--------------------+------------------------------------------------------------+

Common Options
~~~~~~~~~~~~~~

Deprecated Options
~~~~~~~~~~~~~~~~~~

None

Output
~~~~~~

The return value from this command is a list of firewalls.

Examples
~~~~~~~~

Example 1
^^^^^^^^^

.. code-block:: bash

   dcm-list-firewalls --all

Output
%%%%%%

.. code-block:: bash

   +-------------+---------------------------------------------------------------------+-------------+
   | Firewall ID |                                 Name                                | Provider ID |
   +-------------+---------------------------------------------------------------------+-------------+
   |     201     |                      default (VPC vpc-e805f58d)                     | sg-81b768f4 |
   |     202     |                  DemoFirewall (VPC vpc-105e4372)                    | sg-cf9176aa |
   |     203     |                      default (VPC vpc-105e4372)                     | sg-901439f2 |
   +-------------+---------------------------------------------------------------------+-------------+
