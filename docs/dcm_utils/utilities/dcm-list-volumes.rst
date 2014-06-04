.. raw:: latex
  
      \newpage

.. _dcm_list_volumes:

dcm-list-volumes
-----------------

Lists volumes.

Description
~~~~~~~~~~~

Returns a list of volumes.

Syntax
~~~~~~

.. code-block:: bash

   usage: dcm-list-volumes [-h] (--regionid REGIONID | --regionpid REGIONPID | --all)
          [--userid USERID | --email EMAIL] [--groupid GROUPID | --groupname GROUPNAME]
          [--budgetid BUDGETID | --budgetname BUDGETNAME] [--nonattached]
          [--minsize MINSIZE] [--verbose]

   optional arguments:
     -h, --help            show this help message and exit
     --regionid REGIONID, -r REGIONID
                           Region ID.
     --regionpid REGIONPID, -R REGIONPID
                           Region Provider ID such as us-east-1.
     --all, -a             List volumes in all regions.
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
     --nonattached, -n     List non-attached volumes.
     --minsize MINSIZE     Minimum size of the volumes.
     --verbose, -v         Produce verbose output

Options
~~~~~~~

+--------------------+--------------------------------------------------------------+
| Option             | Description                                                  |
+====================+==============================================================+
| -r, --regionid     | Region ID.                                                   |
|                    |                                                              |
|                    | Type: Integer                                                |
|                    |                                                              |
|                    | Default: None                                                |
|                    |                                                              |
|                    | Required: Yes (if regionpid/all is not specified)            |
|                    |                                                              |
|                    | Example: 200                                                 |
+--------------------+--------------------------------------------------------------+
| -R, --regionpid    | Region provider ID.                                          |
|                    |                                                              |
|                    | Type: Str                                                    |
|                    |                                                              |
|                    | Default: None                                                |
|                    |                                                              |
|                    | Required: Yes (if regionid/all is not specified)             |
|                    |                                                              |
|                    | Example: us-west-1                                           |
+--------------------+--------------------------------------------------------------+
| -a, --all          | List volumes in all regions.                                 |
|                    |                                                              |
|                    | Required: Yes (if regionid/regionpid is not specified)       |
+--------------------+--------------------------------------------------------------+
| -u, --userid       | Owning user's VM login ID.                                   |
|                    |                                                              |
|                    | Type: Str                                                    |
|                    |                                                              |
|                    | Default: None                                                |
|                    |                                                              |
|                    | Required: No                                                 |
|                    |                                                              |
|                    | Example: p100                                                |
+--------------------+--------------------------------------------------------------+
| -m, --email        | E-Mail address of owning user.                               |
|                    |                                                              |
|                    | Type: Str                                                    |
|                    |                                                              |
|                    | Default: None                                                |
|                    |                                                              |
|                    | Required: No                                                 |
|                    |                                                              |
|                    | Example: gollum@example.com                                  |
+--------------------+--------------------------------------------------------------+
| -g, --groupid      | Owning group's group ID.                                     |
|                    |                                                              |
|                    | Type: Integer                                                |
|                    |                                                              |
|                    | Default: None                                                |
|                    |                                                              |
|                    | Required: No                                                 |
|                    |                                                              |
|                    | Example: 200                                                 |
+--------------------+--------------------------------------------------------------+
| -G, --groupname    | Owning group's group name.                                   |
|                    |                                                              |
|                    | Type: Str                                                    |
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
|                    | Example: 100                                                 |
+--------------------+--------------------------------------------------------------+
| -B, --budgetname   | Budget name.                                                 |
|                    |                                                              |
|                    | Type: Str                                                    |
|                    |                                                              |
|                    | Default: None                                                |
|                    |                                                              |
|                    | Required: No                                                 |
|                    |                                                              |
|                    | Example: Default                                             |
+--------------------+--------------------------------------------------------------+
| -n, --nonattached  | List non-attached volumes.                                   |
+--------------------+--------------------------------------------------------------+
| --minsize          | Minimum size of the volumes to be listed. Unit:GB            |
|                    |                                                              |
|                    | Type: Integer                                                |
|                    |                                                              |
|                    | Default: None                                                |
|                    |                                                              |
|                    | Required: No                                                 |
|                    |                                                              |
|                    | Example: 50                                                  |
+--------------------+--------------------------------------------------------------+
| -v, --verbose      | Produce verbose output.                                      |
+--------------------+--------------------------------------------------------------+

Common Options
~~~~~~~~~~~~~~

Deprecated Options
~~~~~~~~~~~~~~~~~~

None

Output
~~~~~~

The return value from this command is a list of volumes. 

Examples
~~~~~~~~

Example 1
^^^^^^^^^

.. code-block:: bash

   dcm-list-volumes --regionid 203

Output
%%%%%%

.. code-block:: bash

   +-----------+--------------+------------+--------------+----------------+------+-------------+--------+
   | Volume ID | Provider ID  |    Zone    | Volume Name  | Current Server | Size |    Owner    | Status |
   +-----------+--------------+------------+--------------+----------------+------+-------------+--------+
   |    204    | vol-ce05d1b4 | us-east-1a | vol-ce05d1b4 |      test      |  8   | User, Admin | ACTIVE |
   |    205    | vol-e10125dd | us-east-1a | vol-e10125dd |      test      |  8   | User, Admin | ACTIVE |
   +-----------+--------------+------------+--------------+----------------+------+-------------+--------+
