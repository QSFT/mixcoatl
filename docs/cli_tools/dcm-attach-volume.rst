.. raw:: latex
  
      \newpage

.. _dcm_attach_volume:

dcm-attach-volume
-----------------

Attach a volume to server.

Description
~~~~~~~~~~~

Attach a volume to server with optional specific device ID.

Syntax
~~~~~~

.. program-output:: dcm-attach-volume -h

Options
~~~~~~~

+---------------------+-------------------------------------------------------+
| Option              | Description                                           |
+=====================+=======================================================+
| -v, --volumeid      | Volume ID of the volume to be attached.               |
|                     |                                                       |
|                     | Type: Integer                                         |
|                     |                                                       |
|                     | Default: None                                         |
|                     |                                                       |
|                     | Required: Yes                                         |
|                     |                                                       |
+---------------------+-------------------------------------------------------+
| -s, --serverid      | Server ID of the server to attach the volume.         | 
|                     |                                                       |
|                     | Type: Integer                                         |
|                     |                                                       |
|                     | Default: None                                         |
|                     |                                                       |
|                     | Required: Yes                                         |
|                     |                                                       |
+---------------------+-------------------------------------------------------+
| -d, --deviceid      | Device ID such as /dev/xvdh                           |
|                     |                                                       |
|                     | Type: String                                          |
|                     |                                                       |
|                     | Default: None                                         |
|                     |                                                       |
|                     | Required: No                                          |
|                     |                                                       |
+---------------------+-------------------------------------------------------+

Output
~~~~~~

The return value from this command will be the job ID of the created job.


Examples
~~~~~~~~

.. code-block:: bash

   dcm-attach-volume -v 1103 -s 57432 -d '/dev/xvdh'

Related Topics
~~~~~~~~~~~~~~

:ref:`List Servers <dcm_list_servers>`

:ref:`List Volumes <dcm_list_volumes>`

