.. raw:: latex
  
      \newpage

.. _dcm_create_user:

dcm-create-user
---------------

Create a DCM user.

Description
~~~~~~~~~~~

Creates a DCM user in a given account. Requires permission to create users.

Syntax
~~~~~~

.. program-output:: dcm-create-user -h

Options
~~~~~~~

+--------------------+-------------------------------------------------------+
| Option             | Description                                           |
+====================+=======================================================+
| account_id, -a     | The ID of the account to which the user will be added |
|                    |                                                       |
|                    | Type: Integer                                         |
|                    |                                                       |
|                    | Default: None                                         |
|                    |                                                       |
|                    | Required: Yes                                         |
|                    |                                                       |
|                    | Example: 818                                          |
+--------------------+-------------------------------------------------------+
| first_name, -f     | The first name of the user                            |
|                    |                                                       |
|                    | Type: String                                          |
|                    |                                                       |
|                    | Default: None                                         |
|                    |                                                       |
|                    | Required: Yes                                         |
|                    |                                                       |
|                    | Example: Monty                                        |
+--------------------+-------------------------------------------------------+
| last_name, -l      | The last name of the user                             |
|                    |                                                       |
|                    | Type: String                                          |
|                    |                                                       |
|                    | Default: None                                         |
|                    |                                                       |
|                    | Required: Yes                                         |
|                    |                                                       |
|                    | Example: Python                                       |
+--------------------+-------------------------------------------------------+
| email_address, -e  | The email address of the user                         |
|                    |                                                       |
|                    | Type: String                                          |
|                    |                                                       |
|                    | Default: None                                         |
|                    |                                                       |
|                    | Required: Yes                                         |
|                    |                                                       |
|                    | Example: monty_python@software.dell.com               |
+--------------------+-------------------------------------------------------+
| group              | The group of which the user will be a part            |
|                    |                                                       |
|                    | Type: Integer                                         |
|                    |                                                       |
|                    | Default: None                                         |
|                    |                                                       |
|                    | Required: Yes                                         |
|                    |                                                       |
|                    | Example: 816                                          |
+--------------------+-------------------------------------------------------+
| email_address, -e  | The budget code to which the user will belong         |
|                    |                                                       |
|                    | Type: Integer                                         |
|                    |                                                       |
|                    | Default: None                                         |
|                    |                                                       |
|                    | Required: Yes                                         |
|                    |                                                       |
|                    | Example: 819                                          |
+--------------------+-------------------------------------------------------+
| password, -p       | The password for the user                             |
|                    |                                                       |
|                    | Type: String                                          |
|                    |                                                       |
|                    | Default: None                                         |
|                    |                                                       |
|                    | Required: Yes                                         |
|                    |                                                       |
|                    | Example: iHLIX0GV5x0QIkhH                             |
+--------------------+-------------------------------------------------------+
| verbose, -v        | Print out verbose information about the user creation |
+--------------------+-------------------------------------------------------+

Common Options
~~~~~~~~~~~~~~

Deprecated Options
^^^^^^^^^^^^^^^^^^

None.

Output
~~~~~~

The return value from this command will be the user ID of the created user.

Examples
~~~~~~~~

Example 1
^^^^^^^^^

.. code-block:: bash

   dcm-create-user -a 818 -f Python -l Monty -e monty_python@software.dell.com -g 816 -b 819 -p SMYY05ef2OCDITcG

   921

Related Topics
~~~~~~~~~~~~~~

:ref:`List Accounts <dcm_list_accounts>`

:ref:`List Groups <dcm_list_groups>`

:ref:`Create Group <dcm_create_group>`

:ref:`List Roles <dcm_list_roles>`

:ref:`Create Role <dcm_create_role>`

:ref:`List Users <dcm_list_users>`
