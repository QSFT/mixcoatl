.. raw:: latex
  
      \newpage

.. _dcm_delete_network:

dcm-delete-network
------------------

Deletes a network.

Description
~~~~~~~~~~~

Deletes a network.

Syntax
~~~~~~

.. code-block:: bash

   usage: dcm-delete-network [-h] [--networkid NETWORKID] [--reason REASON]

   optional arguments:
     -h, --help            show this help message and exit
     --networkid NETWORKID, -i NETWORKID
                           Network ID
     --reason REASON, -r REASON
                           The reason for deleting the network.

Options
~~~~~~~

+--------------------+--------------------------------------------------------------+
| Option             | Description                                                  |
+====================+==============================================================+
| -i, --networkid    | Network ID of the network to be deleted.                     |
|                    |                                                              |
|                    | Type: int                                                    |
|                    |                                                              |
|                    | Default: None                                                |
|                    |                                                              |
|                    | Required: Yes                                                |
|                    |                                                              |
|                    | Example: 1301                                                |
+--------------------+--------------------------------------------------------------+
| -r, --reason       | The reason for deleting the network.                         |
|                    |                                                              |
|                    | Type: String                                                 |
|                    |                                                              |
|                    | Default: None                                                |
|                    |                                                              |
|                    | Required: No                                                 |
|                    |                                                              |
|                    | Example: Test completed.                                     |
+--------------------+--------------------------------------------------------------+

Common Options
~~~~~~~~~~~~~~

Deprecated Options
~~~~~~~~~~~~~~~~~~

None

Output
~~~~~~

Job ID

Examples
~~~~~~~~

Example 1
^^^^^^^^^

.. code-block:: bash

   dcm-delete-network -i 1301

Output
%%%%%%

.. code-block:: bash
   
   58424
