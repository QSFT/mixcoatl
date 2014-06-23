.. raw:: latex
  
      \newpage

.. _dcm_detach_volume:

dcm-detach-volume
-----------------

Detaches a volume from server.

Description
~~~~~~~~~~~

Detaches a volume from server.

Syntax
~~~~~~

.. code-block:: bash

   dcm-detach-volume -v <volume_id>

Options
~~~~~~~

+---------------------+-------------------------------------------------------+
| Option              | Description                                           |
+=====================+=======================================================+
| -v, --volumeid      | Volume ID of the volume to be detached.               |
|                     |                                                       |
|                     | Type: Integer                                         |
|                     |                                                       |
|                     | Default: None                                         |
|                     |                                                       |
|                     | Required: Yes                                         |
|                     |                                                       |
+---------------------+-------------------------------------------------------+

Output
~~~~~~

None


Examples
~~~~~~~~

.. code-block:: bash

   dcm-detach-volume -v 1105

Related Topics
~~~~~~~~~~~~~~

:ref:`List Servers <dcm_list_servers>`

:ref:`List Volumes <dcm_list_volumes>`

:ref:`Attach Volume <dcm_attach_volume>`

