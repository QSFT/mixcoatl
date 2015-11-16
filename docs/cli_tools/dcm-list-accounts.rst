.. raw:: latex
  
      \newpage

.. _dcm_list_accounts:

dcm-list-accounts
-----------------

List DCM accounts.

Description
~~~~~~~~~~~

Returns a list of DCM accounts. The list returned is subject to the scope of the API key.

Syntax
~~~~~~

.. program-output:: dcm-list-accounts -h

Options
~~~~~~~

+--------------------+------------------------------------------------------------+
| Option             | Description                                                |
+====================+============================================================+
| -v, --verbose      | Print out verbose information while listing accounts       |
+--------------------+------------------------------------------------------------+

Common Options
~~~~~~~~~~~~~~

Deprecated Options
^^^^^^^^^^^^^^^^^^

None

Output
~~~~~~

The return value from this command is a list of DCM accounts

Examples
~~~~~~~~

Example 1
^^^^^^^^^

.. code-block:: bash

   dcm-list-accounts

Output
%%%%%%

.. code-block:: bash

   +------------+--------------+----------------+--------+
   | Account ID | Account Name | Default Budget | Status |
   +------------+--------------+----------------+--------+
   |    200     |     aws      |      200       | ACTIVE |
   +------------+--------------+----------------+--------+

Example 2
^^^^^^^^^

.. code-block:: bash

   dcm-list-accounts -v

Output
%%%%%%

.. code-block:: json

   {'account_id': 200,
    'alert_configuration': {'alert_interval_in_minutes': 5,
                            'allow_individual_email_alerts': True,
                            'allow_individual_sms_alerts': True,
                            'global_email_threshold': 11,
                            'global_sms_threshold': 11,
                            'stop_alerts_after_minutes': 60},
    'billing_system_id': '200',
    'cloud_subscription': {'account_number': '521320785623',
                           'assignable_private_ip_addresses': False,
                           'assignable_public_ip_addresses': True,
                           'cloud_id': 1,
                           'cloud_subscription_id': 1,
                           'has_public_image_library': True,
                           'ip_address_forwarding': False,
                           'load_balancer_data_center_limited': True,
                           'load_balancer_ip_address_assigned': True,
                           'requestable_private_ip_addresses': False,
                           'requestable_public_ip_addresses': True,
                           'storage_account_number': '5213-2078-5623',
                           'subscribed_auto_scaling': True,
                           'subscribed_blob_store': True,
                           'subscribed_cdn': True,
                           'subscribed_dns': True,
                           'subscribed_email': False,
                           'subscribed_firewall': True,
                           'subscribed_image': True,
                           'subscribed_ip_address': True,
                           'subscribed_key_value': True,
                           'subscribed_load_balancer': True,
                           'subscribed_message_queue': False,
                           'subscribed_push_notifications': True,
                           'subscribed_rdbms': True,
                           'subscribed_server': True,
                           'subscribed_snapshot': True,
                           'subscribed_vlan': True,
                           'subscribed_volume': True,
                           'subscribed_vpn': False,
                           'supports_custom_images': True,
                           'supports_ha_rdbms': True,
                           'supports_hypervisor_analytics': True,
                           'supports_non_ha_rdbms': True,
                           'supports_private_image_sharing': True,
                           'supports_private_snapshot_sharing': True,
                           'supports_public_image_sharing': True,
                           'supports_public_snapshot_sharing': True,
                           'supports_rdbms_firewalls': True,
                           'supports_rdbms_maintenance_windows': True,
                           'supports_rdbms_snapshots': True,
                           'supports_ssh_key_bootstrapping': True},
    'configured': True,
    'current_job': None,
    'customer': {'accounting_currency': 'USD',
                 'automated_exchange_rates': True,
                 'business_name': 'Company Inc.',
                 'created': '2014-05-21T16:43:24.110+0000',
                 'created_timestamp': '2014-05-21T16:43:24.110+0000',
                 'customer_id': 200,
                 'status': 'ACTIVE',
                 'time_zone': 'America/Chicago',
                 'web_site': 'http://www.enstratius.com'},
    'default_budget': 200,
    'dns_automation': None,
    'last_error': None,
    'last_request': '<Response [200]>',
    'name': 'aws',
    'owner': None,
    'path': 'admin/Account/200',
    'plan_id': 2,
    'provisioned': True,
    'request_details': 'extended',
    'status': 'ACTIVE',
    'subscribed': True}
