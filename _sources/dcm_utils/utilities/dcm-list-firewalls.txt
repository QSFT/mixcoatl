.. raw:: latex
  
      \newpage

.. _dcm_list_firewalls:

dcm-list-firewalls
------------------

List firewalls (security groups).

Description
~~~~~~~~~~~

Returns a list of firewalls, optionally restricted by region/account.

Syntax
~~~~~~

.. code-block:: bash

   usage: dcm-list-firewalls [-h]
                             [--accountid ACCOUNTID | --regionid REGIONID | --all]
   
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
| -a, --all          | All -- List all firewalls.                                 | 
+--------------------+------------------------------------------------------------+
| -i, --accountid    | Account ID                                                 | 
|                    |                                                            |
|                    | Type: Integer                                              |
|                    |                                                            |
|                    | Default: None                                              |
|                    |                                                            |
|                    | Required: No                                               |
|                    |                                                            |
|                    | Example: 302                                               |
+--------------------+------------------------------------------------------------+
| -r, --regionid     | Region ID                                                  | 
|                    |                                                            |
|                    | Type: Integer                                              |
|                    |                                                            |
|                    | Default: None                                              |
|                    |                                                            |
|                    | Required: No                                               |
|                    |                                                            |
|                    | Example: 502                                               |
+--------------------+------------------------------------------------------------+
| -v, --verbose      | Print out verbose information while listing regions        |
+--------------------+------------------------------------------------------------+

Common Options
~~~~~~~~~~~~~~

Deprecated Options
^^^^^^^^^^^^^^^^^^

None

Output
~~~~~~

The return value from this command is a list of firewalls/security groups.

Examples
~~~~~~~~

Example 1
^^^^^^^^^

This example is from an OpenStack cloud installation.

.. code-block:: bash

   dcm-list-firewalls --all

Output
%%%%%%

.. code-block:: bash

   +-------------+-----------+--------------------------------------+
   | Firewall ID | Name      | Provider ID                          |
   +-------------+-----------+--------------------------------------+
   | 300         | default   | 6f41b590-c728-450f-8237-ca6bee31f5f3 |
   | 301         | mydefault | be52a40a-e540-4432-bb95-531eb958dd54 |
   +-------------+-----------+--------------------------------------+

Related Topics
~~~~~~~~~~~~~~

:ref:`List Firewall Rules <dcm_list_firewall_rules>`
