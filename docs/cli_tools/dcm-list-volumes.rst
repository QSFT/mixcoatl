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

.. program-output:: dcm-list-volumes -h

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
