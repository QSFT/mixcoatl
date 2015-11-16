.. raw:: latex
  
      \newpage

.. _dcm_assign_cloud:

dcm-assign-cloud
----------------

Assign cloud account to DCM account.

Description
~~~~~~~~~~~

Assign cloud account to DCM account using cloud credentials.

Syntax
~~~~~~

.. program-output:: dcm-assign-cloud -h

Options
~~~~~~~

+---------------------+-------------------------------------------------------+
| Option              | Description                                           |
+=====================+=======================================================+
| -c, --cloudid       | Cloud ID in DCM. Run dcm-list-clouds to get ID.       |
|                     |                                                       |
|                     | Type: Integer                                         |
|                     |                                                       |
|                     | Default: None                                         |
|                     |                                                       |
|                     | Required: Yes                                         |
|                     |                                                       |
+---------------------+-------------------------------------------------------+
| -i, --accountid     | DCM Account ID                                        | 
|                     |                                                       |
|                     | Type: Integer                                         |
|                     |                                                       |
|                     | Default: None                                         |
|                     |                                                       |
|                     | Required: Yes                                         |
|                     |                                                       |
+---------------------+-------------------------------------------------------+
| -n, --accountnumber | Cloud Account Number                                  | 
|                     |                                                       |
|                     | Type: String                                          |
|                     |                                                       |
|                     | Default: None                                         |
|                     |                                                       |
|                     | Required: Yes                                         |
|                     |                                                       |
+---------------------+-------------------------------------------------------+
| -a, --accesskey     | Cloud Account Access Key                              | 
|                     |                                                       |
|                     | Type: String                                          |
|                     |                                                       |
|                     | Default: None                                         |
|                     |                                                       |
|                     | Required: Yes                                         |
|                     |                                                       |
+---------------------+-------------------------------------------------------+
| -s, --secretkey     | Cloud Account Secret Key                              | 
|                     |                                                       |
|                     | Type: String                                          |
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

   dcm-assign-cloud -c 1 -i 200 -n 1234ABCD -a DEF012 -s SEK567

Related Topics
~~~~~~~~~~~~~~

:ref:`List Clouds <dcm_list_clouds>`

:ref:`List Accounts <dcm_list_accounts>`
