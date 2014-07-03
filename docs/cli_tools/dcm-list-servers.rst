.. raw:: latex
  
      \newpage

.. _dcm_list_servers:

dcm-list-servers
----------------

List servers.

Description
~~~~~~~~~~~

Returns a list of servers.

Syntax
~~~~~~

.. code-block:: bash

   usage: dcm-list-servers [-h] [--all] [--userid USERID | --email EMAIL]
                           [--groupid GROUPID | --groupname GROUPNAME]
                           [--budgetid BUDGETID | --budgetname BUDGETNAME]
                           [--verbose]

   optional arguments:
     -h, --help            show this help message and exit
     --all, -a             List all servers.
     --userid USERID, -u USERID
                           Owning user's VM login ID. For example, p100.
     --email EMAIL, -m EMAIL
                           E-Mail address of owning user.
     --groupid GROUPID, -g GROUPID
                           Owning group's group ID.
     --groupname GROUPNAME, -G GROUPNAME
                           Owning group's group name.
     --budgetid BUDGETID, -b BUDGETID
                           Budget ID.
     --budgetname BUDGETNAME, -B BUDGETNAME
                           Budget Name.
     --verbose, -v         Produce verbose output

Options
~~~~~~~

+--------------------+--------------------------------------------------------------+
| Option             | Description                                                  |
+====================+==============================================================+
| -a, --all          | List all servers.                                            |
+--------------------+--------------------------------------------------------------+
| -u, --userid       | Owning user's VM login ID.                                   |
|                    |                                                              |
|                    | Type: String                                                 |
|                    |                                                              |
|                    | Default: None                                                |
|                    |                                                              |
|                    | Required: No                                                 |
|                    |                                                              |
|                    | Example: p100                                                |
+--------------------+--------------------------------------------------------------+
| -m, --email        | E-Mail address of owning user.                               |
|                    |                                                              |
|                    | Type: String                                                 |
|                    |                                                              |
|                    | Default: None                                                |
|                    |                                                              |
|                    | Required: No                                                 |
|                    |                                                              |
|                    | Example: tester@example.com                                  |
+--------------------+--------------------------------------------------------------+
| -g, --groupid      | Owning group's group ID.                                     |
|                    |                                                              |
|                    | Type: Integer                                                |
|                    |                                                              |
|                    | Default: None                                                |
|                    |                                                              |
|                    | Required: No                                                 |
|                    |                                                              |
|                    | Example: 301                                                 |
+--------------------+--------------------------------------------------------------+
| -G, --groupname    | Owning group's group name.                                   |
|                    |                                                              |
|                    | Type: String                                                 |
|                    |                                                              |
|                    | Default: None                                                |
|                    |                                                              |
|                    | Required: No                                                 |
|                    |                                                              |
|                    | Example: admin                                               |
+--------------------+--------------------------------------------------------------+
| -b, --budgetid     | Budget ID.                                                   |
|                    |                                                              |
|                    | Type: Integer                                                |
|                    |                                                              |
|                    | Default: None                                                |
|                    |                                                              |
|                    | Required: No                                                 |
|                    |                                                              |
|                    | Example: 105                                                 |
+--------------------+--------------------------------------------------------------+
| -B, --budgetname   | Budget Name.                                                 |
|                    |                                                              |
|                    | Type: String                                                 |
|                    |                                                              |
|                    | Default: None                                                |
|                    |                                                              |
|                    | Required: No                                                 |
|                    |                                                              |
|                    | Example: QA                                                  |
+--------------------+--------------------------------------------------------------+
| -v, --verbose      | Print out verbose information while listing servers.         |
+--------------------+--------------------------------------------------------------+

Common Options
~~~~~~~~~~~~~~

Deprecated Options
^^^^^^^^^^^^^^^^^^

None

Output
~~~~~~

The return value from this command is a list of servers.

Examples
~~~~~~~~

Example 1
^^^^^^^^^

.. code-block:: bash

   dcm-list-servers -a
   
Output
%%%%%%

.. code-block:: bash

   +-----------+-----------+-------------+----------------------------+-----------+---------+------------------------------+
   | Server ID |   Region  | Provider ID |        Server Name         | Public IP |  Status |          Start Date          |
   +-----------+-----------+-------------+----------------------------+-----------+---------+------------------------------+
   |    528    | eu-west-1 |  i-e91fde98 |        web server          |    None   | STOPPED | 2014-02-02T23:19:31.000+0000 |
   |    529    | eu-west-1 |  i-97481137 |        chef server         |    None   | STOPPED | 2014-02-25T07:21:30.000+0000 |
   |    601    | us-east-1 |  i-83a3fa23 |       puppet server        |    None   | STOPPED | 2014-01-31T07:55:55.000+0000 |
   +-----------+-----------+-------------+----------------------------+-----------+---------+------------------------------+
