.. raw:: latex
  
      \newpage

.. _dcm_check_job:

dcm-check-job
-------------

Checks status of a job.

Description
~~~~~~~~~~~

Returns status of a job.

Syntax
~~~~~~

.. code-block:: bash

   usage: dcm-check-job [-h] jobid

   Check if Job was successfully completed. Possible return values are COMPLETE for completed job, ERROR for failed job, NONE for nonexistent job.

   positional arguments:
     jobid       Job ID

   optional arguments:
     -h, --help  show this help message and exit

Options
~~~~~~~

None

Common Options
~~~~~~~~~~~~~~

Deprecated Options
^^^^^^^^^^^^^^^^^^

None

Output
~~~~~~

The return value from this command is status of a job.

Examples
~~~~~~~~

Example 1
^^^^^^^^^

.. code-block:: bash

   dcm-check-job 3208
   
Output
%%%%%%

.. code-block:: bash

   RUNNING
