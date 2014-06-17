.. raw:: latex
  
      \newpage

.. _dcm_list_groups:

dcm-list-groups
---------------

List groups.

Description
~~~~~~~~~~~

Returns a list of groups.

Syntax
~~~~~~

.. code-block:: bash

   usage: dcm-list-groups [-h] [--userid USERID] [--email EMAIL] [--all] [--verbose]

   optional arguments:
     -h, --help            show this help message and exit
     --userid USERID, -u USERID
                           User ID. For example, p100
     --email EMAIL, -m EMAIL
                           E-Mail address of user
     --all, -a             List all groups
     --verbose, -v         Produce verbose output

Options
~~~~~~~

+--------------------+--------------------------------------------------------------+
| Option             | Description                                                  |
+====================+==============================================================+
| -u, --userid       | User ID. Returns a list of groups the user belongs to.       |
|                    |                                                              |
|                    | Type: Integer                                                |
|                    |                                                              |
|                    | Default: None                                                |
|                    |                                                              |
|                    | Required: No                                                 |
|                    |                                                              |
|                    | Example: 58395                                               |
+--------------------+--------------------------------------------------------------+
| -m, --email        | E-Mail address of user.                                      |
|                    |                                                              |
|                    | Type: String                                                 |
|                    |                                                              |
|                    | Default: None                                                |
|                    |                                                              |
|                    | Required: No                                                 |
|                    |                                                              |
|                    | Example: admin@example.com                                   |
+--------------------+--------------------------------------------------------------+
| -a, --all          | List all groups.                                             |
+--------------------+--------------------------------------------------------------+
| -v, --verbose      | Print out verbose information while listing groups.          |
+--------------------+--------------------------------------------------------------+

Common Options
~~~~~~~~~~~~~~

Deprecated Options
~~~~~~~~~~~~~~~~~~

None

Output
~~~~~~

The return value from this command is a list of DCM groups.

Examples
~~~~~~~~

Example 1
^^^^^^^^^

.. code-block:: bash

   dcm-list-groups --all

Output
%%%%%%

.. code-block:: bash

   +----------+--------------------+-----------------------------------------------------+--------+
   | Group ID |     Group Name     | Description                                         | Status |
   +----------+--------------------+-----------------------------------------------------+--------+
   |   200    |       Admin        | Default administrative group with full permissions. | ACTIVE |
   |   203    |   advanced group   | advanced group                                      | ACTIVE |
   |   201    |    basic group     | basic group                                         | ACTIVE |
   |   202    | intermediate group | intermediate group                                  | ACTIVE |
   +----------+--------------------+-----------------------------------------------------+--------+
