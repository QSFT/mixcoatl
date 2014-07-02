.. raw:: latex
  
      \newpage

.. _dcm_describe_deployment:

dcm-describe-deployment
-----------------------

Describe a deployment.

Description
~~~~~~~~~~~

Returns a description of a deployment.

Syntax
~~~~~~

.. code-block:: bash

   usage: dcm-describe-deployment [-h] [--verbose] deploymentid

   positional arguments:
     deploymentid   Deployment ID

   optional arguments:
     -h, --help     show this help message and exit
     --verbose, -v  Produce verbose output

Options
~~~~~~~

+--------------------+--------------------------------------------------------------+
| Option             | Description                                                  |
+====================+==============================================================+
| -v, --verbose      | Print out verbose information while desribing a deployment.  |
+--------------------+--------------------------------------------------------------+

Common Options
~~~~~~~~~~~~~~

Deprecated Options
^^^^^^^^^^^^^^^^^^

None

Output
~~~~~~

The return value from this command is a description of a deployment.

Examples
~~~~~~~~

Example 1
^^^^^^^^^

.. code-block:: bash

   dcm-describe-deployment 408
   
Output
%%%%%%

.. code-block:: bash

   +--------------------+-------------------------------+
   | Field              | Attribute                     |
   +--------------------+-------------------------------+
   | Deployment ID      | 408                           |
   | Name               | Web Server                    |
   | Type               | DEDICATED                     |
   | Region             | us-east-1 (us-east-1)         |
   | Budget ID          | 300                           |
   | Owning User Name   | Kang, Sean                    |
   | Owning User Email  | sean.kang@enstratius.com      |
   | Owning Group Name  | Admin                         |
   | Creation Timestamp | 2013-12-17T21:41:21.549+0000  |
   | Description        | Test Web Server               |
   | Status             | STOPPED                       |
   +--------------------+-------------------------------+
