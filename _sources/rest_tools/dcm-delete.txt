.. raw:: latex

      \newpage

.. _dcm_delete:

dcm-delete
----------

``dcm-delete`` implements a generic DELETE to the DCM API. DELETE calls destroy
objects.

Description
~~~~~~~~~~~

``dcm-delete`` is provided to allow for making a DELETE to the DCM API.

Syntax
~~~~~~

.. code-block:: bash

   usage: dcm-delete [-h] basepath

   positional arguments:
     basepath     base path

   optional arguments:
     -h, --help   show this help message and exit

Options
~~~~~~~

+--------------------+--------------------------------------------------------+
| Option             | Description                                            |
+====================+========================================================+
| <base path>        | Positional parameter                                   |
|                    |                                                        |
|                    | Type: String                                           |
|                    |                                                        |
|                    | Default: None                                          |
|                    |                                                        |
|                    | Required: Yes                                          |
|                    |                                                        |
|                    | Example: infrastructure/Server/5090                    |
+--------------------+--------------------------------------------------------+

Output
~~~~~~

True, if success.

Examples
~~~~~~~~

Example 1
^^^^^^^^^

A delete to terminate a server.

.. code-block:: bash

   dcm-delete infrastructure/Server/303

Outdelete

.. code-block:: bash

   True

Related Topics
~~~~~~~~~~~~~~

:ref:`DCM GET <dcm_get>`

:ref:`DCM POST <dcm_post>`

:ref:`DCM PUT <dcm_put>`
