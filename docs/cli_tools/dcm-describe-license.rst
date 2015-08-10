.. raw:: latex
  
      \newpage

.. _dcm_describe_license:

dcm-describe-license
--------------------


Description
~~~~~~~~~~~

Returns licensing information for the present DCM instance. This information is only useful in the case of on-premsses
deployments of DCM.

Syntax
~~~~~~

.. code-block:: bash

    usage: dcm-describe-license [-h] [--json | --xml | --csv]

    optional arguments:
    -h, --help  show this help message and exit
    --json      print API response in JSON format.
    --xml       print API response in XML format.
    --csv       print API response in CSV format.


Output
%%%%%%

.. code-block:: bash

    Licensee: Acme Corp
    Days Until Expiration: 365
    Expiration Date: 2016-06-18T16:07:21.311+0000
    Server Limit: 200
    License Valid: True