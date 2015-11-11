.. raw:: latex
  
      \newpage

.. _dcm_list_regions:

dcm-list-regions
----------------

List regions.

Description
~~~~~~~~~~~

Returns a list of regions.

Syntax
~~~~~~

.. program-output:: dcm-list-regions -h

Options
~~~~~~~

+--------------------+------------------------------------------------------------+
| Option             | Description                                                |
+====================+============================================================+
| -v, --verbose      | Print out verbose information while listing regions        |
+--------------------+------------------------------------------------------------+

Common Options
~~~~~~~~~~~~~~

Deprecated Options
^^^^^^^^^^^^^^^^^^

None

Output
~~~~~~

The return value from this command is a list of DCM regions

Examples
~~~~~~~~

Example 1
^^^^^^^^^

.. code-block:: bash

   dcm-list-regions

Output
%%%%%%

.. code-block:: bash

   +-----------+----------------+--------+----------------+----------------+--------+
   | Region ID |  Provider ID   | Cloud  |  Region Name   |  Description   | Status |
   +-----------+----------------+--------+----------------+----------------+--------+
   |    1403   | ap-northeast-1 | Amazon | ap-northeast-1 | ap-northeast-1 | ACTIVE |
   |    1406   | ap-southeast-1 | Amazon | ap-southeast-1 | ap-southeast-1 | ACTIVE |
   |    1407   | ap-southeast-2 | Amazon | ap-southeast-2 | ap-southeast-2 | ACTIVE |
   |    1400   |   eu-west-1    | Amazon |   eu-west-1    |   eu-west-1    | ACTIVE |
   |    1401   |   sa-east-1    | Amazon |   sa-east-1    |   sa-east-1    | ACTIVE |
   |    1402   |   us-east-1    | Amazon |   us-east-1    |   us-east-1    | ACTIVE |
   |    1405   |   us-west-1    | Amazon |   us-west-1    |   us-west-1    | ACTIVE |
   |    1404   |   us-west-2    | Amazon |   us-west-2    |   us-west-2    | ACTIVE |
   +-----------+----------------+--------+----------------+----------------+--------+

Example 2
^^^^^^^^^

.. code-block:: bash

   dcm-list-regions

Output
%%%%%%

.. code-block:: bash

   +-----------+-------------+-----------+-------------+-------------+--------+
   | Region ID | Provider ID | Cloud     | Region Name | Description | Status |
   +-----------+-------------+-----------+-------------+-------------+--------+
   | 300       | RegionOne   | OpenStack | RegionOne   | RegionOne   | ACTIVE |
   +-----------+-------------+-----------+-------------+-------------+--------+
