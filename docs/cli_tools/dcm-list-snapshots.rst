.. raw:: latex
  
      \newpage

.. _dcm_list_snapshots:

dcm-list-snapshots
------------------

Lists snapshots.

Description
~~~~~~~~~~~

Returns a list of snapshots.

Syntax
~~~~~~

.. program-output:: dcm-list-snapshots -h

Options
~~~~~~~

+--------------------+------------------------------------------------------------+
| Option             | Description                                                |
+====================+============================================================+
| -r, --regionid     | Region ID.                                                 |
|                    |                                                            |
|                    | Type: Integer                                              |
|                    |                                                            |
|                    | Default: None                                              |
|                    |                                                            |
|                    | Required: Yes (if regionpid/all was not specified)         |
|                    |                                                            |
|                    | Example: 201                                               |
+--------------------+------------------------------------------------------------+
| -R, --regionpid    | Region provider ID.                                        |
|                    |                                                            |
|                    | Type: Str                                                  |
|                    |                                                            |
|                    | Default: None                                              |
|                    |                                                            |
|                    | Required: Yes (if regionid/all was not specified)          |
|                    |                                                            |
|                    | Example: us-west-1                                         |
+--------------------+------------------------------------------------------------+
| -a, --all          | List all firewalls.                                        |
+--------------------+------------------------------------------------------------+
| -g, --groupid      | Owning group's group ID.                                   |
|                    |                                                            |
|                    | Type: Integer                                              |
|                    |                                                            |
|                    | Default: None                                              |
|                    |                                                            |
|                    | Required: No                                               |
|                    |                                                            |
|                    | Example: 102                                               |
+--------------------+------------------------------------------------------------+
| -G, --groupname    | Owning group's group name.                                 |
|                    |                                                            |
|                    | Type: Str                                                  |
|                    |                                                            |
|                    | Default: None                                              |
|                    |                                                            |
|                    | Required: No                                               |
|                    |                                                            |
|                    | Example: admin                                             |
+--------------------+------------------------------------------------------------+
| -b, --budgetid     | Budget ID.                                                 |
|                    |                                                            |
|                    | Type: Integer                                              |
|                    |                                                            |
|                    | Default: None                                              |
|                    |                                                            |
|                    | Required: No                                               |
|                    |                                                            |
|                    | Example: 301                                               |
+--------------------+------------------------------------------------------------+
| -B, --budgetname   | Budget Name.                                               |
|                    |                                                            |
|                    | Type: Str                                                  |
|                    |                                                            |
|                    | Default: None                                              |
|                    |                                                            |
|                    | Required: No                                               |
|                    |                                                            |
|                    | Example: DEF                                               |
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

The return value from this command is a list of snapshots.

Examples
~~~~~~~~

Example 1
^^^^^^^^^

.. code-block:: bash

   dcm-list-snapshots -r 201

Output
%%%%%%

.. code-block:: bash

   +-------------+---------------+---------------+-------+---------+------------------------------+
   | Snapshot ID |  Provider ID  | Snapshot Name | Group |  Budget |             Date             |
   +-------------+---------------+---------------+-------+---------+------------------------------+
   |      1      | snap-4dbe6fea | snap-4dbe6fea |  None | Default | 2014-03-22T21:01:59.000+0000 |
   +-------------+---------------+---------------+-------+---------+------------------------------+
