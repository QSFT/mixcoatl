.. raw:: latex
  
      \newpage

.. _dcm_delete_billing_code:

dcm-delete-billing-code
-----------------------

Deletes a billing code.

Description
~~~~~~~~~~~

Deletes a billing code and returns if it was successful.

Syntax
~~~~~~

.. code-block:: bash

   usage: dcm-delete-billing-code [-h] [--billingcodeid BILLINGCODEID]
                                  [--reason REASON]
                                  [--replacementcodeid REPLACEMENTCODEID]

   optional arguments:
     -h, --help            show this help message and exit
     --billingcodeid BILLINGCODEID, -b BILLINGCODEID
                           Billing Code ID
     --reason REASON, -r REASON
                           The reason for deleting the billing code.
     --replacementcodeid REPLACEMENTCODEID, -R REPLACEMENTCODEID
                           Replacement code ID.

Options
~~~~~~~

+-------------------------+--------------------------------------------------------------+
| Option                  | Description                                                  |
+=========================+==============================================================+
| -b, --billingcodeid     | Billing Code ID of the billing code to be deleted.           |
|                         |                                                              |
|                         | Type: Integer                                                |
|                         |                                                              |
|                         | Default: None                                                |
|                         |                                                              |
|                         | Required: Yes                                                |
|                         |                                                              |
|                         | Example: 1130                                                |
+-------------------------+--------------------------------------------------------------+
| -r, --reason            | The reason for deleting the billing code.                    |
|                         |                                                              |
|                         | Type: String                                                 |
|                         |                                                              |
|                         | Default: None                                                |
|                         |                                                              |
|                         | Required: Yes                                                |
|                         |                                                              |
|                         | Example: Deprecated billing code.                            |
+-------------------------+--------------------------------------------------------------+
| -R, --replacementcodeid | Replacement code ID.                                         |
|                         |                                                              |
|                         | Type: Integer                                                |
|                         |                                                              |
|                         | Default: None                                                |
|                         |                                                              |
|                         | Required: Yes                                                |
|                         |                                                              |
|                         | Example: 300                                                 |
+-------------------------+--------------------------------------------------------------+

Common Options
~~~~~~~~~~~~~~

Deprecated Options
~~~~~~~~~~~~~~~~~~

None

Output
~~~~~~

Successful. (return code 0)
Failed. (return code 1)

Examples
~~~~~~~~

Example 1
^^^^^^^^^

.. code-block:: bash

   dcm-delete-billing-code -b 1133 -r 'Deprecated.' -R 300

Output
%%%%%%

.. code-block:: bash

   Successful.
