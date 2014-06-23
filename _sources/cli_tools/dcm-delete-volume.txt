.. raw:: latex
  
      \newpage

.. _dcm_delete_volume:

dcm-delete-volume
-----------------

Deletes a volume.

Description
~~~~~~~~~~~

Deletes a volume.

Syntax
~~~~~~

.. code-block:: bash

   usage: dcm-delete-volume [-h] [--reason REASON] volumeid

   positional arguments:
     volumeid              Volume ID

   optional arguments:
     -h, --help            show this help message and exit
     --reason REASON, -r REASON
                           The reason for deleting the volume.

Options
~~~~~~~

+--------------------+--------------------------------------------------------------+
| Option             | Description                                                  |
+====================+==============================================================+
| -r, --reason       | The reason for deleting the volume.                          |
|                    |                                                              |
|                    | Type: String                                                 |
|                    |                                                              |
|                    | Default: None                                                |
|                    |                                                              |
|                    | Required: No                                                 |
|                    |                                                              |
|                    | Example: Not needed anymore.                                 |
+--------------------+--------------------------------------------------------------+

Common Options
~~~~~~~~~~~~~~

Deprecated Options
~~~~~~~~~~~~~~~~~~

None

Output
~~~~~~

A text message to show if deleting was successful.

Examples
~~~~~~~~

Example 1
^^^^^^^^^

.. code-block:: bash

   dcm-delete-volume 48392

Output
%%%%%%

.. code-block:: bash
   
   Deleting the volume.
