.. raw:: latex
  
      \newpage

.. _dcm_list_clouds:

dcm-list-clouds
---------------

List clouds.

Description
~~~~~~~~~~~

Returns a list of clouds in DCM database.

Syntax
~~~~~~

.. code-block:: bash

   usage: dcm-list-clouds [-h] [--verbose]

   optional arguments:
     -h, --help     show this help message and exit
     --verbose, -v  Produce verbose output

Options
~~~~~~~

+--------------------+--------------------------------------------------------------+
| Option             | Description                                                  |
+====================+==============================================================+
| -v, --verbose      | Print out verbose information while listing clouds.          |
+--------------------+--------------------------------------------------------------+

Common Options
~~~~~~~~~~~~~~

Deprecated Options
^^^^^^^^^^^^^^^^^^

None

Output
~~~~~~

The return value from this command is a list of clouds in DCM's database.

Examples
~~~~~~~~

Example 1
^^^^^^^^^

.. code-block:: bash

   dcm-list-clouds

Output
%%%%%%

.. code-block:: bash

   +----------+----------------------------+--------------------------------------------------+-------------------------------------------------------------------+----------+
   | Cloud ID |         Cloud Name         |                     Delegate                     |                              Endpoint                             |  Status  |
   +----------+----------------------------+--------------------------------------------------+-------------------------------------------------------------------+----------+
   |    1     |    Amazon Web Services     |          org.dasein.cloud.aws.AWSCloud           |                https://ec2.us-east-1.amazonaws.com                |  ACTIVE  |
   |    45    |           Azure            |           org.dasein.cloud.azure.Azure           |                https://management.core.windows.net/               |  ACTIVE  |
   |   1011   |        CloudCentral        |       org.dasein.cloud.cloudstack.CSCloud        |        http://cloudplatform.cloudcentral.com.au/client/api        |  ACTIVE  |
   |    37    |    CloudSigma Las Vegas    |      org.dasein.cloud.cloudsigma.CloudSigma      |                https://lvs.cloudsigma.com/api/2.0/                |  ACTIVE  |
   |   9110   |       Datapipe Cloud       |       org.dasein.cloud.cloudstack.CSCloud        |             https://cloud.datapipe.com/api/compute/v1/            |  ACTIVE  |
   |    9     |           Google           |          org.dasein.cloud.aws.AWSCloud           |              https://commondatastorage.googleapis.com             |  ACTIVE  |
   |    28    |          HP Cloud          | org.dasein.cloud.openstack.nova.os.NovaOpenStack |     https://region-a.geo-1.identity.hpcloudsvc.com:35357/v2.0     |  ACTIVE  |
   |   9000   | IBM SmartCloud Enterprise  |           org.dasein.cloud.ibm.sce.SCE           | https://www-147.ibm.com/computecloud/enterprise/api/rest/20100331 | INACTIVE |
   |    16    |        Joyent Cloud        |     org.dasein.cloud.joyent.SmartDataCenter      |               https://us-west-1.api.joyentcloud.com               |  ACTIVE  |
   +----------+----------------------------+--------------------------------------------------+-------------------------------------------------------------------+----------+
