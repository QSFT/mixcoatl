.. raw:: latex
  
      \newpage

.. _dcm_update_server_billing_code:

dcm-update-server-billing-code
------------------------------

Update the billing/budget code of a server.

Note that billing code has been replaced with budget in DCM, however Mixcoatl
maintains the use of of the word billing code to maintain backwards CLI compatibility.
Version 2.0 of Mixcoatl will replace billing-code with budget in all CLI commands.


Syntax
~~~~~~

.. program-output:: dcm-update-server-billing-code -h


Examples
~~~~~~~~

.. code-block:: bash

    $ dcm-update-server-billing-code --server_id 95 --billing_code 201
    Server with ID: 95 has changed to Billing Code: 201

Related Topics
~~~~~~~~~~~~~~

:ref:`List Billing Codes <dcm_list_billing_codes>`

:ref:`List Servers  <dcm_list_servers>`

