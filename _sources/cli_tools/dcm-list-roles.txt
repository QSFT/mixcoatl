.. raw:: latex
  
      \newpage

.. _dcm_list_roles:

dcm-list-roles
--------------

List roles.

Description
~~~~~~~~~~~

Returns a list of roles.

Syntax
~~~~~~

.. code-block:: bash

   usage: dcm-list-roles [-h] [--verbose]
   
   optional arguments:
     -h, --help     show this help message and exit
     --verbose, -v  Produce verbose output

Options
~~~~~~~

+--------------------+------------------------------------------------------------+
| Option             | Description                                                |
+====================+============================================================+
| -v, --verbose      | Print out verbose information while listing roles          |
+--------------------+------------------------------------------------------------+

Common Options
~~~~~~~~~~~~~~

Deprecated Options
^^^^^^^^^^^^^^^^^^

None

Output
~~~~~~

The return value from this command is a list of DCM roles

Examples
~~~~~~~~

Example 1
^^^^^^^^^

.. code-block:: bash

   dcm-list-roles

Output
%%%%%%

.. code-block:: bash

   +---------+-------------+--------------------+--------+
   | Role ID | Role Name   | Description        | Status |
   +---------+-------------+--------------------+--------+
   | 55400   | Admin       | General Admin Role | ACTIVE |
   | 55502   | Production  | Production         | ACTIVE |
   | 55501   | Testing     | Testing            | ACTIVE |
   | 55500   | Development | Development        | ACTIVE |
   +---------+-------------+--------------------+--------+
