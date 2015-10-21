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

    usage: dcm-list-servers [-h] [--region REGION] [--extended EXTENDED]
                            [--verbose] [--userid USERID | --email EMAIL]
                            [--groupid GROUPID | --groupname GROUPNAME]
                            [--budgetid BUDGETID | --budgetname BUDGETNAME]
                            [--json | --xml | --csv]

    optional arguments:
      -h, --help            show this help message and exit
      --region REGION, -r REGION
                            Region ID
      --extended EXTENDED, -e EXTENDED
                            Extended Status
      --verbose, -v         print more more Server properties in the table
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
      --json                print API response in JSON format.
      --xml                 print API response in XML format.
      --csv                 print API response in CSV format.

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
| -v, --verbose      | Print out more information about servers when listing such   |
|                    | as Machine Image Name, Architecture, Owning User, Owning     |
|                    | Group etc                                                    |
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

    +-----------+--------+-------------+----------------------+---------------+----------+--------+-----------+---------+------------------------------+
    | Server ID | Region | Provider ID | Server Name          | Public IP     | Platform | Budget | Product   | Status  | Start Date                   |
    +-----------+--------+-------------+----------------------+---------------+----------+--------+-----------+---------+------------------------------+
    | 115626    | 1031   | i-2fb42dfd  | jds-2012-test        | None          | WINDOWS  | 200    | m3.medium | STOPPED | 2015-08-14T14:41:57.000+0000 |
    | 115642    | 1031   | i-bdd74716  | jds-sensu1           | None          | UBUNTU   | 200    | m1.medium | STOPPED | 2015-08-19T12:40:13.000+0000 |
    | 226380    | 1031   | i-58c804fa  | jdsiara54            | 22.22.22.21   | UBUNTU   | 200    | m1.medium | RUNNING | 2015-10-07T17:07:27.000+0000 |
    | 155837    | 1031   | i-4a8028e9  | jdsubu090915-1       | 22.22.22.22   | UBUNTU   | 807    | m1.medium | RUNNING | 2015-09-09T12:21:02.000+0000 |
    | 155805    | 1034   | i-a21c8362  | appliance-win        | 22.22.22.23   | WINDOWS  | 200    | m3.medium | RUNNING | 2015-09-02T20:03:50.000+0000 |
    | 85236     | 1034   | i-b8e7a77b  | puppetmaster (keep!) | 22.22.22.24   | CENT_OS  | 200    | m3.medium | RUNNING | 2015-08-14T16:07:55.000+0000 |
    | 155833    | 1033   | i-bcd59679  | training             | 22.22.22.25   | UBUNTU   | 200    | m1.medium | RUNNING | 2015-09-04T16:51:06.000+0000 |
    +-----------+--------+-------------+----------------------+---------------+----------+--------+-----------+---------+------------------------------+


Example 2
^^^^^^^^^

.. code-block:: bash

   dcm-list-servers -v

Output
%%%%%%

.. code-block:: bash

    +-----------+--------+-------------+----------------------+---------------+----------+--------+-----------+---------+------------------------------+--------------+------+-------------+-------+--------+-----------------------------------------------------------------+
    | Server ID | Region | Provider ID | Server Name          | Public IP     | Platform | Budget | Product   | Status  | Start Date                   | User         | Arch | Data Center | Agent | Groups | Machine Image                                                   |
    +-----------+--------+-------------+----------------------+---------------+----------+--------+-----------+---------+------------------------------+--------------+------+-------------+-------+--------+-----------------------------------------------------------------+
    | 115626    | 1031   | i-2fb42dfd  | jds-2012-test        | None          | WINDOWS  | 200    | m3.medium | STOPPED | 2015-08-14T14:41:57.000+0000 | jane@doe.com | I64  | 1266        | None  | None   | Windows_Server-2012-R2_RTM-English-64Bit-Base-2015.07.15        |
    | 115642    | 1031   | i-bdd74716  | jds-sensu1           | None          | UBUNTU   | 200    | m1.medium | STOPPED | 2015-08-19T12:40:13.000+0000 | john@doe.com | I64  | 1265        | None  | 201    | ubuntu/images/ebs/ubuntu-trusty-14.04-amd64-server-20140416.1   |
    | 226380    | 1031   | i-58c804fa  | jdsiara54            | 22.22.22.21   | UBUNTU   | 200    | m1.medium | RUNNING | 2015-10-07T17:07:27.000+0000 | john@doe.com | I64  | 1265        | None  | 201    | ubuntu/images/ebs/ubuntu-precise-12.04-amd64-server-20150204    |
    | 155837    | 1031   | i-4a8028e9  | jdsubu090915-1       | 22.22.22.22   | UBUNTU   | 807    | m1.medium | RUNNING | 2015-09-09T12:21:02.000+0000 | john@doe.com | I64  | 1265        | None  | 201    | ubuntu/images/ebs/ubuntu-precise-12.04-amd64-server-20150204    |
    | 155805    | 1034   | i-a21c8362  | appliance-win        | 22.22.22.23   | WINDOWS  | 200    | m3.medium | RUNNING | 2015-09-02T20:03:50.000+0000 | john@doe.com | I64  | 1274        | None  | None   | Amazon/Windows_Server-2008-R2_SP1-English-64Bit-Base-2015.01.01 |
    | 85236     | 1034   | i-b8e7a77bc | puppetmaster (keep!) | 22.22.22.24   | CENT_OS  | 200    | m3.medium | RUNNING | 2015-08-14T16:07:55.000+0000 | jane@doe.com | I64  | 1273        | None  | None   | CentOS 6.4 x86_64 - with updates - G2 support                   |
    | 155833    | 1033   | i-bcd59679  | training             | 22.22.22.25   | UBUNTU   | 200    | m1.medium | RUNNING | 2015-09-04T16:51:06.000+0000 | jane@doe.com | I64  | 1271        | 104   | None   | ubuntu/images/ebs/ubuntu-trusty-14.04-amd64-server-20140416.1   |
    +-----------+--------+-------------+----------------------+---------------+----------+--------+-----------+---------+------------------------------+--------------+------+-------------+-------+--------+-----------------------------------------------------------------+
