.. raw:: latex
  
      \newpage

.. _dcm_list_snapshots:

dcm-list-snapshots
------------------

Lists snapshots.

Description
~~~~~~~~~~~

Returns a list of snapshots.

Syntax
~~~~~~

.. program-output:: dcm-list-snapshots -h


The return value from this command is a list of snapshots.

Examples
~~~~~~~~

Example 1
^^^^^^^^^

.. code-block:: bash

   dcm-list-snapshots -r 201

Output
%%%%%%

.. code-block:: bash

   +-------------+---------------+---------------+-------+---------+------------------------------+
   | Snapshot ID |  Provider ID  | Snapshot Name | Group |  Budget |             Date             |
   +-------------+---------------+---------------+-------+---------+------------------------------+
   |      1      | snap-4dbe6fea | snap-4dbe6fea |  None | Default | 2014-03-22T21:01:59.000+0000 |
   +-------------+---------------+---------------+-------+---------+------------------------------+
