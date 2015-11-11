.. raw:: latex
  
      \newpage

.. _dcm_describe_machine_image:

dcm-describe-machine-image
--------------------------

Describe a machine image.

Description
~~~~~~~~~~~

Returns a short summary about a machine image.

Syntax
~~~~~~

.. program-output:: dcm-describe-machine-image -h

Options
~~~~~~~

+--------------------+----------------------------------------------------------------+
| Option             | Description                                                    |
+====================+================================================================+
| -v, --verbose      | Print out verbose information while describing a machine image |
+--------------------+----------------------------------------------------------------+

Common Options
~~~~~~~~~~~~~~

Deprecated Options
^^^^^^^^^^^^^^^^^^

None

Output
~~~~~~

The output of this command is a short summary of information about a machine image given a machine image ID.

Examples
~~~~~~~~

Example 1
^^^^^^^^^

.. code-block:: bash

   dcm-describe-machine-image 601

Output
%%%%%%

.. code-block:: bash

   +------------------+--------------+
   | Field            | Attribute    |
   +------------------+--------------+
   | Machine Image ID | 601          |
   | Name             | Chef-server  |
   | Provider ID      | ami-13596457 |
   | Platform         | UBUNTU       |
   | Architecture     | I64          |
   | Region ID        | 301          |
   | Budget ID        | 300          |
   | Owning User ID   | 410          |
   | Owning Group ID  | None         |
   | Description      | Chef-server  |
   | Agent Version    | 17           |
   | Status           | ACTIVE       |
   +------------------+--------------+
