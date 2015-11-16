.. raw:: latex
  
      \newpage

.. _dcm_list_server_products:

dcm-list-server-products
------------------------

List server products for a region.

Description
~~~~~~~~~~~

Returns available server products. You can filter the list of products by :ref:`region ID <dcm_list_regions>` and
by :ref:`provider region ID <dcm_list_regions>`.

Syntax
~~~~~~

.. program-output:: dcm-list-server-products -h

Options
~~~~~~~

+-------------------------+-------------------------------------------------------+
| Option                  | Description                                           |
+=========================+=======================================================+
| -r, --regionid          | The region for which server products will be listed   |
|                         |                                                       |
|                         | Type: String/Integer                                  |
|                         |                                                       |
|                         | Default: None                                         |
|                         |                                                       |
|                         | Required: No                                          |
|                         |                                                       |
|                         | Example: 1403                                         |
+-------------------------+-------------------------------------------------------+
|-p, --regionpid          | The provider product id which server products will be |
|                         | listed.                                               |
|                         |                                                       |
|                         | Type: String/Integer                                  |
|                         |                                                       |
|                         | Default: None                                         |
|                         |                                                       |
|                         | Required: No                                          |
|                         |                                                       |
|                         | Example: us-east-1                                    |
+-------------------------+-------------------------------------------------------+
| -v, --verbose           | Print out verbose information while listing regions   |
+-------------------------+-------------------------------------------------------+

Common Options
~~~~~~~~~~~~~~

Deprecated Options
^^^^^^^^^^^^^^^^^^

None

Output
~~~~~~

The output is information about server products for a region.

Examples
~~~~~~~~

Example 1
^^^^^^^^^

.. code-block:: bash

   dcm-list-server-products --regionpid us-east-1

Output
%%%%%%

.. code-block:: bash

   +-------------------+--------------------+---------------------+----------------------+----------+----------+-------------+
   | Server Product ID | Provider Region ID | Provider Product ID | Name                 | Platform | Currency | Hourly Rate |
   +-------------------+--------------------+---------------------+----------------------+----------+----------+-------------+
   | 2052              | us-east-1          | c1.medium           | c1.medium            | SUSE     | USD      | 0.23        |
   | 2053              | us-east-1          | c1.medium           | c1.medium            | SUSE     | USD      | 0.23        |
   | 1452              | us-east-1          | c1.medium           | c1.medium            | RHEL     | USD      | 0.19        |
   | 1453              | us-east-1          | c1.medium           | c1.medium            | RHEL     | USD      | 0.19        |
   | 3039              | us-east-1          | c1.medium           | c1.medium            | UNIX     | USD      | 0.13        |
   | 3040              | us-east-1          | c1.medium           | High-CPU Medium      | UNKNOWN  | USD      | 0.145       |
   | 3041              | us-east-1          | c1.medium           | c1.medium            | UNIX     | USD      | 0.13        |
   | 3042              | us-east-1          | c1.medium           | High-CPU Medium      | UNKNOWN  | USD      | 0.145       |
   | 3043              | us-east-1          | c1.medium           | c1.medium            | WINDOWS  | USD      | 0.21        |
   | 3044              | us-east-1          | c1.medium           | c1.medium            | WINDOWS  | USD      | 0.21        |
   | 2055              | us-east-1          | c1.xlarge           | c1.xlarge            | SUSE     | USD      | 0.62        |
   | 1455              | us-east-1          | c1.xlarge           | c1.xlarge            | RHEL     | USD      | 0.65        |
   | 3045              | us-east-1          | c1.xlarge           | c1.xlarge            | UNIX     | USD      | 0.52        |
   | 3046              | us-east-1          | c1.xlarge           | High-CPU Extra Large | UNKNOWN  | USD      | 0.58        |
   | 3047              | us-east-1          | c1.xlarge           | c1.xlarge            | WINDOWS  | USD      | 0.84        |
   | 523               | us-east-1          | c3.2xlarge          | c3.2xlarge           | UNKNOWN  | USD      | 0.42        |
   | 2317              | us-east-1          | c3.2xlarge          | c3.2xlarge           | WINDOWS  | USD      | 0.752       |
   | 1119              | us-east-1          | c3.2xlarge          | c3.2xlarge           | RHEL     | USD      | 0.55        |
   | 1719              | us-east-1          | c3.2xlarge          | c3.2xlarge           | SUSE     | USD      | 0.52        |
   +-------------------+--------------------+---------------------+----------------------+----------+----------+-------------+


