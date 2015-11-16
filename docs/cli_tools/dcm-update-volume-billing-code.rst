.. raw:: latex
  
      \newpage

.. _dcm_update_volume_billing_code:

dcm-update-volume-billing-code
------------------------------

Update the billing code/budget of a volume.

Note that billing code has been replaced with budget in DCM, however Mixcoatl
maintains the use of of the word billing code to maintain backwards CLI compatibility.
Version 2.0 of Mixcoatl will replace billing-code with budget in all CLI commands.


Syntax
~~~~~~

.. program-output:: dcm-update-volume-billing-code -h


Examples
~~~~~~~~

.. code-block:: bash

    $ dcm-update-volume-group --volume_id 95 --billing_code 201
    Volume with ID: 95 has changed to Billing Code: 201

Related Topics
~~~~~~~~~~~~~~

:ref:`List Billing Code  <dcm_list_billing_codes>`

:ref:`List Volumes  <dcm_list_volumes>`

