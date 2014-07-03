.. raw:: latex
  
      \newpage

.. _dcm_list_cm_accounts:

dcm-list-cm-accounts
--------------------

List configuration management accounts.

Description
~~~~~~~~~~~

Returns a list of configuration management accounts.

Syntax
~~~~~~

.. code-block:: bash

   usage: dcm-list-cm-accounts [-h] [--verbose]

   optional arguments:
     -h, --help     show this help message and exit
     --verbose, -v  Produce verbose output

Options
~~~~~~~

+--------------------+--------------------------------------------------------------+
| Option             | Description                                                  |
+====================+==============================================================+
| -v, --verbose      | Print out verbose information while listing CM accounts.     |
+--------------------+--------------------------------------------------------------+

Common Options
~~~~~~~~~~~~~~

Deprecated Options
^^^^^^^^^^^^^^^^^^

None

Output
~~~~~~

The return value from this command is a list of configuration management accounts.

Examples
~~~~~~~~

Example 1
^^^^^^^^^

.. code-block:: bash

   dcm-list-cm-accounts
   
Output
%%%%%%

.. code-block:: bash

   +------------+------------+-------------+----------+
   | Account ID |    Name    |    System   |  Status  |
   +------------+------------+-------------+----------+
   |    201     |   Chef11   |     Chef    |  ACTIVE  |
   |    202     |   Puppet   |    Puppet   |  ACTIVE  |
   |    203     | Sean Test  | ObjectStore | INACTIVE |
   +------------+------------+-------------+----------+
