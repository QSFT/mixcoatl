.. raw:: latex
  
      \newpage

.. _dcm_list_billing_codes:

dcm-list-billing-codes
----------------------

List billing (budget codes).

Description
~~~~~~~~~~~

Returns a list of all budget codes in table format or if called using the `-v` option, a JSON response.

Syntax
~~~~~~

.. code-block:: bash

   dcm-list-billing-codes --help
   usage: dcm-list-billing-codes [-h] [--verbose]
   
   optional arguments:
     -h, --help     show this help message and exit
     --verbose, -v  Produce verbose output

Options
~~~~~~~

+--------------------+------------------------------------------------------------+
| Option             | Description                                                |
+====================+============================================================+
| -v, --verbose      | Print out verbose information while listing billing codes. |
+--------------------+------------------------------------------------------------+

Common Options
~~~~~~~~~~~~~~

Deprecated Options
^^^^^^^^^^^^^^^^^^

None

Output
~~~~~~

The return value from this command is information about billing codes.

Examples
~~~~~~~~

Example 1
^^^^^^^^^

.. code-block:: bash

   dcm-list-billing-codes

Output
%%%%%%

.. code-block:: bash

   +-----+----------------+-------------+------------+-------------+---------------+-----------------+--------+
   |  ID |      Name      | Budget Code | Soft Quota |  Hard Quota | Current Usage | Projected Usage | Status |
   +-----+----------------+-------------+------------+-------------+---------------+-----------------+--------+
   | 819 |    Default     |     DEF     |    0.00    |     0.00    |  USD 1718.75  |   USD 2598.71   | ACTIVE |
   +-----+----------------+-------------+------------+-------------+---------------+-----------------+--------+

Example 2
^^^^^^^^^

.. code-block:: bash

   dcm-list-billing-codes -v

Output
%%%%%%

.. code-block:: json

   {'billing_code_id': 819,
    'budget_state': 'NORMAL',
    'current_job': None,
    'current_usage': {'currency': 'USD', 'value': 1719.0999755859375},
    'customer': {'accounting_currency': 'USD',
                 'automated_exchange_rates': True,
                 'business_name': 'DCM CSE',
                 'created': '2014-04-28T15:46:58.580+0000',
                 'created_timestamp': '2014-04-28T15:46:58.580+0000',
                 'customer_id': 816,
                 'status': 'ACTIVE',
                 'time_zone': 'UTC',
                 'web_site': 'http://www.dell.com'},
    'description': 'Default Billing Code',
    'finance_code': 'DEF',
    'hard_quota': None,
    'last_error': None,
    'last_request': '<Response [200]>',
    'name': 'Default',
    'path': 'admin/BillingCode/819',
    'projected_usage': {'currency': 'USD', 'value': 2599.070068359375},
    'request_details': 'extended',
    'soft_quota': None,
    'status': 'ACTIVE'}

Related Topics
~~~~~~~~~~~~~~

:ref:`Create Billing Code <dcm_create_billing_code>`
