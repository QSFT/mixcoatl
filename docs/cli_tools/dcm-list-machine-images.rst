.. raw:: latex
  
      \newpage

.. _dcm_list_machine_images:

dcm-list-machine-images
-----------------------

List machine images.

Description
~~~~~~~~~~~

Returns a list of machine images.

Syntax
~~~~~~

.. program-output:: dcm-list-machine-images -h

Options
~~~~~~~

+--------------------+--------------------------------------------------------------+
| Option             | Description                                                  |
+====================+==============================================================+
| -r, --regionid     | Region ID.                                                   |
|                    |                                                              |
|                    | Type: Integer                                                |
|                    |                                                              |
|                    | Default: None                                                |
|                    |                                                              |
|                    | Required: Yes (if regionpid is not specified)                |
|                    |                                                              |
|                    | Example: 201                                                 |
+--------------------+--------------------------------------------------------------+
| -R, --regionpid    | Provider region ID.                                          |
|                    |                                                              |
|                    | Type: String                                                 |
|                    |                                                              |
|                    | Default: None                                                |
|                    |                                                              |
|                    | Required: Yes (if regionid is not specified)                 |
|                    |                                                              |
|                    | Example: us-east-1                                           |
+--------------------+--------------------------------------------------------------+
| -e, --registered   | Returns only images with agent installed.                    |
|                    |                                                              |
|                    | Default: None                                                |
|                    |                                                              |
|                    | Required: No                                                 |
+--------------------+--------------------------------------------------------------+
| -v, --verbose      | Print out verbose information while listing machine images.  |
+--------------------+--------------------------------------------------------------+

Common Options
~~~~~~~~~~~~~~

Deprecated Options
^^^^^^^^^^^^^^^^^^

None

Output
~~~~~~

The return value from this command is a list of machine images.

Examples
~~~~~~~~

Example 1
^^^^^^^^^

.. code-block:: bash

   dcm-list-machine-images -r 202
   
Output
%%%%%%

.. code-block:: bash

   +-----+---------------+-----------------------------------------+---------+------+-------+--------+
   |  ID |  Provider ID  | Name                                    |    OS   | Arch | Agent | Status |
   +-----+---------------+-----------------------------------------+---------+------+-------+--------+
   | 200 |  ami-58a42e30 | ubuntu/images/ebs/ubuntu-precise-12.04  |  UBUNTU | I64  |  None | ACTIVE |
   | 203 |  ami-2ca259b1 | TestImage                               |  RHEL   | I64  |   17  | ACTIVE |
   +-----+---------------+-----------------------------------------+---------+------+-------+--------+
