.. raw:: latex
  
      \newpage

.. _dcm_update_server_group:

dcm-update-server-group
----------------

Update the the owning group of a a server.


Syntax
~~~~~~

.. code-block:: bash

    usage: dcm-update-server-group [-h] --server_id SERVER_ID --group_id GROUP_ID

    optional arguments:
      -h, --help            show this help message and exit
      --server_id SERVER_ID, -s SERVER_ID
                            Server ID
      --group_id GROUP_ID, -g GROUP_ID
                            Group ID


Examples
~~~~~~~~

.. code-block:: bash

    $ dcm-update-server-group --server_id 95 --group_id 201
    Server with ID: 95 has changed to Group ID: 201

Related Topics
~~~~~~~~~~~~~~

:ref:`List Groups  <dcm_list_groups>`

