.. raw:: latex
  
      \newpage

.. _dcm_get:

dcm-get
-------

``mixcoatl`` ships with a small utility for querying arbitrary objects via
the DCM API called ``dcm-get``. It's very minimal and only dumps the JSON
results of your query:

example:

.. code-block:: bash

        dcm-get admin/Job

.. code-block:: json

        {
          "jobs": []
        }

It can also accept query parameters in the form of a python ``dictionary`` (the
same format the ``requests`` library uses:

.. code-block:: bash

        dcm-get geography/DataCenter "{'regionId':19344}"

.. code-block:: json

        {
          "dataCenters": [
            {
              "dataCenterId": 64351, 
              "description": "us-west-2a", 
              "name": "us-west-2a", 
              "providerId": "us-west-2a", 
              "region": {
                "cloud": {
                  "cloudId": 1
                }, 
                "customer": {
                  "customerId": 14334
                }, 
                "description": "AWS Western United States (2)", 
                "jurisdiction": "US", 
                "name": "Oregon (us-west-2)", 
                "providerId": "us-west-2", 
                "regionId": 19344, 
                "status": "ACTIVE"
              }, 
              "status": "ACTIVE"
            }
          ]
        }
