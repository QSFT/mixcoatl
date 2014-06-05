.. raw:: latex
  
      \newpage

.. _dcm_list_deployments:

dcm-list-deployments
--------------------

Lists deployments.

Description
~~~~~~~~~~~

Returns a list of deployments.

Syntax
~~~~~~

.. code-block:: bash

   usage: dcm-list-deployments [-h] [--all] [--verbose]

   optional arguments:
     -h, --help     show this help message and exit
     --all, -a      List all deployments.
     --verbose, -v  Produce verbose output

Options
~~~~~~~

+--------------------+------------------------------------------------------------+
| Option             | Description                                                |
+====================+============================================================+
| -a, --all          | List all deployments.                                      |
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

The return value from this command is a list of deployments.

Examples
~~~~~~~~

Example 1
^^^^^^^^^

.. code-block:: bash

   dcm-list-deployments --all

Output
%%%%%%

.. code-block:: bash

   +---------------+------+-------------+------------------------------+---------+
   | Deployment ID | Name |    Owner    |      Creation Timestamp      |  Status |
   +---------------+------+-------------+------------------------------+---------+
   |       1       | Demo | User, Admin | 2014-02-23T10:35:10.876+0000 | STOPPED |
   +---------------+------+-------------+------------------------------+---------+
