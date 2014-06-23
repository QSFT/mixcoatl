.. raw:: latex
  
      \newpage

.. _dcm_describe_job:

dcm-describe-job
----------------

Describe a job.

Description
~~~~~~~~~~~

Returns a short summary about a job.

Syntax
~~~~~~

.. code-block:: bash

   usage: dcm-describe-job [-h] [--verbose] jobid

   positional arguments:
     jobid          Job ID

   optional arguments:
     -h, --help     show this help message and exit
     --verbose, -v  Produce verbose output.

Options
~~~~~~~

+--------------------+----------------------------------------------------------------+
| Option             | Description                                                    |
+====================+================================================================+
| -v, --verbose      | Print out verbose information while describing a job.          |
+--------------------+----------------------------------------------------------------+

Common Options
~~~~~~~~~~~~~~

Deprecated Options
^^^^^^^^^^^^^^^^^^

None

Output
~~~~~~

The output of this command is a short summary of information about a job given a job ID.

Examples
~~~~~~~~

Example 1
^^^^^^^^^

.. code-block:: bash

   dcm-describe-job 3219

Output
%%%%%%

.. code-block:: bash
   +-------------+------------------------------+
   |    Field    |          Attribute           |
   +-------------+------------------------------+
   |    Job ID   |             3219             |
   | Description | Create Network test-network  |
   |  Start Date | 2014-05-23T05:04:37.553+0000 |
   |   End Date  |             None             |
   |    Status   |           RUNNING            |
   |   Message   |             None             |
   +-------------+------------------------------+
