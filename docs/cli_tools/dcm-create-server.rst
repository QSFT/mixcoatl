.. raw:: latex

      \newpage

.. _dcm_create_server:

dcm-create-server
-----------------

Creates a server.

Description
~~~~~~~~~~~

Creates a server from a specified machine image.

Syntax
~~~~~~

.. program-output:: dcm-create-server -h


Output
~~~~~~

Job ID

Examples
~~~~~~~~

.. code-block:: bash

   dcm-create-server -m 34251 -d 7659 -n 'linux-demo-server' -D 'Linux demonstration server' -b 100

   54830

Related Topics
~~~~~~~~~~~~~~

:ref:`List Servers <dcm_list_servers>`

