.. raw:: latex
  
      \newpage

.. _dcm_list_rdbms_products:

dcm-list-rdbms-products
-----------------------

List RDBMS products.

Description
~~~~~~~~~~~

Returns a list of RDBMS products.

Syntax
~~~~~~

.. code-block:: bash

   usage: dcm-list-rdbms-products [-h] [--regionid REGIONID] [--engine ENGINE]
                                  [--verbose]

   optional arguments:
     -h, --help            show this help message and exit
     --regionid REGIONID, -r REGIONID
                           Region ID
     --engine ENGINE, -e ENGINE
                           DB engine. examples: MYSQL51, MYSQL55, ORACLE11G,
                           ORACLE11GEX, ORACLE11GX
     --verbose, -v         Produce verbose output

Options
~~~~~~~

+--------------------+---------------------------------------------------------------+
| Option             | Description                                                   |
+====================+===============================================================+
| -r, --regionid     | Region ID.                                                    |
|                    |                                                               |
|                    | Type: Integer                                                 |
|                    |                                                               |
|                    | Default: None                                                 |
|                    |                                                               |
|                    | Required: Yes                                                 |
|                    |                                                               |
|                    | Example: 201                                                  |
+--------------------+---------------------------------------------------------------+
| -e, --engine       | RDBMS engine.                                                 |
|                    |                                                               |
|                    | Default: None                                                 |
|                    |                                                               |
|                    | Required: Yes                                                 |
|                    |                                                               |
|                    | Example: MYSQL51, MYSQL55, ORACLE11G, ORACLE11GEX, ORACLE11GX |
+--------------------+---------------------------------------------------------------+
| -v, --verbose      | Print out verbose information while listing RDBMS products.   |
+--------------------+---------------------------------------------------------------+

Common Options
~~~~~~~~~~~~~~

Deprecated Options
^^^^^^^^^^^^^^^^^^

None

Output
~~~~~~

The return value from this command is a list of RDBMS products.

Examples
~~~~~~~~

Example 1
^^^^^^^^^

.. code-block:: bash

   dcm-list-rdbms-products -r 303 -e MYSQL51
   
Output
%%%%%%

.. code-block:: bash

   +------------------+-----------------------------------------------+---------------------+---------+----------+----------------+----------------+-----------------+
   | RDBMS Product ID |                      Name                     | Provider Product ID |  Engine | Currency | Hourly Pricing |   IO Pricing   | Storage Pricing |
   +------------------+-----------------------------------------------+---------------------+---------+----------+----------------+----------------+-----------------+
   |       161        |               Micro DB Instance               |     db.t1.micro     | MYSQL51 |   USD    | 0.035000000149 | 0.109999999404 |  0.109999999404 |
   |       163        |               Small DB Instance               |     db.m1.small     | MYSQL51 |   USD    | 0.097999997437 | 0.109999999404 |  0.109999999404 |
   |       165        |               Medium DB Instance              |     db.m1.medium    | MYSQL51 |   USD    | 0.194999992847 | 0.109999999404 |  0.109999999404 |
   |       167        |               Large DB Instance               |     db.m1.large     | MYSQL51 |   USD    | 0.395999997854 | 0.109999999404 |  0.109999999404 |
   |       169        |            Extra Large DB Instance            |     db.m1.xlarge    | MYSQL51 |   USD    | 0.791000008583 | 0.109999999404 |  0.109999999404 |
   |       171        |      High-Memory Extra Large DB Instance      |     db.m2.xlarge    | MYSQL51 |   USD    | 0.65499997139  | 0.109999999404 |  0.109999999404 |
   |       173        |   High-Memory Double Extra Large DB Instance  |    db.m2.2xlarge    | MYSQL51 |   USD    | 1.31500005722  | 0.109999999404 |  0.109999999404 |
   |       175        | High-Memory Quadruple Extra Large DB Instance |    db.m2.4xlarge    | MYSQL51 |   USD    | 2.63000011444  | 0.109999999404 |  0.109999999404 |
   +------------------+-----------------------------------------------+---------------------+---------+----------+----------------+----------------+-----------------+
