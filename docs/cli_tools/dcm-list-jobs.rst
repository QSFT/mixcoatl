.. raw:: latex
  
      \newpage

.. _dcm_list_jobs:

dcm-list-jobs
-------------

List DCM jobs.

Description
~~~~~~~~~~~

Returns a list of DCM accounts. The list returned is subject to the scope of the API key.

Note that the End Date displayed in the output table for currently running jobs is the time the job information was
retrieved.

Syntax
~~~~~~

.. program-output:: dcm-list-jobs -h


Examples
~~~~~~~~

Example 1
^^^^^^^^^

.. code-block:: bash

   $ dcm-list-jobs
   +--------+----------------------------------+----------+------------------------------+------------------------------+---------------------------------+
   | ID     | Description                      | Status   | Start Date                   | End Date                     | Message                         |
   +--------+----------------------------------+----------+------------------------------+------------------------------+---------------------------------+
   | 817194 | Create Volume igable-deleteme-11 | RUNNING  | 2015-12-11T18:55:14.700+0000 | 2015-12-11T18:55:15.600+0000 | Checking provider volume status |
   | 817193 | Create Volume igable-deleteme-11 | COMPLETE | 2015-12-11T18:42:49.611+0000 | 2015-12-11T18:48:51.878+0000 | 127705                          |
   +--------+----------------------------------+----------+------------------------------+------------------------------+---------------------------------+

Example 2
^^^^^^^^^

.. code-block:: bash

   $ dcm-list-jobs -j 817194
   +--------+----------------------------------+---------+------------------------------+------------------------------+---------------------------------+
   | ID     | Description                      | Status  | Start Date                   | End Date                     | Message                         |
   +--------+----------------------------------+---------+------------------------------+------------------------------+---------------------------------+
   | 817194 | Create Volume igable-deleteme-11 | RUNNING | 2015-12-11T18:55:14.700+0000 | 2015-12-11T18:56:45.962+0000 | Checking provider volume status |
   +--------+----------------------------------+---------+------------------------------+------------------------------+---------------------------------+
