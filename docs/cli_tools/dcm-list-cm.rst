.. raw:: latex
  
      \newpage

.. _dcm_list_cm:

dcm-list-cm
-----------

Lists configuration management accounts.

Description
~~~~~~~~~~~

Returns a list of configuration management accounts.

Syntax
~~~~~~

.. program-output:: dcm-list-cm -h

Options
~~~~~~~

+--------------------+--------------------------------------------------------------+
| Option             | Description                                                  |
+====================+==============================================================+
| -v, --verbose      | Print out verbose information while listing cm accounts.     |
+--------------------+--------------------------------------------------------------+

Common Options
~~~~~~~~~~~~~~

Deprecated Options
~~~~~~~~~~~~~~~~~~

None

Output
~~~~~~

The return value from this command is a list of configuration management accounts.

Examples
~~~~~~~~

Example 1
^^^^^^^^^

.. code-block:: bash

   dcm-list-cm --all

Output
%%%%%%

.. code-block:: bash

   +-----+------+------------------+---------------------------------------+----------+
   |  ID | Type |   Description    |                Endpoint               |  Status  |
   +-----+------+------------------+---------------------------------------+----------+
   |  1  | Chef | Demo Chef server | https://chef.example.com:443          |  ACTIVE  |
   +-----+------+------------------+---------------------------------------+----------+
