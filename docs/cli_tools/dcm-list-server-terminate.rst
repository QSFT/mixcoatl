.. raw:: latex
  
      \newpage

.. _dcm_list_server_terminate:

dcm-list-server-terminate
-------------------------

Lists all servers with their accompanying terminateAfter timestamp.  

The terminateAfter timestamp is a date in the future in which the server will
automatically be terminated.

Description
~~~~~~~~~~~

Lists all servers with their accompanying terminateAfter timestamp. 

Syntax
~~~~~~

.. program-output:: dcm-list-server-terminate -h

Options
~~~~~~~

+--------------------+-------------------------------------------------------+
| Option             | Description                                           |
+====================+=======================================================+
| -a, --all          | List all servers with terminateAfter timestamp.       |
+--------------------+-------------------------------------------------------+
| -s, --serverid     | Server ID                                             | 
|                    |                                                       |
|                    | Type: Integer                                         |
|                    |                                                       |
|                    | Default: None                                         |
|                    |                                                       |
|                    | Required: Yes                                         |
|                    |                                                       |
|                    | Example: 1515                                         |
+--------------------+-------------------------------------------------------+

Common Options
~~~~~~~~~~~~~~

Deprecated Options
^^^^^^^^^^^^^^^^^^

None

Output
~~~~~~

The return value from this command is a list of servers with their terminateAfter timestamp.

Examples
~~~~~~~~

Example 1
^^^^^^^^^

.. code-block:: bash

   dcm-list-server-terminate --all

    +------+--------+----------------+-------------+--------------------------+-------------------------------+---------+-------------+
    |  ID  | Cloud  |     Region     | Provider ID |       Server Name        |             Owner             |  Status | Termination |
    +------+--------+----------------+-------------+--------------------------+-------------------------------+---------+-------------+
    | 4099 | Amazon | ap-southeast-2 |  i-367e490a |    skang-single-node     |           Not Found           | STOPPED |  48.7 hours |
    | 6481 | Amazon |   us-east-1    |  i-4ccea560 | DataB-independent-node-0 |         bob@example.com       | RUNNING |    Never    |
    | 4201 | Amazon |   us-east-1    |  i-df6524a7 |         Demo-GSA         |           Not Found           | STOPPED |    Never    |
    | 4202 | Amazon |   us-east-1    |  i-4839b336 |          jdsAD2          |           Not Found           | RUNNING |    Never    |
    | 6111 | Amazon |   us-east-1    |  i-fde947af |          jdsAD3          |         jim@example.com       | STOPPED |    Never    |
    | 4204 | Amazon |   us-east-1    |  i-1b677d4b |          jdsi41          |           Not Found           | RUNNING |    Never    |
    | 4203 | Amazon |   us-east-1    |  i-18c88476 |       jdsrhel62-2        |           Not Found           | STOPPED |    Never    |
    | 4200 | Amazon |   us-east-1    |  i-2fec0b42 |        pe-30-web3        |           Not Found           | RUNNING |    Never    |
    | 6415 | Amazon |   us-east-1    |  i-bfe57893 |       PuppetEnt323       |        joe@example.com        | RUNNING |    Never    |
    | 4537 | Amazon |   us-east-1    |  i-f0eff9a3 |           test           |        tom@example.com        | RUNNING |  3.7 hours  |
    | 6505 | Amazon |   us-east-1    |  i-a171e68d |       UbuntuAgent        |        ed@example.com         | STOPPED |    Never    |
    | 4209 | Amazon |   us-west-1    |  i-3e018f64 |     Master Training      |           Not Found           | STOPPED |    Never    |
    | 4212 | Amazon |   us-west-2    |  i-013b7f35 |    cse-redhat-mirror     |           Not Found           | RUNNING |    Never    |
    | 4211 | Amazon |   us-west-2    |  i-2d708119 |       infa-cse-git       |           Not Found           | RUNNING |    Never    |
    | 4210 | Amazon |   us-west-2    |  i-263d3f14 |        pairing01         |           Not Found           | RUNNING |    Never    |
    | 4214 | Amazon |   us-west-2    |  i-e76610d1 |   test-aws-user-data-2   |           Not Found           | RUNNING |    Never    |
    | 4213 | Amazon |   us-west-2    |  i-679a4951 |       test-jv-fw-1       |           Not Found           | RUNNING |    Never    |
    +------+--------+----------------+-------------+--------------------------+-------------------------------+---------+-------------+

Related Topics
~~~~~~~~~~~~~~

:ref:`Set Server Terminate <dcm_set_server_terminate>`
