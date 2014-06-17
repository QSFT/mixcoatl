.. raw:: latex
  
      \newpage

.. _dcm_put:

dcm-put
-------

``dcm-put`` implements a generic PUT to the DCM API. PUT calls can create a new
object or update an existing one.

PUT requests are idempotent.

Description
~~~~~~~~~~~

``dcm-put`` is provided to allow for making a PUT to the DCM API.

Syntax
~~~~~~

.. code-block:: bash

   usage: dcm-put [-h] (--xml XML | --json JSON) basepath

   positional arguments:
     basepath     base path
   
   optional arguments:
     -h, --help   show this help message and exit
     --xml XML
     --json JSON

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
| --xml              | Pass XML payload to put command.                       | 
|                    |                                                        |
|                    | Type: File                                             |
|                    |                                                        |
|                    | Default: None                                          |
|                    |                                                        |
|                    | Required: Yes (if using XML)                           |
|                    |                                                        |
|                    | Example: --xml update.xml                              |
+--------------------+--------------------------------------------------------+
| --json             | Pass JSON payload to put command.                      | 
|                    |                                                        |
|                    | Type: File                                             |
|                    |                                                        |
|                    | Default: None                                          |
|                    |                                                        |
|                    | Required: Yes (if using JSON)                          |
|                    |                                                        |
|                    | Example: --json update.json                            |
+--------------------+--------------------------------------------------------+

Output
~~~~~~

True, if success.

Examples
~~~~~~~~

Example 1
^^^^^^^^^

An update to rename a server. :download:`click here <./files/test_put.json>` to view the contents of the JSON payload.

.. code-block:: bash

   dcm-put infrastructure/Server/5090 --json test_put.json

Output

.. code-block:: bash

   True

Related Topics
~~~~~~~~~~~~~~

:ref:`DCM GET <dcm_get>`

:ref:`DCM POST <dcm_post>`

