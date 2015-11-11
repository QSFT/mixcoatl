.. raw:: latex
  
      \newpage

.. _dcm_create_billing_code:

dcm-create-billing-code
-----------------------

Create a DCM billing/budget code. The terms `billing` and `budget` are used
interchangeably.

Description
~~~~~~~~~~~

Billing codes are used to track 'spend' and are required whenever resources
that incur cost are provisioned.

Syntax
~~~~~~

.. program-output:: dcm-create-billing-code -h

Options
~~~~~~~

+--------------------+-------------------------------------------------------+
| Option             | Description                                           |
+====================+=======================================================+
| -n, --name         | The name of the billing code                          | 
|                    |                                                       |
|                    | Type: String                                          |
|                    |                                                       |
|                    | Default: None                                         |
|                    |                                                       |
|                    | Required: Yes                                         |
|                    |                                                       |
|                    | Example: 'Operations'                                 |
+--------------------+-------------------------------------------------------+
| -d, --description  | The description of the billing code                   | 
|                    |                                                       |
|                    | Type: String                                          |
|                    |                                                       |
|                    | Default: None                                         |
|                    |                                                       |
|                    | Required: Yes                                         |
|                    |                                                       |
+--------------------+-------------------------------------------------------+
| -c, --code         | A short/friendly name for the billing code            | 
|                    |                                                       |
|                    | Type: String                                          |
|                    |                                                       |
|                    | Default: None                                         |
|                    |                                                       |
|                    | Required: Yes                                         |
|                    |                                                       |
+--------------------+-------------------------------------------------------+
| --soft             | The value of the soft quota                           | 
|                    |                                                       |
|                    | Type: Integer                                         |
|                    |                                                       |
|                    | Default: None                                         |
|                    |                                                       |
|                    | Required: Yes                                         |
|                    |                                                       |
+--------------------+-------------------------------------------------------+
| --hard             | The value of the hard quota                           | 
|                    |                                                       |
|                    | Type: Integer                                         |
|                    |                                                       |
|                    | Default: None                                         |
|                    |                                                       |
|                    | Required: Yes                                         |
|                    |                                                       |
+--------------------+-------------------------------------------------------+
| -v, --verbose      | Print out verbose information about the role creation |
+--------------------+-------------------------------------------------------+

Common Options
~~~~~~~~~~~~~~

Deprecated Options
^^^^^^^^^^^^^^^^^^

None

Output
~~~~~~

None

Examples
~~~~~~~~

.. code-block:: bash

   dcm-create-billing-code -n test -d 'Operations' --soft 100 --hard 200 -c OPS

   5123

Related Topics
~~~~~~~~~~~~~~

:ref:`List Billing Codes <dcm_list_billing_codes>`
