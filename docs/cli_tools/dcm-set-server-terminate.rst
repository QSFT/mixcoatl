.. raw:: latex
  
      \newpage

.. _dcm_set_server_terminate:

dcm-set-server-terminate
------------------------

Set or Extend a servers terminateAfter timestamp. 

The terminateAfter timestamp is a date in the future in which the server will
automatically be terminated.

Description
~~~~~~~~~~~

Set or Extend a servers terminateAfter timestamp.

Syntax
~~~~~~

.. program-output:: dcm-set-server-terminate -h

Options
~~~~~~~

+--------------------+-------------------------------------------------------+
| Option             | Description                                           |
+====================+=======================================================+
| -s, --serverid     | Server ID                                             | 
|                    |                                                       |
|                    | Type: Integer                                         |
|                    |                                                       |
|                    | Default: None                                         |
|                    |                                                       |
|                    | Required: Yes                                         |
|                    |                                                       |
|                    | Example: 1515                                         |
|                    |                                                       |
+--------------------+-------------------------------------------------------+
| -x, --extend       | Sets terminateAfter to NOW + Hour Specified           | 
|                    |                                                       |
|                    | Type: Integer                                         |
|                    |                                                       |
|                    | Default: None                                         |
|                    |                                                       |
|                    | Required: No                                          |
|                    |                                                       |
|                    | Example: 3                                            |
|                    |                                                       |
+--------------------+-------------------------------------------------------+
| -d, --date_format  | Date/Time                                             | 
|                    |                                                       |
|                    | Type: DATETIME                                        |
|                    |                                                       |
|                    | Default: None                                         |
|                    |                                                       |
|                    | Required: No                                          |
|                    |                                                       |
|                    | Example: "2014-07-04 08:03:11"                        |
|                    |                                                       |
+--------------------+-------------------------------------------------------+

Common Options
~~~~~~~~~~~~~~

Deprecated Options
^^^^^^^^^^^^^^^^^^

None

Output
~~~~~~

None

Examples
~~~~~~~~

Example 1
^^^^^^^^^

.. code-block:: bash

    dcm-set-server-terminate -s 4537 -x 5

    dcm-list-server-terminate -s 4537

    +------+--------+-----------+-------------+-------------+-------------------------------+---------+-------------+
    |  ID  | Cloud  |   Region  | Provider ID | Server Name |             Owner             |  Status | Termination |
    +------+--------+-----------+-------------+-------------+-------------------------------+---------+-------------+
    | 4537 | Amazon | us-east-1 |  i-f0eff9a3 |     test    | brian.williams@enstratius.com | RUNNING |  5.0 hours  |
    +------+--------+-----------+-------------+-------------+-------------------------------+---------+-------------+

Related Topics
~~~~~~~~~~~~~~

:ref:`List Server Terminate <dcm_list_server_terminate>`
