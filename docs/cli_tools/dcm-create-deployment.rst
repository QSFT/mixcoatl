.. raw:: latex
  
      \newpage

.. _dcm_create_deployment:

dcm-create-deployment
---------------------

Creates a deployment.

Description
~~~~~~~~~~~

Creates a deployment and returns Job ID.

Syntax
~~~~~~

.. code-block:: bash

   usage: dcm-create-deployment [-h] [--name NAME] [--description DESCRIPTION]
                                [--region REGION] [--budgetid BUDGETID] [-i FILE]
                                [--verbose]
   optional arguments:
     -h, --help            show this help message and exit
     --name NAME, -n NAME  The name of the deployment.
     --description DESCRIPTION, -d DESCRIPTION
                           The description of the deployment.
     --region REGION, -r REGION
                           The default region of the deployment.
     --budgetid BUDGETID, -b BUDGETID
                           The region of the deployment.
     -i FILE               Input file for creating a deployment
     --verbose, -v         Print out verbose information about the deployment creation.

Options
~~~~~~~

+--------------------+--------------------------------------------------------------+
| Option             | Description                                                  |
+====================+==============================================================+
| -n, --name         | The name of the deployment.                                  |
|                    |                                                              |
|                    | Type: String                                                 |
|                    |                                                              |
|                    | Default: None                                                |
|                    |                                                              |
|                    | Required: Yes                                                |
|                    |                                                              |
|                    | Example: webapp-deployment-1                                 |
+--------------------+--------------------------------------------------------------+
| -d, --description  | The description of the deployment.                           |
|                    |                                                              |
|                    | Type: String                                                 |
|                    |                                                              |
|                    | Default: None                                                |
|                    |                                                              |
|                    | Required: Yes                                                |
|                    |                                                              |
|                    | Example: Web Application Deployment                          |
+--------------------+--------------------------------------------------------------+
| -r, --region       | The default region of the deployment.                        |
|                    |                                                              |
|                    | Type: Integer                                                |
|                    |                                                              |
|                    | Default: None                                                |
|                    |                                                              |
|                    | Required: Yes                                                |
|                    |                                                              |
|                    | Example: 302                                                 |
+--------------------+--------------------------------------------------------------+
| -b, --budgetid     | Budget ID of the deployment.                                 |
|                    |                                                              |
|                    | Type: Integer                                                |
|                    |                                                              |
|                    | Default: None                                                |
|                    |                                                              |
|                    | Required: Yes                                                |
|                    |                                                              |
|                    | Example: 300                                                 |
+--------------------+--------------------------------------------------------------+
| -i                 | Input file for creating deployment.                          |
|                    |                                                              |
|                    | Type: String                                                 |
|                    |                                                              |
|                    | Default: None                                                |
|                    |                                                              |
|                    | Required: No                                                 |
+--------------------+--------------------------------------------------------------+
| -v, --verbose      | Print out verbose information while creating deployment.     |
+--------------------+--------------------------------------------------------------+

Common Options
~~~~~~~~~~~~~~

Deprecated Options
^^^^^^^^^^^^^^^^^^

None

Output
~~~~~~

The return value from this command is Job ID of creating deployment.

Examples
~~~~~~~~

Example 1
^^^^^^^^^

.. code-block:: bash

   dcm-create-deployment -n 'webapp-deployment-1' -r 302 -b 300 -d 'Web Application Deployment'
   
Output
%%%%%%

.. code-block:: bash

   4852
