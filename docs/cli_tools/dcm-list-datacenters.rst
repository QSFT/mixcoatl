.. raw:: latex
  
      \newpage

.. _dcm_list_datacenters:

dcm-list-datacenters
--------------------

Lists datacenters.

Description
~~~~~~~~~~~

Returns a list of datacenters within a region.

Syntax
~~~~~~

.. program-output:: dcm-list-datacenters -h

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
|                    | Required: Yes (if regionpid was not specified)             |
|                    |                                                            |
|                    | Example: 200                                               |
+--------------------+------------------------------------------------------------+
| -R, --regionpid    | Region Provider ID.                                        |
|                    |                                                            |
|                    | Type: Str                                                  |
|                    |                                                            |
|                    | Default: None                                              |
|                    |                                                            |
|                    | Required: Yes (if regionid was not specified)              |
|                    |                                                            |
|                    | Example: us-west-1                                         |
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

The return value from this command is a list of datacenters.

Examples
~~~~~~~~

Example 1
^^^^^^^^^

.. code-block:: bash

   dcm-list-datacenters -r 201

Output
%%%%%%

.. code-block:: bash

   +---------------+-------------+-------------+--------+
   | Datacenter ID | Provider ID | Description | Status |
   +---------------+-------------+-------------+--------+
   |      204      |  us-east-1b |  us-east-1b | ACTIVE |
   |      205      |  us-east-1c |  us-east-1c | ACTIVE |
   |      206      |  us-east-1d |  us-east-1d | ACTIVE |
   +---------------+-------------+-------------+--------+
