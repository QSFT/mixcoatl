.. raw:: latex
  
      \newpage

.. _dcm_post:

dcm-post
--------

``dcm-post`` implements a generic POST to the DCM API. POST calls can create a new
object or update an existing one.

Description
~~~~~~~~~~~

``dcm-post`` is provided to allow for making a POST to the DCM API.

Syntax
~~~~~~

.. code-block:: bash

   usage: dcm-post [-h] (--xml XML | --json JSON) basepath

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
| --xml              | Pass XML payload to post command.                      |
|                    |                                                        |
|                    | Type: File                                             |
|                    |                                                        |
|                    | Default: None                                          |
|                    |                                                        |
|                    | Required: Yes (if using XML)                           |
|                    |                                                        |
|                    | Example: --xml update.xml                              |
+--------------------+--------------------------------------------------------+
| --json             | Pass JSON payload to post command.                     |
|                    |                                                        |
|                    | Type: File                                             |
|                    |                                                        |
|                    | Default: None                                          |
|                    |                                                        |
|                    | Required: Yes (if using JSON)                          |
|                    |                                                        |
|                    | Example: --json update.json                            |
+--------------------+--------------------------------------------------------+

Example 1
^^^^^^^^^

A call to create a volume. :download:`click here <./files/create_volume.json>` to view the contents of the JSON
payload.

.. code-block:: bash

   dcm-post --json create_volume infrastructure/Volume

Output

.. code-block:: bash

   {u'jobs': [{u'status': u'RUNNING', u'jobId': 300}]}

Related Topics
~~~~~~~~~~~~~~

:ref:`DCM GET <dcm_get>`

:ref:`DCM POST <dcm_put>`