Example 2
^^^^^^^^^

.. code-block:: bash

   dcm-list-server-products -r 1403

Output
%%%%%%

.. code-block:: bash

   +-------------------+--------------------+---------------------+-----------------------------------+----------+----------+-------------+
   | Server Product ID | Provider Region ID | Provider Product ID |                Name               | Platform | Currency | Hourly Rate |
   +-------------------+--------------------+---------------------+-----------------------------------+----------+----------+-------------+
   |        3330       |   ap-northeast-1   |      c1.medium      |          High-CPU Medium          |   UNIX   |   USD    |    0.185    |
   |        3332       |   ap-northeast-1   |      c1.medium      |          High-CPU Medium          |   UNIX   |   USD    |    0.185    |
   |        3331       |   ap-northeast-1   |      c1.medium      |          High-CPU Medium          | UNKNOWN  |   USD    |    0.185    |
   |        3333       |   ap-northeast-1   |      c1.medium      |          High-CPU Medium          | UNKNOWN  |   USD    |    0.185    |
   |        3334       |   ap-northeast-1   |      c1.medium      |          High-CPU Medium          | WINDOWS  |   USD    |    0.285    |
   |        3335       |   ap-northeast-1   |      c1.medium      |          High-CPU Medium          | WINDOWS  |   USD    |    0.285    |
   |        3336       |   ap-northeast-1   |      c1.xlarge      |        High-CPU Extra Large       |   UNIX   |   USD    |     0.74    |
   |        3337       |   ap-northeast-1   |      c1.xlarge      |        High-CPU Extra Large       | UNKNOWN  |   USD    |     0.74    |
   |        3338       |   ap-northeast-1   |      c1.xlarge      |        High-CPU Extra Large       | WINDOWS  |   USD    |     1.14    |
   |        3303       |   ap-northeast-1   |       m1.large      |               Large               |   UNIX   |   USD    |     0.35    |
   |        3304       |   ap-northeast-1   |       m1.large      |               Large               | UNKNOWN  |   USD    |     0.35    |
   |        3305       |   ap-northeast-1   |       m1.large      |               Large               | WINDOWS  |   USD    |     0.46    |
   |        3297       |   ap-northeast-1   |      m1.medium      |               Medium              |   UNIX   |   USD    |    0.175    |
   |        3299       |   ap-northeast-1   |      m1.medium      |               Medium              |   UNIX   |   USD    |    0.175    |
   |        3298       |   ap-northeast-1   |      m1.medium      |               Medium              | UNKNOWN  |   USD    |    0.175    |
   |        3300       |   ap-northeast-1   |      m1.medium      |               Medium              | UNKNOWN  |   USD    |    0.175    |
   |        3301       |   ap-northeast-1   |      m1.medium      |               Medium              | WINDOWS  |   USD    |     0.23    |
   |        3302       |   ap-northeast-1   |      m1.medium      |               Medium              | WINDOWS  |   USD    |     0.23    |
   |        3291       |   ap-northeast-1   |       m1.small      |               Small               |   UNIX   |   USD    |    0.088    |
   |        3293       |   ap-northeast-1   |       m1.small      |               Small               |   UNIX   |   USD    |    0.088    |
   |        3292       |   ap-northeast-1   |       m1.small      |               Small               | UNKNOWN  |   USD    |    0.088    |
   |        3294       |   ap-northeast-1   |       m1.small      |               Small               | UNKNOWN  |   USD    |    0.088    |
   |        3295       |   ap-northeast-1   |       m1.small      |               Small               | WINDOWS  |   USD    |    0.115    |
   |        3296       |   ap-northeast-1   |       m1.small      |               Small               | WINDOWS  |   USD    |    0.115    |
   |        3306       |   ap-northeast-1   |      m1.xlarge      |            Extra Large            |   UNIX   |   USD    |     0.7     |
   |        3307       |   ap-northeast-1   |      m1.xlarge      |            Extra Large            | UNKNOWN  |   USD    |     0.7     |
   |        3308       |   ap-northeast-1   |      m1.xlarge      |            Extra Large            | WINDOWS  |   USD    |     0.92    |
   |        3324       |   ap-northeast-1   |      m2.2xlarge     |   High-Memory Double Extra Large  |   UNIX   |   USD    |     1.01    |
   |        3325       |   ap-northeast-1   |      m2.2xlarge     |   High-Memory Double Extra Large  | UNKNOWN  |   USD    |     1.01    |
   |        3326       |   ap-northeast-1   |      m2.2xlarge     |   High-Memory Double Extra Large  | WINDOWS  |   USD    |     1.14    |
   |        3327       |   ap-northeast-1   |      m2.4xlarge     | High-Memory Quadruple Extra Large |   UNIX   |   USD    |     2.02    |
   |        3328       |   ap-northeast-1   |      m2.4xlarge     | High-Memory Quadruple Extra Large | UNKNOWN  |   USD    |     2.02    |
   |        3329       |   ap-northeast-1   |      m2.4xlarge     | High-Memory Quadruple Extra Large | WINDOWS  |   USD    |     2.28    |
   |        3321       |   ap-northeast-1   |      m2.xlarge      |      High-Memory Extra Large      |   UNIX   |   USD    |    0.505    |
   |        3322       |   ap-northeast-1   |      m2.xlarge      |      High-Memory Extra Large      | UNKNOWN  |   USD    |    0.505    |
   |        3323       |   ap-northeast-1   |      m2.xlarge      |      High-Memory Extra Large      | WINDOWS  |   USD    |     0.57    |
   |        3312       |   ap-northeast-1   |      m3.2xlarge     |   M3 Double Extra Large Instance  |   UNIX   |   USD    |     1.52    |
   |        3313       |   ap-northeast-1   |      m3.2xlarge     |   M3 Double Extra Large Instance  | UNKNOWN  |   USD    |     1.52    |
   |        3314       |   ap-northeast-1   |      m3.2xlarge     |   M3 Double Extra Large Instance  | WINDOWS  |   USD    |     1.96    |
   |        3309       |   ap-northeast-1   |      m3.xlarge      |      M3 Extra Large Instance      |   UNIX   |   USD    |     0.76    |
   |        3310       |   ap-northeast-1   |      m3.xlarge      |      M3 Extra Large Instance      | UNKNOWN  |   USD    |     0.76    |
   |        3311       |   ap-northeast-1   |      m3.xlarge      |      M3 Extra Large Instance      | WINDOWS  |   USD    |     0.98    |
   |        3315       |   ap-northeast-1   |       t1.micro      |               Micro               |   UNIX   |   USD    |    0.027    |
   |        3317       |   ap-northeast-1   |       t1.micro      |               Micro               |   UNIX   |   USD    |    0.027    |
   |        3316       |   ap-northeast-1   |       t1.micro      |               Micro               | UNKNOWN  |   USD    |    0.027    |
   |        3318       |   ap-northeast-1   |       t1.micro      |               Micro               | UNKNOWN  |   USD    |    0.027    |
   |        3319       |   ap-northeast-1   |       t1.micro      |               Micro               | WINDOWS  |   USD    |    0.035    |
   |        3320       |   ap-northeast-1   |       t1.micro      |               Micro               | WINDOWS  |   USD    |    0.035    |
   +-------------------+--------------------+---------------------+-----------------------------------+----------+----------+-------------+

Example 3
^^^^^^^^^

.. code-block:: bash

   dcm-list-server-products -r 1403 -v

Output
%%%%%%

The output from this command is lengthy, to view it, please :download:`click here <./files/verbose_server_product.txt>`
