.. raw:: latex
  
      \newpage

.. _dcm_list_users:

dcm-list-users
--------------

List users.

Description
~~~~~~~~~~~

Returns a list of users.

Syntax
~~~~~~

.. code-block:: bash

   usage: dcm-list-users [-h] [--verbose]

   optional arguments:
     -h, --help     show this help message and exit
     --verbose, -v  Produce verbose output

Options
~~~~~~~

+--------------------+-------------------------------------------------------------+
| Option             | Description                                                 |
+====================+=============================================================+
| -v, --verbose      | Print out verbose information while listing users.          |
+--------------------+-------------------------------------------------------------+

Common Options
~~~~~~~~~~~~~~

Deprecated Options
^^^^^^^^^^^^^^^^^^

None

Output
~~~~~~

The return value from this command is a list of DCM users.

Example
~~~~~~~

.. code-block:: bash

   dcm-list-users

Output
%%%%%%

.. code-block:: bash

   +---------+-------------+--------------+------------+--------------------------------+--------------------+
   | User ID | VM Login ID |  Last Name   | First Name |                  Email         |       Groups       |
   +---------+-------------+--------------+------------+--------------------------------+--------------------+
   |  50938  |      p1     |     User     |   Admin    |        admin@exmpale.com       |       Admin        |
   |  50940  |     p200    |    basic     |    user    |     basic_user@example.com     |    basic group     |
   |  50941  |     p201    |    basic     |   user2    |     basic_user2@example.com    |    basic group     |
   |  50942  |     p202    | intermediate |    user    |  intermediate_user@example.com | intermediate group |
   |  50943  |     p203    | intermediate |   user2    | intermediate_user2@example.com | intermediate group |
   |  50944  |     p204    |   advanced   |    user    |    advanced_user@example.com   |   advanced group   |
   |  50945  |     p205    |   advanced   |   user2    |   advanced_user2@example.com   |   advanced group   |
   +---------+-------------+--------------+------------+--------------------------------+--------------------+

