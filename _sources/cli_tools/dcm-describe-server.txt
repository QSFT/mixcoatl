.. raw:: latex
  
      \newpage

.. _dcm_describe_server:

dcm-describe-server
-------------------

Describe a server.

Description
~~~~~~~~~~~

Returns a short summary about a server.

Syntax
~~~~~~

.. code-block:: bash

   usage: dcm-describe-server [-h] [--verbose] serverid
   
   positional arguments:
     serverid       Server ID
   
   optional arguments:
     -h, --help     show this help message and exit
     --verbose, -v  Produce verbose output

Options
~~~~~~~

+--------------------+------------------------------------------------------------+
| Option             | Description                                                |
+====================+============================================================+
| -v, --verbose      | Print out verbose information while describing a server    |
+--------------------+------------------------------------------------------------+

Common Options
~~~~~~~~~~~~~~

Deprecated Options
^^^^^^^^^^^^^^^^^^

None

Output
~~~~~~

The output of this command is a short summary of information about a server given a server ID.

Examples
~~~~~~~~

Example 1
^^^^^^^^^

.. code-block:: bash

   dcm-describe-server 906

Output
%%%%%%

.. code-block:: bash

   +--------------------+-------------------------------+
   | Field              | Attribute                     |
   +--------------------+-------------------------------+
   | Server ID          | 906                           |
   | Name               | SM-Console-A                  |
   | Machine Image ID   | 601                           |
   | Machine Image Name | RHEL-6.4_GA-x86_64-10-Hourly2 |
   | Architecture       | I64                           |
   | Product Size       | m1.medium                     |
   | Public IP Address  | None                          |
   | Private IP Address | 10.28.244.150                 |
   | Region ID          | 201                           |
   | Datacenter ID      | 204                           |
   | Datacenter Name    | us-east-1a                    |
   | Budget ID          | 200                           |
   | Owning User ID     | None                          |
   | Owning User Name   | None                          |
   | Owning User Email  | None                          |
   | Owning Group ID    | None                          |
   | Owning Group Name  | None                          |
   | Start Date         | 2014-05-20T19:39:01.000+0000  |
   | Description        | SM-Console-A                  |
   | Agent Version      | 0                             |
   | Status             | RUNNING                       |
   +--------------------+-------------------------------+
