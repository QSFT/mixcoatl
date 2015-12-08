.. raw:: latex
  
      \newpage

.. _dcm_update_machine_image_billing_code:

dcm-update-machine-image-billing-code
-------------------------------------

Update the billing/budged code of a machine image.

Note that billing code has been replaced with budget in DCM, however Mixcoatl
maintains the use of of the word billing code to maintain backwards CLI compatibility.
Version 2.0 of Mixcoatl will replace billing-code with budget in all CLI commands.


Syntax
~~~~~~

.. program-output:: dcm-update-machine-image-billing-code -h


Examples
~~~~~~~~

.. code-block:: bash

    $ dcm-update-machine-image-billing-code --machine_image_id 95 --billing_code 201
    Machine Image with ID: 95 has changed to Billing Code: 201

Related Topics
~~~~~~~~~~~~~~

:ref:`List Billing Codes  <dcm_list_billing_codes>`

:ref:`List Machine Images  <dcm_list_machine_images>`

