.. raw:: latex
  
      \newpage

.. _dcm_list_jobs:

dcm-list-jobs
-------------

List DCM jobs.

Description
~~~~~~~~~~~

Returns a list of DCM accounts. The list returned is subject to the scope of the API key.

Syntax
~~~~~~

.. code-block:: bash

   usage: dcm-list-jobs [-h] [--verbose] [--job-id JOB_ID]

   optional arguments:
   -h, --help            show this help message and exit
   --verbose, -v         Produce verbose output
   --job-id JOB_ID, -j JOB_ID Job ID


Options
~~~~~~~

+--------------------+------------------------------------------------------------+
| Option             | Description                                                |
+====================+============================================================+
| -v, --verbose      | Print out verbose information while listing jobs           |
+--------------------+------------------------------------------------------------+

Common Options
~~~~~~~~~~~~~~

Deprecated Options
^^^^^^^^^^^^^^^^^^

None

Output
~~~~~~

The output from this command is a list of DCM jobs when no argument is passed,
or if a job ID is passed, the return message from the job is provided.

Examples
~~~~~~~~

Example 1
^^^^^^^^^

.. code-block:: bash

   dcm-list-jobs

Output
%%%%%%

.. code-block:: bash

   +--------+-----------------------------+----------+------------------------------+------------------------------+----------------------------+
   | Job ID | Description                 |  Status  |          Start Date          |           End Date           |          Message           |
   +--------+-----------------------------+----------+------------------------------+------------------------------+----------------------------+
   |  901   | Terminate 1005              | COMPLETE | 2014-05-22T19:37:41.926+0000 | 2014-05-22T19:38:36.424+0000 |            None            |
   |  902   | Add Firewall Rule 0.0.0.0/0 | COMPLETE | 2014-05-22T19:38:20.903+0000 | 2014-05-22T19:38:36.422+0000 | ID: 800   Time: 15 seconds |
   |  900   | Terminate 1006              | RUNNING  | 2014-05-22T19:37:35.843+0000 |             None             |            None            |
   |  903   | Launch Server Test          | RUNNING  | 2014-05-22T19:38:41.982+0000 |             None             |            None            |
   +--------+-----------------------------+----------+------------------------------+------------------------------+----------------------------+

Example 2
^^^^^^^^^

.. code-block:: bash

   dcm-list-accounts -j 902

Output
%%%%%%

.. code-block:: json

   ID: 800   Time: 15 seconds

Example 3
^^^^^^^^^

.. code-block:: bash

   dcm-list-jobs

Output
%%%%%%

.. code-block:: bash

   +--------+-----------------------------+----------+------------------------------+------------------------------+----------------------------+
   | Job ID | Description                 |  Status  |          Start Date          |           End Date           |          Message           |
   +--------+-----------------------------+----------+------------------------------+------------------------------+----------------------------+
   |  903   | Launch Server Test          | COMPLETE | 2014-05-22T19:38:41.982+0000 | 2014-05-22T19:40:00.430+0000 |            1100            |
   |  904   | CREATE VOLUME               | RUNNING  | 2014-05-22T19:41:11.917+0000 |             None             |            None            |
   |  905   | Create Image cirros-image   | RUNNING  | 2014-05-22T19:42:09.985+0000 |             None             |       Bundling Image       |
   +--------+-----------------------------+----------+------------------------------+------------------------------+----------------------------+

Example 4
^^^^^^^^^

.. code-block:: bash

   dcm-list-jobs -j 905

Output
%%%%%%

.. code-block:: bash

   Bundling Image
