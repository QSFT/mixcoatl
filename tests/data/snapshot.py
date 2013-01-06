all_items = '''
{
    "snapshots": [
        {
            "region": {
                "status": "ACTIVE",
                "description": "AWS Southeast Asia/Pacific (2)",
                "name": "Sydney (ap-southeast-2)",
                "providerId": "ap-southeast-2",
                "cloud": {
                    "cloudId": 1
                },
                "jurisdiction": "AU",
                "customer": {
                    "customerId": 11111
                },
                "regionId": 19556
            },
            "snapshotId": 23237460,
            "budget": 10287,
            "createdTimestamp": "2012-11-20T01:31:53.000+0000",
            "status": "ACTIVE",
            "removable": true,
            "label": null,
            "available": true,
            "customer": {
                "businessName": "CSE",
                "customerId": 11111,
                "createdTimestamp": "2012-11-07T16:38:26.885+0000",
                "status": "ACTIVE",
                "accountingCurrency": "USD",
                "created": "2012-11-07T16:38:26.885+0000",
                "timeZone": "UTC",
                "automatedExchangeRates": true
            },
            "encrypted": false,
            "description": "snap-b0810e80",
            "sharable": true,
            "name": "snap-b0810e80",
            "sizeInGb": 8,
            "volume": {
                "region": {
                    "regionId": 19556
                },
                "budget": 10287,
                "volumeId": 209179,
                "status": "INACTIVE",
                "removable": false,
                "sizeString": "8GB",
                "dataCenter": {
                    "dataCenterId": 64716
                },
                "available": false,
                "customer": {
                    "customerId": 11111
                },
                "owningGroups": [
                    {
                        "groupId": 9465
                    }
                ],
                "encrypted": false,
                "description": "vol-9a31cda9",
                "sizeInGb": 8,
                "name": "vol-9a31cda9",
                "providerId": "vol-9a31cda9",
                "cloud": {
                    "cloudId": 1
                },
                "server": {
                    "serverId": 319622
                },
                "creationTimestamp": "1970-01-01T00:00:00.000+0000",
                "owningUser": {
                    "userId": 12345
                },
                "deviceId": "/dev/sda1",
                "owningAccount": {
                    "accountId": 16000
                }
            },
            "providerId": "snap-b0810e80",
            "cloud": {
                "computeDelegate": "org.dasein.cloud.aws.AWSCloud",
                "cloudId": 1,
                "computeX509KeyLabel": "AWS_PRIVATE_KEY",
                "status": "ACTIVE",
                "computeEndpoint": "https://ec2.us-east-1.amazonaws.com,https://ec2.us-west-1.amazonaws.com,https://ec2.eu-west-1.amazonaws.com",
                "privateCloud": false,
                "computeSecretKeyLabel": "AWS_SECRET_ACCESS_KEY",
                "computeX509CertLabel": "AWS_CERTIFICATE",
                "computeAccountNumberLabel": "AWS_ACCOUNT_NUMBER",
                "documentationLabel": null,
                "name": "Amazon Web Services",
                "cloudProviderName": "Amazon",
                "computeAccessKeyLabel": "AWS_ACCESS_KEY",
                "cloudProviderConsoleURL": "http://aws.amazon.com",
                "cloudProviderLogoURL": "/clouds/aws.gif"
            },
            "owningAccount": {
                "accountId": 16000,
                "cloudSubscriptionId": {
                    "cloudId": 1,
                    "accountNumber": "825279278023",
                    "cloudSubscriptionId": 12620,
                    "storageAccountNumber": null
                },
                "status": "ACTIVE",
                "configured": true,
                "provisioned": true,
                "planId": 2,
                "subscribed": true,
                "billingSystemId": "16000",
                "customer": {
                    "customerId": 11111
                },
                "defaultBudget": 10287,
                "name": "CSE",
                "owner": {
                    "userId": 12346
                },
                "alertConfiguration": {
                    "allowIndividualSmsAlerts": true,
                    "stopAlertsAfterMinutes": 60,
                    "globalSmsThreshold": 11,
                    "globalEmailThreshold": 11,
                    "allowIndividualEmailAlerts": true,
                    "alertIntervalInMinutes": 5
                }
            }
        },
        {
            "region": {
                "status": "ACTIVE",
                "description": "AWS Southeast Asia/Pacific (2)",
                "name": "Sydney (ap-southeast-2)",
                "providerId": "ap-southeast-2",
                "cloud": {
                    "cloudId": 1
                },
                "jurisdiction": "AU",
                "customer": {
                    "customerId": 11111
                },
                "regionId": 19556
            },
            "snapshotId": 23294582,
            "budget": 10287,
            "createdTimestamp": "2012-11-21T20:47:36.000+0000",
            "status": "ACTIVE",
            "removable": true,
            "label": null,
            "available": true,
            "customer": {
                "businessName": "CSE",
                "customerId": 11111,
                "createdTimestamp": "2012-11-07T16:38:26.885+0000",
                "status": "ACTIVE",
                "accountingCurrency": "USD",
                "created": "2012-11-07T16:38:26.885+0000",
                "timeZone": "UTC",
                "automatedExchangeRates": true
            },
            "encrypted": false,
            "description": "snap-2044cb10",
            "sharable": true,
            "name": "snap-2044cb10",
            "sizeInGb": 8,
            "volume": {
                "region": {
                    "regionId": 19556
                },
                "budget": 10287,
                "volumeId": 209824,
                "status": "INACTIVE",
                "removable": false,
                "sizeString": "8GB",
                "dataCenter": {
                    "dataCenterId": 64716
                },
                "available": false,
                "customer": {
                    "customerId": 11111
                },
                "encrypted": false,
                "description": "vol-8e7688bd",
                "name": "vol-8e7688bd",
                "sizeInGb": 8,
                "providerId": "vol-8e7688bd",
                "cloud": {
                    "cloudId": 1
                },
                "server": {
                    "serverId": 321097
                },
                "creationTimestamp": "1970-01-01T00:00:00.000+0000",
                "deviceId": "/dev/sda1",
                "owningAccount": {
                    "accountId": 16000
                }
            },
            "providerId": "snap-2044cb10",
            "cloud": {
                "computeDelegate": "org.dasein.cloud.aws.AWSCloud",
                "cloudId": 1,
                "computeX509KeyLabel": "AWS_PRIVATE_KEY",
                "status": "ACTIVE",
                "computeEndpoint": "https://ec2.us-east-1.amazonaws.com,https://ec2.us-west-1.amazonaws.com,https://ec2.eu-west-1.amazonaws.com",
                "privateCloud": false,
                "computeSecretKeyLabel": "AWS_SECRET_ACCESS_KEY",
                "computeX509CertLabel": "AWS_CERTIFICATE",
                "computeAccountNumberLabel": "AWS_ACCOUNT_NUMBER",
                "documentationLabel": null,
                "name": "Amazon Web Services",
                "cloudProviderName": "Amazon",
                "computeAccessKeyLabel": "AWS_ACCESS_KEY",
                "cloudProviderConsoleURL": "http://aws.amazon.com",
                "cloudProviderLogoURL": "/clouds/aws.gif"
            },
            "owningAccount": {
                "accountId": 16000,
                "cloudSubscriptionId": {
                    "cloudId": 1,
                    "accountNumber": "825279278023",
                    "cloudSubscriptionId": 12620,
                    "storageAccountNumber": null
                },
                "status": "ACTIVE",
                "configured": true,
                "provisioned": true,
                "planId": 2,
                "subscribed": true,
                "billingSystemId": "16000",
                "customer": {
                    "customerId": 11111
                },
                "defaultBudget": 10287,
                "name": "CSE",
                "owner": {
                    "userId": 12346
                },
                "alertConfiguration": {
                    "allowIndividualSmsAlerts": true,
                    "stopAlertsAfterMinutes": 60,
                    "globalSmsThreshold": 11,
                    "globalEmailThreshold": 11,
                    "allowIndividualEmailAlerts": true,
                    "alertIntervalInMinutes": 5
                }
            }
        },
        {
            "region": {
                "status": "ACTIVE",
                "description": "AWS Western United States (1)",
                "name": "N. California (us-west-1)",
                "providerId": "us-west-1",
                "cloud": {
                    "cloudId": 1
                },
                "jurisdiction": "US",
                "customer": {
                    "customerId": 11111
                },
                "regionId": 19342
            },
            "snapshotId": 23016074,
            "budget": 10287,
            "createdTimestamp": "2012-11-08T09:26:16.000+0000",
            "status": "ACTIVE",
            "removable": true,
            "label": null,
            "available": true,
            "customer": {
                "businessName": "CSE",
                "customerId": 11111,
                "createdTimestamp": "2012-11-07T16:38:26.885+0000",
                "status": "ACTIVE",
                "accountingCurrency": "USD",
                "created": "2012-11-07T16:38:26.885+0000",
                "timeZone": "UTC",
                "automatedExchangeRates": true
            },
            "encrypted": false,
            "description": "snap-41a1946d",
            "sharable": true,
            "name": "snap-41a1946d",
            "sizeInGb": 8,
            "volume": {
                "region": {
                    "regionId": 19342
                },
                "budget": 10287,
                "volumeId": 205576,
                "status": "INACTIVE",
                "removable": false,
                "sizeString": "8GB",
                "dataCenter": {
                    "dataCenterId": 64346
                },
                "available": false,
                "customer": {
                    "customerId": 11111
                },
                "owningGroups": [
                    {
                        "groupId": 9465
                    }
                ],
                "encrypted": false,
                "description": "vol-9d7875b3",
                "sizeInGb": 8,
                "name": "vol-9d7875b3",
                "providerId": "vol-9d7875b3",
                "cloud": {
                    "cloudId": 1
                },
                "server": {
                    "serverId": 311942
                },
                "creationTimestamp": "1970-01-01T00:00:00.000+0000",
                "owningUser": {
                    "userId": 54321
                },
                "deviceId": "/dev/sda1",
                "owningAccount": {
                    "accountId": 16000
                }
            },
            "providerId": "snap-41a1946d",
            "cloud": {
                "computeDelegate": "org.dasein.cloud.aws.AWSCloud",
                "cloudId": 1,
                "computeX509KeyLabel": "AWS_PRIVATE_KEY",
                "status": "ACTIVE",
                "computeEndpoint": "https://ec2.us-east-1.amazonaws.com,https://ec2.us-west-1.amazonaws.com,https://ec2.eu-west-1.amazonaws.com",
                "privateCloud": false,
                "computeSecretKeyLabel": "AWS_SECRET_ACCESS_KEY",
                "computeX509CertLabel": "AWS_CERTIFICATE",
                "computeAccountNumberLabel": "AWS_ACCOUNT_NUMBER",
                "documentationLabel": null,
                "name": "Amazon Web Services",
                "cloudProviderName": "Amazon",
                "computeAccessKeyLabel": "AWS_ACCESS_KEY",
                "cloudProviderConsoleURL": "http://aws.amazon.com",
                "cloudProviderLogoURL": "/clouds/aws.gif"
            },
            "owningAccount": {
                "accountId": 16000,
                "cloudSubscriptionId": {
                    "cloudId": 1,
                    "accountNumber": "825279278023",
                    "cloudSubscriptionId": 12620,
                    "storageAccountNumber": null
                },
                "status": "ACTIVE",
                "configured": true,
                "provisioned": true,
                "planId": 2,
                "subscribed": true,
                "billingSystemId": "16000",
                "customer": {
                    "customerId": 11111
                },
                "defaultBudget": 10287,
                "name": "CSE",
                "owner": {
                    "userId": 12346
                },
                "alertConfiguration": {
                    "allowIndividualSmsAlerts": true,
                    "stopAlertsAfterMinutes": 60,
                    "globalSmsThreshold": 11,
                    "globalEmailThreshold": 11,
                    "allowIndividualEmailAlerts": true,
                    "alertIntervalInMinutes": 5
                }
            }
        },
        {
            "region": {
                "status": "ACTIVE",
                "description": "AWS Western United States (2)",
                "name": "Oregon (us-west-2)",
                "providerId": "us-west-2",
                "cloud": {
                    "cloudId": 1
                },
                "jurisdiction": "US",
                "customer": {
                    "customerId": 11111
                },
                "regionId": 19344
            },
            "snapshotId": 23008962,
            "budget": 10287,
            "createdTimestamp": "2012-11-08T03:52:17.000+0000",
            "status": "ACTIVE",
            "removable": true,
            "label": null,
            "available": true,
            "customer": {
                "businessName": "CSE",
                "customerId": 11111,
                "createdTimestamp": "2012-11-07T16:38:26.885+0000",
                "status": "ACTIVE",
                "accountingCurrency": "USD",
                "created": "2012-11-07T16:38:26.885+0000",
                "timeZone": "UTC",
                "automatedExchangeRates": true
            },
            "encrypted": false,
            "description": "snap-53de4b75",
            "sharable": true,
            "name": "snap-53de4b75",
            "sizeInGb": 8,
            "volume": {
                "region": {
                    "regionId": 19344
                },
                "budget": 10287,
                "volumeId": 205544,
                "status": "INACTIVE",
                "removable": false,
                "sizeString": "8GB",
                "dataCenter": {
                    "dataCenterId": 64351
                },
                "available": false,
                "customer": {
                    "customerId": 11111
                },
                "owningGroups": [
                    {
                        "groupId": 9465
                    }
                ],
                "encrypted": false,
                "description": "vol-43d7de65",
                "sizeInGb": 8,
                "name": "vol-43d7de65",
                "providerId": "vol-43d7de65",
                "cloud": {
                    "cloudId": 1
                },
                "server": {
                    "serverId": 311413
                },
                "creationTimestamp": "1970-01-01T00:00:00.000+0000",
                "owningUser": {
                    "userId": 54321
                },
                "deviceId": "/dev/sda1",
                "owningAccount": {
                    "accountId": 16000
                }
            },
            "providerId": "snap-53de4b75",
            "cloud": {
                "computeDelegate": "org.dasein.cloud.aws.AWSCloud",
                "cloudId": 1,
                "computeX509KeyLabel": "AWS_PRIVATE_KEY",
                "status": "ACTIVE",
                "computeEndpoint": "https://ec2.us-east-1.amazonaws.com,https://ec2.us-west-1.amazonaws.com,https://ec2.eu-west-1.amazonaws.com",
                "privateCloud": false,
                "computeSecretKeyLabel": "AWS_SECRET_ACCESS_KEY",
                "computeX509CertLabel": "AWS_CERTIFICATE",
                "computeAccountNumberLabel": "AWS_ACCOUNT_NUMBER",
                "documentationLabel": null,
                "name": "Amazon Web Services",
                "cloudProviderName": "Amazon",
                "computeAccessKeyLabel": "AWS_ACCESS_KEY",
                "cloudProviderConsoleURL": "http://aws.amazon.com",
                "cloudProviderLogoURL": "/clouds/aws.gif"
            },
            "owningAccount": {
                "accountId": 16000,
                "cloudSubscriptionId": {
                    "cloudId": 1,
                    "accountNumber": "825279278023",
                    "cloudSubscriptionId": 12620,
                    "storageAccountNumber": null
                },
                "status": "ACTIVE",
                "configured": true,
                "provisioned": true,
                "planId": 2,
                "subscribed": true,
                "billingSystemId": "16000",
                "customer": {
                    "customerId": 11111
                },
                "defaultBudget": 10287,
                "name": "CSE",
                "owner": {
                    "userId": 12346
                },
                "alertConfiguration": {
                    "allowIndividualSmsAlerts": true,
                    "stopAlertsAfterMinutes": 60,
                    "globalSmsThreshold": 11,
                    "globalEmailThreshold": 11,
                    "allowIndividualEmailAlerts": true,
                    "alertIntervalInMinutes": 5
                }
            }
        },
        {
            "region": {
                "status": "ACTIVE",
                "description": "AWS Western United States (2)",
                "name": "Oregon (us-west-2)",
                "providerId": "us-west-2",
                "cloud": {
                    "cloudId": 1
                },
                "jurisdiction": "US",
                "customer": {
                    "customerId": 11111
                },
                "regionId": 19344
            },
            "snapshotId": 23023228,
            "budget": 10287,
            "createdTimestamp": "2012-11-08T19:03:59.000+0000",
            "status": "ACTIVE",
            "removable": true,
            "label": null,
            "available": true,
            "customer": {
                "businessName": "CSE",
                "customerId": 11111,
                "createdTimestamp": "2012-11-07T16:38:26.885+0000",
                "status": "ACTIVE",
                "accountingCurrency": "USD",
                "created": "2012-11-07T16:38:26.885+0000",
                "timeZone": "UTC",
                "automatedExchangeRates": true
            },
            "encrypted": false,
            "description": "snap-023aaf24",
            "sharable": true,
            "name": "snap-023aaf24",
            "sizeInGb": 8,
            "volume": {
                "region": {
                    "regionId": 19344
                },
                "budget": 10287,
                "volumeId": 205920,
                "status": "INACTIVE",
                "removable": false,
                "sizeString": "8GB",
                "dataCenter": {
                    "dataCenterId": 64351
                },
                "available": false,
                "customer": {
                    "customerId": 11111
                },
                "encrypted": false,
                "description": "vol-845c57a2",
                "name": "vol-845c57a2",
                "sizeInGb": 8,
                "providerId": "vol-845c57a2",
                "cloud": {
                    "cloudId": 1
                },
                "server": {
                    "serverId": 312352
                },
                "creationTimestamp": "1970-01-01T00:00:00.000+0000",
                "owningUser": {
                    "userId": 16574
                },
                "deviceId": "/dev/sda1",
                "owningAccount": {
                    "accountId": 16000
                }
            },
            "providerId": "snap-023aaf24",
            "cloud": {
                "computeDelegate": "org.dasein.cloud.aws.AWSCloud",
                "cloudId": 1,
                "computeX509KeyLabel": "AWS_PRIVATE_KEY",
                "status": "ACTIVE",
                "computeEndpoint": "https://ec2.us-east-1.amazonaws.com,https://ec2.us-west-1.amazonaws.com,https://ec2.eu-west-1.amazonaws.com",
                "privateCloud": false,
                "computeSecretKeyLabel": "AWS_SECRET_ACCESS_KEY",
                "computeX509CertLabel": "AWS_CERTIFICATE",
                "computeAccountNumberLabel": "AWS_ACCOUNT_NUMBER",
                "documentationLabel": null,
                "name": "Amazon Web Services",
                "cloudProviderName": "Amazon",
                "computeAccessKeyLabel": "AWS_ACCESS_KEY",
                "cloudProviderConsoleURL": "http://aws.amazon.com",
                "cloudProviderLogoURL": "/clouds/aws.gif"
            },
            "owningAccount": {
                "accountId": 16000,
                "cloudSubscriptionId": {
                    "cloudId": 1,
                    "accountNumber": "825279278023",
                    "cloudSubscriptionId": 12620,
                    "storageAccountNumber": null
                },
                "status": "ACTIVE",
                "configured": true,
                "provisioned": true,
                "planId": 2,
                "subscribed": true,
                "billingSystemId": "16000",
                "customer": {
                    "customerId": 11111
                },
                "defaultBudget": 10287,
                "name": "CSE",
                "owner": {
                    "userId": 12346
                },
                "alertConfiguration": {
                    "allowIndividualSmsAlerts": true,
                    "stopAlertsAfterMinutes": 60,
                    "globalSmsThreshold": 11,
                    "globalEmailThreshold": 11,
                    "allowIndividualEmailAlerts": true,
                    "alertIntervalInMinutes": 5
                }
            }
        },
        {
            "region": {
                "status": "ACTIVE",
                "description": "AWS Western United States (2)",
                "name": "Oregon (us-west-2)",
                "providerId": "us-west-2",
                "cloud": {
                    "cloudId": 1
                },
                "jurisdiction": "US",
                "customer": {
                    "customerId": 11111
                },
                "regionId": 19344
            },
            "snapshotId": 23200284,
            "budget": 10287,
            "createdTimestamp": "2012-11-19T01:47:14.000+0000",
            "status": "ACTIVE",
            "removable": true,
            "label": null,
            "available": true,
            "customer": {
                "businessName": "CSE",
                "customerId": 11111,
                "createdTimestamp": "2012-11-07T16:38:26.885+0000",
                "status": "ACTIVE",
                "accountingCurrency": "USD",
                "created": "2012-11-07T16:38:26.885+0000",
                "timeZone": "UTC",
                "automatedExchangeRates": true
            },
            "encrypted": false,
            "description": "snap-9a67fdbc",
            "sharable": true,
            "name": "snap-9a67fdbc",
            "sizeInGb": 8,
            "volume": {
                "region": {
                    "regionId": 19344
                },
                "budget": 10287,
                "volumeId": 208841,
                "status": "INACTIVE",
                "removable": false,
                "sizeString": "8GB",
                "dataCenter": {
                    "dataCenterId": 64352
                },
                "available": false,
                "customer": {
                    "customerId": 11111
                },
                "encrypted": false,
                "description": "vol-dd37d2e4",
                "name": "vol-dd37d2e4",
                "sizeInGb": 8,
                "providerId": "vol-dd37d2e4",
                "cloud": {
                    "cloudId": 1
                },
                "server": {
                    "serverId": 319218
                },
                "creationTimestamp": "1970-01-01T00:00:00.000+0000",
                "deviceId": "/dev/sda1",
                "owningAccount": {
                    "accountId": 16000
                }
            },
            "providerId": "snap-9a67fdbc",
            "cloud": {
                "computeDelegate": "org.dasein.cloud.aws.AWSCloud",
                "cloudId": 1,
                "computeX509KeyLabel": "AWS_PRIVATE_KEY",
                "status": "ACTIVE",
                "computeEndpoint": "https://ec2.us-east-1.amazonaws.com,https://ec2.us-west-1.amazonaws.com,https://ec2.eu-west-1.amazonaws.com",
                "privateCloud": false,
                "computeSecretKeyLabel": "AWS_SECRET_ACCESS_KEY",
                "computeX509CertLabel": "AWS_CERTIFICATE",
                "computeAccountNumberLabel": "AWS_ACCOUNT_NUMBER",
                "documentationLabel": null,
                "name": "Amazon Web Services",
                "cloudProviderName": "Amazon",
                "computeAccessKeyLabel": "AWS_ACCESS_KEY",
                "cloudProviderConsoleURL": "http://aws.amazon.com",
                "cloudProviderLogoURL": "/clouds/aws.gif"
            },
            "owningAccount": {
                "accountId": 16000,
                "cloudSubscriptionId": {
                    "cloudId": 1,
                    "accountNumber": "825279278023",
                    "cloudSubscriptionId": 12620,
                    "storageAccountNumber": null
                },
                "status": "ACTIVE",
                "configured": true,
                "provisioned": true,
                "planId": 2,
                "subscribed": true,
                "billingSystemId": "16000",
                "customer": {
                    "customerId": 11111
                },
                "defaultBudget": 10287,
                "name": "CSE",
                "owner": {
                    "userId": 12346
                },
                "alertConfiguration": {
                    "allowIndividualSmsAlerts": true,
                    "stopAlertsAfterMinutes": 60,
                    "globalSmsThreshold": 11,
                    "globalEmailThreshold": 11,
                    "allowIndividualEmailAlerts": true,
                    "alertIntervalInMinutes": 5
                }
            }
        },
        {
            "region": {
                "status": "ACTIVE",
                "description": "AWS Western United States (2)",
                "name": "Oregon (us-west-2)",
                "providerId": "us-west-2",
                "cloud": {
                    "cloudId": 1
                },
                "jurisdiction": "US",
                "customer": {
                    "customerId": 11111
                },
                "regionId": 19344
            },
            "snapshotId": 23297026,
            "budget": 10287,
            "createdTimestamp": "2012-11-22T00:59:09.000+0000",
            "status": "ACTIVE",
            "removable": true,
            "label": null,
            "available": true,
            "customer": {
                "businessName": "CSE",
                "customerId": 11111,
                "createdTimestamp": "2012-11-07T16:38:26.885+0000",
                "status": "ACTIVE",
                "accountingCurrency": "USD",
                "created": "2012-11-07T16:38:26.885+0000",
                "timeZone": "UTC",
                "automatedExchangeRates": true
            },
            "encrypted": false,
            "description": "snap-b0563096",
            "sharable": true,
            "name": "snap-b0563096",
            "sizeInGb": 8,
            "volume": {
                "region": {
                    "regionId": 19344
                },
                "budget": 10287,
                "volumeId": 208841,
                "status": "INACTIVE",
                "removable": false,
                "sizeString": "8GB",
                "dataCenter": {
                    "dataCenterId": 64352
                },
                "available": false,
                "customer": {
                    "customerId": 11111
                },
                "encrypted": false,
                "description": "vol-dd37d2e4",
                "name": "vol-dd37d2e4",
                "sizeInGb": 8,
                "providerId": "vol-dd37d2e4",
                "cloud": {
                    "cloudId": 1
                },
                "server": {
                    "serverId": 319218
                },
                "creationTimestamp": "1970-01-01T00:00:00.000+0000",
                "deviceId": "/dev/sda1",
                "owningAccount": {
                    "accountId": 16000
                }
            },
            "providerId": "snap-b0563096",
            "cloud": {
                "computeDelegate": "org.dasein.cloud.aws.AWSCloud",
                "cloudId": 1,
                "computeX509KeyLabel": "AWS_PRIVATE_KEY",
                "status": "ACTIVE",
                "computeEndpoint": "https://ec2.us-east-1.amazonaws.com,https://ec2.us-west-1.amazonaws.com,https://ec2.eu-west-1.amazonaws.com",
                "privateCloud": false,
                "computeSecretKeyLabel": "AWS_SECRET_ACCESS_KEY",
                "computeX509CertLabel": "AWS_CERTIFICATE",
                "computeAccountNumberLabel": "AWS_ACCOUNT_NUMBER",
                "documentationLabel": null,
                "name": "Amazon Web Services",
                "cloudProviderName": "Amazon",
                "computeAccessKeyLabel": "AWS_ACCESS_KEY",
                "cloudProviderConsoleURL": "http://aws.amazon.com",
                "cloudProviderLogoURL": "/clouds/aws.gif"
            },
            "owningAccount": {
                "accountId": 16000,
                "cloudSubscriptionId": {
                    "cloudId": 1,
                    "accountNumber": "825279278023",
                    "cloudSubscriptionId": 12620,
                    "storageAccountNumber": null
                },
                "status": "ACTIVE",
                "configured": true,
                "provisioned": true,
                "planId": 2,
                "subscribed": true,
                "billingSystemId": "16000",
                "customer": {
                    "customerId": 11111
                },
                "defaultBudget": 10287,
                "name": "CSE",
                "owner": {
                    "userId": 12346
                },
                "alertConfiguration": {
                    "allowIndividualSmsAlerts": true,
                    "stopAlertsAfterMinutes": 60,
                    "globalSmsThreshold": 11,
                    "globalEmailThreshold": 11,
                    "allowIndividualEmailAlerts": true,
                    "alertIntervalInMinutes": 5
                }
            }
        },
        {
            "region": {
                "status": "ACTIVE",
                "description": "AWS Western United States (2)",
                "name": "Oregon (us-west-2)",
                "providerId": "us-west-2",
                "cloud": {
                    "cloudId": 1
                },
                "jurisdiction": "US",
                "customer": {
                    "customerId": 11111
                },
                "regionId": 19344
            },
            "snapshotId": 23336930,
            "budget": 10287,
            "createdTimestamp": "2012-11-26T23:16:45.000+0000",
            "status": "ACTIVE",
            "removable": true,
            "label": null,
            "available": true,
            "customer": {
                "businessName": "CSE",
                "customerId": 11111,
                "createdTimestamp": "2012-11-07T16:38:26.885+0000",
                "status": "ACTIVE",
                "accountingCurrency": "USD",
                "created": "2012-11-07T16:38:26.885+0000",
                "timeZone": "UTC",
                "automatedExchangeRates": true
            },
            "owningGroups": [
                {
                    "groupId": 9465,
                    "status": "ACTIVE",
                    "description": "Default administrative group with full permissions.",
                    "name": "Admin",
                    "customer": {
                        "customerId": 11111
                    }
                }
            ],
            "encrypted": false,
            "description": "16102-Services-/dev/sdh1",
            "sharable": true,
            "sizeInGb": 1,
            "name": "16102-Services-/dev/sdh1",
            "volume": {
                "region": {
                    "regionId": 19344
                },
                "budget": 10287,
                "volumeId": 211152,
                "status": "INACTIVE",
                "removable": true,
                "sizeString": "1GB",
                "dataCenter": {
                    "dataCenterId": 64351
                },
                "available": false,
                "customer": {
                    "customerId": 11111
                },
                "owningGroups": [
                    {
                        "groupId": 9465
                    }
                ],
                "encrypted": false,
                "description": "16102-Services-/dev/sdh1",
                "sizeInGb": 1,
                "name": "16102-Services-/dev/sdh1",
                "providerId": "vol-44c52f7d",
                "cloud": {
                    "cloudId": 1
                },
                "creationTimestamp": "1970-01-01T00:00:00.000+0000",
                "owningUser": {
                    "userId": 54321
                },
                "deviceId": "/dev/sdh",
                "owningAccount": {
                    "accountId": 16000
                }
            },
            "providerId": "snap-d2432df4",
            "cloud": {
                "computeDelegate": "org.dasein.cloud.aws.AWSCloud",
                "cloudId": 1,
                "computeX509KeyLabel": "AWS_PRIVATE_KEY",
                "status": "ACTIVE",
                "computeEndpoint": "https://ec2.us-east-1.amazonaws.com,https://ec2.us-west-1.amazonaws.com,https://ec2.eu-west-1.amazonaws.com",
                "privateCloud": false,
                "computeSecretKeyLabel": "AWS_SECRET_ACCESS_KEY",
                "computeX509CertLabel": "AWS_CERTIFICATE",
                "computeAccountNumberLabel": "AWS_ACCOUNT_NUMBER",
                "documentationLabel": null,
                "name": "Amazon Web Services",
                "cloudProviderName": "Amazon",
                "computeAccessKeyLabel": "AWS_ACCESS_KEY",
                "cloudProviderConsoleURL": "http://aws.amazon.com",
                "cloudProviderLogoURL": "/clouds/aws.gif"
            },
            "owningAccount": {
                "accountId": 16000,
                "cloudSubscriptionId": {
                    "cloudId": 1,
                    "accountNumber": "825279278023",
                    "cloudSubscriptionId": 12620,
                    "storageAccountNumber": null
                },
                "status": "ACTIVE",
                "configured": true,
                "provisioned": true,
                "planId": 2,
                "subscribed": true,
                "billingSystemId": "16000",
                "customer": {
                    "customerId": 11111
                },
                "defaultBudget": 10287,
                "name": "CSE",
                "owner": {
                    "userId": 12346
                },
                "alertConfiguration": {
                    "allowIndividualSmsAlerts": true,
                    "stopAlertsAfterMinutes": 60,
                    "globalSmsThreshold": 11,
                    "globalEmailThreshold": 11,
                    "allowIndividualEmailAlerts": true,
                    "alertIntervalInMinutes": 5
                }
            }
        },
        {
            "region": {
                "status": "ACTIVE",
                "description": "AWS Western United States (2)",
                "name": "Oregon (us-west-2)",
                "providerId": "us-west-2",
                "cloud": {
                    "cloudId": 1
                },
                "jurisdiction": "US",
                "customer": {
                    "customerId": 11111
                },
                "regionId": 19344
            },
            "snapshotId": 23368904,
            "budget": 10287,
            "createdTimestamp": "2012-11-28T21:43:18.000+0000",
            "status": "ACTIVE",
            "removable": true,
            "label": null,
            "available": true,
            "customer": {
                "businessName": "CSE",
                "customerId": 11111,
                "createdTimestamp": "2012-11-07T16:38:26.885+0000",
                "status": "ACTIVE",
                "accountingCurrency": "USD",
                "created": "2012-11-07T16:38:26.885+0000",
                "timeZone": "UTC",
                "automatedExchangeRates": true
            },
            "encrypted": false,
            "description": "snap-24364202",
            "sharable": true,
            "name": "snap-24364202",
            "sizeInGb": 8,
            "volume": {
                "region": {
                    "regionId": 19344
                },
                "budget": 10287,
                "volumeId": 211966,
                "status": "INACTIVE",
                "removable": false,
                "sizeString": "8GB",
                "dataCenter": {
                    "dataCenterId": 64351
                },
                "available": false,
                "customer": {
                    "customerId": 11111
                },
                "encrypted": false,
                "description": "vol-1eba4c27",
                "name": "vol-1eba4c27",
                "sizeInGb": 8,
                "providerId": "vol-1eba4c27",
                "cloud": {
                    "cloudId": 1
                },
                "server": {
                    "serverId": 324080
                },
                "creationTimestamp": "1970-01-01T00:00:00.000+0000",
                "owningUser": {
                    "userId": 99912
                },
                "deviceId": "/dev/sda1",
                "owningAccount": {
                    "accountId": 16000
                }
            },
            "providerId": "snap-24364202",
            "cloud": {
                "computeDelegate": "org.dasein.cloud.aws.AWSCloud",
                "cloudId": 1,
                "computeX509KeyLabel": "AWS_PRIVATE_KEY",
                "status": "ACTIVE",
                "computeEndpoint": "https://ec2.us-east-1.amazonaws.com,https://ec2.us-west-1.amazonaws.com,https://ec2.eu-west-1.amazonaws.com",
                "privateCloud": false,
                "computeSecretKeyLabel": "AWS_SECRET_ACCESS_KEY",
                "computeX509CertLabel": "AWS_CERTIFICATE",
                "computeAccountNumberLabel": "AWS_ACCOUNT_NUMBER",
                "documentationLabel": null,
                "name": "Amazon Web Services",
                "cloudProviderName": "Amazon",
                "computeAccessKeyLabel": "AWS_ACCESS_KEY",
                "cloudProviderConsoleURL": "http://aws.amazon.com",
                "cloudProviderLogoURL": "/clouds/aws.gif"
            },
            "owningAccount": {
                "accountId": 16000,
                "cloudSubscriptionId": {
                    "cloudId": 1,
                    "accountNumber": "825279278023",
                    "cloudSubscriptionId": 12620,
                    "storageAccountNumber": null
                },
                "status": "ACTIVE",
                "configured": true,
                "provisioned": true,
                "planId": 2,
                "subscribed": true,
                "billingSystemId": "16000",
                "customer": {
                    "customerId": 11111
                },
                "defaultBudget": 10287,
                "name": "CSE",
                "owner": {
                    "userId": 12346
                },
                "alertConfiguration": {
                    "allowIndividualSmsAlerts": true,
                    "stopAlertsAfterMinutes": 60,
                    "globalSmsThreshold": 11,
                    "globalEmailThreshold": 11,
                    "allowIndividualEmailAlerts": true,
                    "alertIntervalInMinutes": 5
                }
            }
        },
        {
            "region": {
                "status": "ACTIVE",
                "description": "AWS Western United States (2)",
                "name": "Oregon (us-west-2)",
                "providerId": "us-west-2",
                "cloud": {
                    "cloudId": 1
                },
                "jurisdiction": "US",
                "customer": {
                    "customerId": 11111
                },
                "regionId": 19344
            },
            "snapshotId": 23394023,
            "budget": 10287,
            "createdTimestamp": "2012-11-29T19:57:28.000+0000",
            "status": "ACTIVE",
            "removable": true,
            "label": null,
            "available": true,
            "customer": {
                "businessName": "CSE",
                "customerId": 11111,
                "createdTimestamp": "2012-11-07T16:38:26.885+0000",
                "status": "ACTIVE",
                "accountingCurrency": "USD",
                "created": "2012-11-07T16:38:26.885+0000",
                "timeZone": "UTC",
                "automatedExchangeRates": true
            },
            "encrypted": false,
            "description": "snap-a3ef9985",
            "sharable": true,
            "name": "snap-a3ef9985",
            "sizeInGb": 8,
            "volume": {
                "region": {
                    "regionId": 19344
                },
                "budget": 10287,
                "volumeId": 212123,
                "status": "INACTIVE",
                "removable": false,
                "sizeString": "8GB",
                "dataCenter": {
                    "dataCenterId": 64351
                },
                "available": false,
                "customer": {
                    "customerId": 11111
                },
                "encrypted": false,
                "description": "vol-3d12e304",
                "name": "vol-3d12e304",
                "sizeInGb": 8,
                "providerId": "vol-3d12e304",
                "cloud": {
                    "cloudId": 1
                },
                "server": {
                    "serverId": 324447
                },
                "creationTimestamp": "1970-01-01T00:00:00.000+0000",
                "owningUser": {
                    "userId": 99912
                },
                "deviceId": "/dev/sda1",
                "owningAccount": {
                    "accountId": 16000
                }
            },
            "providerId": "snap-a3ef9985",
            "cloud": {
                "computeDelegate": "org.dasein.cloud.aws.AWSCloud",
                "cloudId": 1,
                "computeX509KeyLabel": "AWS_PRIVATE_KEY",
                "status": "ACTIVE",
                "computeEndpoint": "https://ec2.us-east-1.amazonaws.com,https://ec2.us-west-1.amazonaws.com,https://ec2.eu-west-1.amazonaws.com",
                "privateCloud": false,
                "computeSecretKeyLabel": "AWS_SECRET_ACCESS_KEY",
                "computeX509CertLabel": "AWS_CERTIFICATE",
                "computeAccountNumberLabel": "AWS_ACCOUNT_NUMBER",
                "documentationLabel": null,
                "name": "Amazon Web Services",
                "cloudProviderName": "Amazon",
                "computeAccessKeyLabel": "AWS_ACCESS_KEY",
                "cloudProviderConsoleURL": "http://aws.amazon.com",
                "cloudProviderLogoURL": "/clouds/aws.gif"
            },
            "owningAccount": {
                "accountId": 16000,
                "cloudSubscriptionId": {
                    "cloudId": 1,
                    "accountNumber": "825279278023",
                    "cloudSubscriptionId": 12620,
                    "storageAccountNumber": null
                },
                "status": "ACTIVE",
                "configured": true,
                "provisioned": true,
                "planId": 2,
                "subscribed": true,
                "billingSystemId": "16000",
                "customer": {
                    "customerId": 11111
                },
                "defaultBudget": 10287,
                "name": "CSE",
                "owner": {
                    "userId": 12346
                },
                "alertConfiguration": {
                    "allowIndividualSmsAlerts": true,
                    "stopAlertsAfterMinutes": 60,
                    "globalSmsThreshold": 11,
                    "globalEmailThreshold": 11,
                    "allowIndividualEmailAlerts": true,
                    "alertIntervalInMinutes": 5
                }
            }
        },
        {
            "region": {
                "status": "ACTIVE",
                "description": "AWS Western United States (2)",
                "name": "Oregon (us-west-2)",
                "providerId": "us-west-2",
                "cloud": {
                    "cloudId": 1
                },
                "jurisdiction": "US",
                "customer": {
                    "customerId": 11111
                },
                "regionId": 19344
            },
            "snapshotId": 23496433,
            "budget": 10287,
            "createdTimestamp": "2012-12-04T20:53:12.000+0000",
            "status": "ACTIVE",
            "removable": true,
            "label": null,
            "available": true,
            "customer": {
                "businessName": "CSE",
                "customerId": 11111,
                "createdTimestamp": "2012-11-07T16:38:26.885+0000",
                "status": "ACTIVE",
                "accountingCurrency": "USD",
                "created": "2012-11-07T16:38:26.885+0000",
                "timeZone": "UTC",
                "automatedExchangeRates": true
            },
            "owningGroups": [
                {
                    "groupId": 9465,
                    "status": "ACTIVE",
                    "description": "Default administrative group with full permissions.",
                    "name": "Admin",
                    "customer": {
                        "customerId": 11111
                    }
                }
            ],
            "encrypted": false,
            "description": "16102-Services-/dev/sdh1",
            "sharable": true,
            "sizeInGb": 1,
            "name": "16102-Services-/dev/sdh1",
            "volume": {
                "region": {
                    "regionId": 19344
                },
                "budget": 10287,
                "volumeId": 212633,
                "status": "INACTIVE",
                "removable": true,
                "sizeString": "1GB",
                "dataCenter": {
                    "dataCenterId": 64351
                },
                "available": false,
                "customer": {
                    "customerId": 11111
                },
                "owningGroups": [
                    {
                        "groupId": 9465
                    }
                ],
                "encrypted": false,
                "description": "16102-Services-/dev/sdh1",
                "sizeInGb": 1,
                "name": "16102-Services-/dev/sdh1",
                "providerId": "vol-f7d42cce",
                "cloud": {
                    "cloudId": 1
                },
                "creationTimestamp": "1970-01-01T00:00:00.000+0000",
                "owningUser": {
                    "userId": 54321
                },
                "deviceId": "/dev/sdh",
                "owningAccount": {
                    "accountId": 16000
                }
            },
            "providerId": "snap-272b6b01",
            "cloud": {
                "computeDelegate": "org.dasein.cloud.aws.AWSCloud",
                "cloudId": 1,
                "computeX509KeyLabel": "AWS_PRIVATE_KEY",
                "status": "ACTIVE",
                "computeEndpoint": "https://ec2.us-east-1.amazonaws.com,https://ec2.us-west-1.amazonaws.com,https://ec2.eu-west-1.amazonaws.com",
                "privateCloud": false,
                "computeSecretKeyLabel": "AWS_SECRET_ACCESS_KEY",
                "computeX509CertLabel": "AWS_CERTIFICATE",
                "computeAccountNumberLabel": "AWS_ACCOUNT_NUMBER",
                "documentationLabel": null,
                "name": "Amazon Web Services",
                "cloudProviderName": "Amazon",
                "computeAccessKeyLabel": "AWS_ACCESS_KEY",
                "cloudProviderConsoleURL": "http://aws.amazon.com",
                "cloudProviderLogoURL": "/clouds/aws.gif"
            },
            "owningAccount": {
                "accountId": 16000,
                "cloudSubscriptionId": {
                    "cloudId": 1,
                    "accountNumber": "825279278023",
                    "cloudSubscriptionId": 12620,
                    "storageAccountNumber": null
                },
                "status": "ACTIVE",
                "configured": true,
                "provisioned": true,
                "planId": 2,
                "subscribed": true,
                "billingSystemId": "16000",
                "customer": {
                    "customerId": 11111
                },
                "defaultBudget": 10287,
                "name": "CSE",
                "owner": {
                    "userId": 12346
                },
                "alertConfiguration": {
                    "allowIndividualSmsAlerts": true,
                    "stopAlertsAfterMinutes": 60,
                    "globalSmsThreshold": 11,
                    "globalEmailThreshold": 11,
                    "allowIndividualEmailAlerts": true,
                    "alertIntervalInMinutes": 5
                }
            }
        },
        {
            "region": {
                "status": "ACTIVE",
                "description": "AWS Western United States (2)",
                "name": "Oregon (us-west-2)",
                "providerId": "us-west-2",
                "cloud": {
                    "cloudId": 1
                },
                "jurisdiction": "US",
                "customer": {
                    "customerId": 11111
                },
                "regionId": 19344
            },
            "snapshotId": 23549995,
            "budget": 10287,
            "createdTimestamp": "2012-12-06T23:07:59.000+0000",
            "status": "ACTIVE",
            "removable": true,
            "label": null,
            "available": true,
            "customer": {
                "businessName": "CSE",
                "customerId": 11111,
                "createdTimestamp": "2012-11-07T16:38:26.885+0000",
                "status": "ACTIVE",
                "accountingCurrency": "USD",
                "created": "2012-11-07T16:38:26.885+0000",
                "timeZone": "UTC",
                "automatedExchangeRates": true
            },
            "encrypted": false,
            "description": "snap-afa6e889",
            "sharable": true,
            "name": "snap-afa6e889",
            "sizeInGb": 8,
            "volume": {
                "region": {
                    "regionId": 19344
                },
                "budget": 10287,
                "volumeId": 213110,
                "status": "INACTIVE",
                "removable": false,
                "sizeString": "8GB",
                "dataCenter": {
                    "dataCenterId": 64351
                },
                "available": false,
                "customer": {
                    "customerId": 11111
                },
                "owningGroups": [
                    {
                        "groupId": 9465
                    }
                ],
                "encrypted": false,
                "description": "vol-11884c28",
                "sizeInGb": 8,
                "name": "vol-11884c28",
                "providerId": "vol-11884c28",
                "cloud": {
                    "cloudId": 1
                },
                "server": {
                    "serverId": 326586
                },
                "creationTimestamp": "1970-01-01T00:00:00.000+0000",
                "owningUser": {
                    "userId": 54321
                },
                "deviceId": "/dev/sda1",
                "owningAccount": {
                    "accountId": 16000
                }
            },
            "providerId": "snap-afa6e889",
            "cloud": {
                "computeDelegate": "org.dasein.cloud.aws.AWSCloud",
                "cloudId": 1,
                "computeX509KeyLabel": "AWS_PRIVATE_KEY",
                "status": "ACTIVE",
                "computeEndpoint": "https://ec2.us-east-1.amazonaws.com,https://ec2.us-west-1.amazonaws.com,https://ec2.eu-west-1.amazonaws.com",
                "privateCloud": false,
                "computeSecretKeyLabel": "AWS_SECRET_ACCESS_KEY",
                "computeX509CertLabel": "AWS_CERTIFICATE",
                "computeAccountNumberLabel": "AWS_ACCOUNT_NUMBER",
                "documentationLabel": null,
                "name": "Amazon Web Services",
                "cloudProviderName": "Amazon",
                "computeAccessKeyLabel": "AWS_ACCESS_KEY",
                "cloudProviderConsoleURL": "http://aws.amazon.com",
                "cloudProviderLogoURL": "/clouds/aws.gif"
            },
            "owningAccount": {
                "accountId": 16000,
                "cloudSubscriptionId": {
                    "cloudId": 1,
                    "accountNumber": "825279278023",
                    "cloudSubscriptionId": 12620,
                    "storageAccountNumber": null
                },
                "status": "ACTIVE",
                "configured": true,
                "provisioned": true,
                "planId": 2,
                "subscribed": true,
                "billingSystemId": "16000",
                "customer": {
                    "customerId": 11111
                },
                "defaultBudget": 10287,
                "name": "CSE",
                "owner": {
                    "userId": 12346
                },
                "alertConfiguration": {
                    "allowIndividualSmsAlerts": true,
                    "stopAlertsAfterMinutes": 60,
                    "globalSmsThreshold": 11,
                    "globalEmailThreshold": 11,
                    "allowIndividualEmailAlerts": true,
                    "alertIntervalInMinutes": 5
                }
            }
        },
        {
            "region": {
                "status": "ACTIVE",
                "description": "AWS Western United States (2)",
                "name": "Oregon (us-west-2)",
                "providerId": "us-west-2",
                "cloud": {
                    "cloudId": 1
                },
                "jurisdiction": "US",
                "customer": {
                    "customerId": 11111
                },
                "regionId": 19344
            },
            "snapshotId": 23552013,
            "budget": 10287,
            "createdTimestamp": "2012-12-07T00:29:26.000+0000",
            "status": "ACTIVE",
            "removable": true,
            "label": null,
            "available": true,
            "customer": {
                "businessName": "CSE",
                "customerId": 11111,
                "createdTimestamp": "2012-11-07T16:38:26.885+0000",
                "status": "ACTIVE",
                "accountingCurrency": "USD",
                "created": "2012-11-07T16:38:26.885+0000",
                "timeZone": "UTC",
                "automatedExchangeRates": true
            },
            "encrypted": false,
            "description": "snap-05db9523",
            "sharable": true,
            "name": "snap-05db9523",
            "sizeInGb": 8,
            "volume": {
                "region": {
                    "regionId": 19344
                },
                "budget": 10287,
                "volumeId": 213110,
                "status": "INACTIVE",
                "removable": false,
                "sizeString": "8GB",
                "dataCenter": {
                    "dataCenterId": 64351
                },
                "available": false,
                "customer": {
                    "customerId": 11111
                },
                "owningGroups": [
                    {
                        "groupId": 9465
                    }
                ],
                "encrypted": false,
                "description": "vol-11884c28",
                "sizeInGb": 8,
                "name": "vol-11884c28",
                "providerId": "vol-11884c28",
                "cloud": {
                    "cloudId": 1
                },
                "server": {
                    "serverId": 326586
                },
                "creationTimestamp": "1970-01-01T00:00:00.000+0000",
                "owningUser": {
                    "userId": 54321
                },
                "deviceId": "/dev/sda1",
                "owningAccount": {
                    "accountId": 16000
                }
            },
            "providerId": "snap-05db9523",
            "cloud": {
                "computeDelegate": "org.dasein.cloud.aws.AWSCloud",
                "cloudId": 1,
                "computeX509KeyLabel": "AWS_PRIVATE_KEY",
                "status": "ACTIVE",
                "computeEndpoint": "https://ec2.us-east-1.amazonaws.com,https://ec2.us-west-1.amazonaws.com,https://ec2.eu-west-1.amazonaws.com",
                "privateCloud": false,
                "computeSecretKeyLabel": "AWS_SECRET_ACCESS_KEY",
                "computeX509CertLabel": "AWS_CERTIFICATE",
                "computeAccountNumberLabel": "AWS_ACCOUNT_NUMBER",
                "documentationLabel": null,
                "name": "Amazon Web Services",
                "cloudProviderName": "Amazon",
                "computeAccessKeyLabel": "AWS_ACCESS_KEY",
                "cloudProviderConsoleURL": "http://aws.amazon.com",
                "cloudProviderLogoURL": "/clouds/aws.gif"
            },
            "owningAccount": {
                "accountId": 16000,
                "cloudSubscriptionId": {
                    "cloudId": 1,
                    "accountNumber": "825279278023",
                    "cloudSubscriptionId": 12620,
                    "storageAccountNumber": null
                },
                "status": "ACTIVE",
                "configured": true,
                "provisioned": true,
                "planId": 2,
                "subscribed": true,
                "billingSystemId": "16000",
                "customer": {
                    "customerId": 11111
                },
                "defaultBudget": 10287,
                "name": "CSE",
                "owner": {
                    "userId": 12346
                },
                "alertConfiguration": {
                    "allowIndividualSmsAlerts": true,
                    "stopAlertsAfterMinutes": 60,
                    "globalSmsThreshold": 11,
                    "globalEmailThreshold": 11,
                    "allowIndividualEmailAlerts": true,
                    "alertIntervalInMinutes": 5
                }
            }
        },
        {
            "region": {
                "status": "ACTIVE",
                "description": "AWS Western United States (2)",
                "name": "Oregon (us-west-2)",
                "providerId": "us-west-2",
                "cloud": {
                    "cloudId": 1
                },
                "jurisdiction": "US",
                "customer": {
                    "customerId": 11111
                },
                "regionId": 19344
            },
            "snapshotId": 23552035,
            "budget": 10287,
            "createdTimestamp": "2012-12-07T01:26:34.000+0000",
            "status": "ACTIVE",
            "removable": true,
            "label": null,
            "available": true,
            "customer": {
                "businessName": "CSE",
                "customerId": 11111,
                "createdTimestamp": "2012-11-07T16:38:26.885+0000",
                "status": "ACTIVE",
                "accountingCurrency": "USD",
                "created": "2012-11-07T16:38:26.885+0000",
                "timeZone": "UTC",
                "automatedExchangeRates": true
            },
            "encrypted": false,
            "description": "snap-2efdb308",
            "sharable": true,
            "name": "snap-2efdb308",
            "sizeInGb": 8,
            "volume": {
                "region": {
                    "regionId": 19344
                },
                "budget": 10287,
                "volumeId": 213110,
                "status": "INACTIVE",
                "removable": false,
                "sizeString": "8GB",
                "dataCenter": {
                    "dataCenterId": 64351
                },
                "available": false,
                "customer": {
                    "customerId": 11111
                },
                "owningGroups": [
                    {
                        "groupId": 9465
                    }
                ],
                "encrypted": false,
                "description": "vol-11884c28",
                "sizeInGb": 8,
                "name": "vol-11884c28",
                "providerId": "vol-11884c28",
                "cloud": {
                    "cloudId": 1
                },
                "server": {
                    "serverId": 326586
                },
                "creationTimestamp": "1970-01-01T00:00:00.000+0000",
                "owningUser": {
                    "userId": 54321
                },
                "deviceId": "/dev/sda1",
                "owningAccount": {
                    "accountId": 16000
                }
            },
            "providerId": "snap-2efdb308",
            "cloud": {
                "computeDelegate": "org.dasein.cloud.aws.AWSCloud",
                "cloudId": 1,
                "computeX509KeyLabel": "AWS_PRIVATE_KEY",
                "status": "ACTIVE",
                "computeEndpoint": "https://ec2.us-east-1.amazonaws.com,https://ec2.us-west-1.amazonaws.com,https://ec2.eu-west-1.amazonaws.com",
                "privateCloud": false,
                "computeSecretKeyLabel": "AWS_SECRET_ACCESS_KEY",
                "computeX509CertLabel": "AWS_CERTIFICATE",
                "computeAccountNumberLabel": "AWS_ACCOUNT_NUMBER",
                "documentationLabel": null,
                "name": "Amazon Web Services",
                "cloudProviderName": "Amazon",
                "computeAccessKeyLabel": "AWS_ACCESS_KEY",
                "cloudProviderConsoleURL": "http://aws.amazon.com",
                "cloudProviderLogoURL": "/clouds/aws.gif"
            },
            "owningAccount": {
                "accountId": 16000,
                "cloudSubscriptionId": {
                    "cloudId": 1,
                    "accountNumber": "825279278023",
                    "cloudSubscriptionId": 12620,
                    "storageAccountNumber": null
                },
                "status": "ACTIVE",
                "configured": true,
                "provisioned": true,
                "planId": 2,
                "subscribed": true,
                "billingSystemId": "16000",
                "customer": {
                    "customerId": 11111
                },
                "defaultBudget": 10287,
                "name": "CSE",
                "owner": {
                    "userId": 12346
                },
                "alertConfiguration": {
                    "allowIndividualSmsAlerts": true,
                    "stopAlertsAfterMinutes": 60,
                    "globalSmsThreshold": 11,
                    "globalEmailThreshold": 11,
                    "allowIndividualEmailAlerts": true,
                    "alertIntervalInMinutes": 5
                }
            }
        },
        {
            "region": {
                "status": "ACTIVE",
                "description": "AWS Western United States (2)",
                "name": "Oregon (us-west-2)",
                "providerId": "us-west-2",
                "cloud": {
                    "cloudId": 1
                },
                "jurisdiction": "US",
                "customer": {
                    "customerId": 11111
                },
                "regionId": 19344
            },
            "snapshotId": 23560344,
            "budget": 10287,
            "createdTimestamp": "2012-12-09T23:21:22.000+0000",
            "status": "ACTIVE",
            "removable": true,
            "label": null,
            "available": true,
            "customer": {
                "businessName": "CSE",
                "customerId": 11111,
                "createdTimestamp": "2012-11-07T16:38:26.885+0000",
                "status": "ACTIVE",
                "accountingCurrency": "USD",
                "created": "2012-11-07T16:38:26.885+0000",
                "timeZone": "UTC",
                "automatedExchangeRates": true
            },
            "encrypted": false,
            "description": "snap-52227374",
            "sharable": true,
            "name": "snap-52227374",
            "sizeInGb": 8,
            "volume": {
                "region": {
                    "regionId": 19344
                },
                "budget": 10287,
                "volumeId": 213413,
                "status": "INACTIVE",
                "removable": false,
                "sizeString": "8GB",
                "dataCenter": {
                    "dataCenterId": 64351
                },
                "available": false,
                "customer": {
                    "customerId": 11111
                },
                "encrypted": false,
                "description": "vol-b13cfc88",
                "name": "vol-b13cfc88",
                "sizeInGb": 8,
                "providerId": "vol-b13cfc88",
                "cloud": {
                    "cloudId": 1
                },
                "server": {
                    "serverId": 327124
                },
                "creationTimestamp": "1970-01-01T00:00:00.000+0000",
                "deviceId": "/dev/sda1",
                "owningAccount": {
                    "accountId": 16000
                }
            },
            "providerId": "snap-52227374",
            "cloud": {
                "computeDelegate": "org.dasein.cloud.aws.AWSCloud",
                "cloudId": 1,
                "computeX509KeyLabel": "AWS_PRIVATE_KEY",
                "status": "ACTIVE",
                "computeEndpoint": "https://ec2.us-east-1.amazonaws.com,https://ec2.us-west-1.amazonaws.com,https://ec2.eu-west-1.amazonaws.com",
                "privateCloud": false,
                "computeSecretKeyLabel": "AWS_SECRET_ACCESS_KEY",
                "computeX509CertLabel": "AWS_CERTIFICATE",
                "computeAccountNumberLabel": "AWS_ACCOUNT_NUMBER",
                "documentationLabel": null,
                "name": "Amazon Web Services",
                "cloudProviderName": "Amazon",
                "computeAccessKeyLabel": "AWS_ACCESS_KEY",
                "cloudProviderConsoleURL": "http://aws.amazon.com",
                "cloudProviderLogoURL": "/clouds/aws.gif"
            },
            "owningAccount": {
                "accountId": 16000,
                "cloudSubscriptionId": {
                    "cloudId": 1,
                    "accountNumber": "825279278023",
                    "cloudSubscriptionId": 12620,
                    "storageAccountNumber": null
                },
                "status": "ACTIVE",
                "configured": true,
                "provisioned": true,
                "planId": 2,
                "subscribed": true,
                "billingSystemId": "16000",
                "customer": {
                    "customerId": 11111
                },
                "defaultBudget": 10287,
                "name": "CSE",
                "owner": {
                    "userId": 12346
                },
                "alertConfiguration": {
                    "allowIndividualSmsAlerts": true,
                    "stopAlertsAfterMinutes": 60,
                    "globalSmsThreshold": 11,
                    "globalEmailThreshold": 11,
                    "allowIndividualEmailAlerts": true,
                    "alertIntervalInMinutes": 5
                }
            }
        },
        {
            "region": {
                "status": "ACTIVE",
                "description": "AWS Western United States (2)",
                "name": "Oregon (us-west-2)",
                "providerId": "us-west-2",
                "cloud": {
                    "cloudId": 1
                },
                "jurisdiction": "US",
                "customer": {
                    "customerId": 11111
                },
                "regionId": 19344
            },
            "snapshotId": 23560345,
            "budget": 10287,
            "createdTimestamp": "2012-12-10T03:26:09.000+0000",
            "status": "ACTIVE",
            "removable": true,
            "label": null,
            "available": true,
            "customer": {
                "businessName": "CSE",
                "customerId": 11111,
                "createdTimestamp": "2012-11-07T16:38:26.885+0000",
                "status": "ACTIVE",
                "accountingCurrency": "USD",
                "created": "2012-11-07T16:38:26.885+0000",
                "timeZone": "UTC",
                "automatedExchangeRates": true
            },
            "owningGroups": [
                {
                    "groupId": 9465,
                    "status": "ACTIVE",
                    "description": "Default administrative group with full permissions.",
                    "name": "Admin",
                    "customer": {
                        "customerId": 11111
                    }
                }
            ],
            "encrypted": true,
            "description": "16406-Services-/dev/sdh1",
            "sharable": true,
            "sizeInGb": 1,
            "name": "16406-Services-/dev/sdh1",
            "volume": {
                "region": {
                    "regionId": 19344
                },
                "budget": 10287,
                "volumeId": 213315,
                "status": "INACTIVE",
                "removable": true,
                "sizeString": "1GB",
                "dataCenter": {
                    "dataCenterId": 64351
                },
                "available": false,
                "customer": {
                    "customerId": 11111
                },
                "owningGroups": [
                    {
                        "groupId": 9465
                    }
                ],
                "encrypted": true,
                "description": "16406-Services-/dev/sdh1",
                "sizeInGb": 1,
                "name": "16406-Services-/dev/sdh1",
                "providerId": "vol-e88340d1",
                "cloud": {
                    "cloudId": 1
                },
                "creationTimestamp": "1970-01-01T00:00:00.000+0000",
                "owningUser": {
                    "userId": 54321
                },
                "deviceId": "/dev/sdh",
                "owningAccount": {
                    "accountId": 16000
                }
            },
            "providerId": "snap-a1a1f087",
            "cloud": {
                "computeDelegate": "org.dasein.cloud.aws.AWSCloud",
                "cloudId": 1,
                "computeX509KeyLabel": "AWS_PRIVATE_KEY",
                "status": "ACTIVE",
                "computeEndpoint": "https://ec2.us-east-1.amazonaws.com,https://ec2.us-west-1.amazonaws.com,https://ec2.eu-west-1.amazonaws.com",
                "privateCloud": false,
                "computeSecretKeyLabel": "AWS_SECRET_ACCESS_KEY",
                "computeX509CertLabel": "AWS_CERTIFICATE",
                "computeAccountNumberLabel": "AWS_ACCOUNT_NUMBER",
                "documentationLabel": null,
                "name": "Amazon Web Services",
                "cloudProviderName": "Amazon",
                "computeAccessKeyLabel": "AWS_ACCESS_KEY",
                "cloudProviderConsoleURL": "http://aws.amazon.com",
                "cloudProviderLogoURL": "/clouds/aws.gif"
            },
            "owningAccount": {
                "accountId": 16000,
                "cloudSubscriptionId": {
                    "cloudId": 1,
                    "accountNumber": "825279278023",
                    "cloudSubscriptionId": 12620,
                    "storageAccountNumber": null
                },
                "status": "ACTIVE",
                "configured": true,
                "provisioned": true,
                "planId": 2,
                "subscribed": true,
                "billingSystemId": "16000",
                "customer": {
                    "customerId": 11111
                },
                "defaultBudget": 10287,
                "name": "CSE",
                "owner": {
                    "userId": 12346
                },
                "alertConfiguration": {
                    "allowIndividualSmsAlerts": true,
                    "stopAlertsAfterMinutes": 60,
                    "globalSmsThreshold": 11,
                    "globalEmailThreshold": 11,
                    "allowIndividualEmailAlerts": true,
                    "alertIntervalInMinutes": 5
                }
            }
        },
        {
            "region": {
                "status": "ACTIVE",
                "description": "AWS Western United States (2)",
                "name": "Oregon (us-west-2)",
                "providerId": "us-west-2",
                "cloud": {
                    "cloudId": 1
                },
                "jurisdiction": "US",
                "customer": {
                    "customerId": 11111
                },
                "regionId": 19344
            },
            "snapshotId": 23562281,
            "budget": 10287,
            "createdTimestamp": "2012-12-10T00:24:08.000+0000",
            "status": "ACTIVE",
            "removable": true,
            "label": null,
            "available": true,
            "customer": {
                "businessName": "CSE",
                "customerId": 11111,
                "createdTimestamp": "2012-11-07T16:38:26.885+0000",
                "status": "ACTIVE",
                "accountingCurrency": "USD",
                "created": "2012-11-07T16:38:26.885+0000",
                "timeZone": "UTC",
                "automatedExchangeRates": true
            },
            "encrypted": false,
            "description": "snap-fc4617da",
            "sharable": true,
            "name": "snap-fc4617da",
            "sizeInGb": 8,
            "volume": {
                "region": {
                    "regionId": 19344
                },
                "budget": 10287,
                "volumeId": 213110,
                "status": "INACTIVE",
                "removable": false,
                "sizeString": "8GB",
                "dataCenter": {
                    "dataCenterId": 64351
                },
                "available": false,
                "customer": {
                    "customerId": 11111
                },
                "owningGroups": [
                    {
                        "groupId": 9465
                    }
                ],
                "encrypted": false,
                "description": "vol-11884c28",
                "sizeInGb": 8,
                "name": "vol-11884c28",
                "providerId": "vol-11884c28",
                "cloud": {
                    "cloudId": 1
                },
                "server": {
                    "serverId": 326586
                },
                "creationTimestamp": "1970-01-01T00:00:00.000+0000",
                "owningUser": {
                    "userId": 54321
                },
                "deviceId": "/dev/sda1",
                "owningAccount": {
                    "accountId": 16000
                }
            },
            "providerId": "snap-fc4617da",
            "cloud": {
                "computeDelegate": "org.dasein.cloud.aws.AWSCloud",
                "cloudId": 1,
                "computeX509KeyLabel": "AWS_PRIVATE_KEY",
                "status": "ACTIVE",
                "computeEndpoint": "https://ec2.us-east-1.amazonaws.com,https://ec2.us-west-1.amazonaws.com,https://ec2.eu-west-1.amazonaws.com",
                "privateCloud": false,
                "computeSecretKeyLabel": "AWS_SECRET_ACCESS_KEY",
                "computeX509CertLabel": "AWS_CERTIFICATE",
                "computeAccountNumberLabel": "AWS_ACCOUNT_NUMBER",
                "documentationLabel": null,
                "name": "Amazon Web Services",
                "cloudProviderName": "Amazon",
                "computeAccessKeyLabel": "AWS_ACCESS_KEY",
                "cloudProviderConsoleURL": "http://aws.amazon.com",
                "cloudProviderLogoURL": "/clouds/aws.gif"
            },
            "owningAccount": {
                "accountId": 16000,
                "cloudSubscriptionId": {
                    "cloudId": 1,
                    "accountNumber": "825279278023",
                    "cloudSubscriptionId": 12620,
                    "storageAccountNumber": null
                },
                "status": "ACTIVE",
                "configured": true,
                "provisioned": true,
                "planId": 2,
                "subscribed": true,
                "billingSystemId": "16000",
                "customer": {
                    "customerId": 11111
                },
                "defaultBudget": 10287,
                "name": "CSE",
                "owner": {
                    "userId": 12346
                },
                "alertConfiguration": {
                    "allowIndividualSmsAlerts": true,
                    "stopAlertsAfterMinutes": 60,
                    "globalSmsThreshold": 11,
                    "globalEmailThreshold": 11,
                    "allowIndividualEmailAlerts": true,
                    "alertIntervalInMinutes": 5
                }
            }
        },
        {
            "region": {
                "status": "ACTIVE",
                "description": "AWS Western United States (2)",
                "name": "Oregon (us-west-2)",
                "providerId": "us-west-2",
                "cloud": {
                    "cloudId": 1
                },
                "jurisdiction": "US",
                "customer": {
                    "customerId": 11111
                },
                "regionId": 19344
            },
            "snapshotId": 23562282,
            "budget": 10287,
            "createdTimestamp": "2012-12-10T01:01:43.000+0000",
            "status": "ACTIVE",
            "removable": true,
            "label": null,
            "available": true,
            "customer": {
                "businessName": "CSE",
                "customerId": 11111,
                "createdTimestamp": "2012-11-07T16:38:26.885+0000",
                "status": "ACTIVE",
                "accountingCurrency": "USD",
                "created": "2012-11-07T16:38:26.885+0000",
                "timeZone": "UTC",
                "automatedExchangeRates": true
            },
            "encrypted": false,
            "description": "snap-a27a2b84",
            "sharable": true,
            "name": "snap-a27a2b84",
            "sizeInGb": 8,
            "volume": {
                "region": {
                    "regionId": 19344
                },
                "budget": 10287,
                "volumeId": 213413,
                "status": "INACTIVE",
                "removable": false,
                "sizeString": "8GB",
                "dataCenter": {
                    "dataCenterId": 64351
                },
                "available": false,
                "customer": {
                    "customerId": 11111
                },
                "encrypted": false,
                "description": "vol-b13cfc88",
                "name": "vol-b13cfc88",
                "sizeInGb": 8,
                "providerId": "vol-b13cfc88",
                "cloud": {
                    "cloudId": 1
                },
                "server": {
                    "serverId": 327124
                },
                "creationTimestamp": "1970-01-01T00:00:00.000+0000",
                "deviceId": "/dev/sda1",
                "owningAccount": {
                    "accountId": 16000
                }
            },
            "providerId": "snap-a27a2b84",
            "cloud": {
                "computeDelegate": "org.dasein.cloud.aws.AWSCloud",
                "cloudId": 1,
                "computeX509KeyLabel": "AWS_PRIVATE_KEY",
                "status": "ACTIVE",
                "computeEndpoint": "https://ec2.us-east-1.amazonaws.com,https://ec2.us-west-1.amazonaws.com,https://ec2.eu-west-1.amazonaws.com",
                "privateCloud": false,
                "computeSecretKeyLabel": "AWS_SECRET_ACCESS_KEY",
                "computeX509CertLabel": "AWS_CERTIFICATE",
                "computeAccountNumberLabel": "AWS_ACCOUNT_NUMBER",
                "documentationLabel": null,
                "name": "Amazon Web Services",
                "cloudProviderName": "Amazon",
                "computeAccessKeyLabel": "AWS_ACCESS_KEY",
                "cloudProviderConsoleURL": "http://aws.amazon.com",
                "cloudProviderLogoURL": "/clouds/aws.gif"
            },
            "owningAccount": {
                "accountId": 16000,
                "cloudSubscriptionId": {
                    "cloudId": 1,
                    "accountNumber": "825279278023",
                    "cloudSubscriptionId": 12620,
                    "storageAccountNumber": null
                },
                "status": "ACTIVE",
                "configured": true,
                "provisioned": true,
                "planId": 2,
                "subscribed": true,
                "billingSystemId": "16000",
                "customer": {
                    "customerId": 11111
                },
                "defaultBudget": 10287,
                "name": "CSE",
                "owner": {
                    "userId": 12346
                },
                "alertConfiguration": {
                    "allowIndividualSmsAlerts": true,
                    "stopAlertsAfterMinutes": 60,
                    "globalSmsThreshold": 11,
                    "globalEmailThreshold": 11,
                    "allowIndividualEmailAlerts": true,
                    "alertIntervalInMinutes": 5
                }
            }
        },
        {
            "region": {
                "status": "ACTIVE",
                "description": "AWS Western United States (2)",
                "name": "Oregon (us-west-2)",
                "providerId": "us-west-2",
                "cloud": {
                    "cloudId": 1
                },
                "jurisdiction": "US",
                "customer": {
                    "customerId": 11111
                },
                "regionId": 19344
            },
            "snapshotId": 23562283,
            "budget": 10287,
            "createdTimestamp": "2012-12-10T01:59:13.000+0000",
            "status": "ACTIVE",
            "removable": true,
            "label": null,
            "available": true,
            "customer": {
                "businessName": "CSE",
                "customerId": 11111,
                "createdTimestamp": "2012-11-07T16:38:26.885+0000",
                "status": "ACTIVE",
                "accountingCurrency": "USD",
                "created": "2012-11-07T16:38:26.885+0000",
                "timeZone": "UTC",
                "automatedExchangeRates": true
            },
            "encrypted": false,
            "description": "snap-e794c5c1",
            "sharable": true,
            "name": "snap-e794c5c1",
            "sizeInGb": 8,
            "volume": {
                "region": {
                    "regionId": 19344
                },
                "budget": 10287,
                "volumeId": 213413,
                "status": "INACTIVE",
                "removable": false,
                "sizeString": "8GB",
                "dataCenter": {
                    "dataCenterId": 64351
                },
                "available": false,
                "customer": {
                    "customerId": 11111
                },
                "encrypted": false,
                "description": "vol-b13cfc88",
                "name": "vol-b13cfc88",
                "sizeInGb": 8,
                "providerId": "vol-b13cfc88",
                "cloud": {
                    "cloudId": 1
                },
                "server": {
                    "serverId": 327124
                },
                "creationTimestamp": "1970-01-01T00:00:00.000+0000",
                "deviceId": "/dev/sda1",
                "owningAccount": {
                    "accountId": 16000
                }
            },
            "providerId": "snap-e794c5c1",
            "cloud": {
                "computeDelegate": "org.dasein.cloud.aws.AWSCloud",
                "cloudId": 1,
                "computeX509KeyLabel": "AWS_PRIVATE_KEY",
                "status": "ACTIVE",
                "computeEndpoint": "https://ec2.us-east-1.amazonaws.com,https://ec2.us-west-1.amazonaws.com,https://ec2.eu-west-1.amazonaws.com",
                "privateCloud": false,
                "computeSecretKeyLabel": "AWS_SECRET_ACCESS_KEY",
                "computeX509CertLabel": "AWS_CERTIFICATE",
                "computeAccountNumberLabel": "AWS_ACCOUNT_NUMBER",
                "documentationLabel": null,
                "name": "Amazon Web Services",
                "cloudProviderName": "Amazon",
                "computeAccessKeyLabel": "AWS_ACCESS_KEY",
                "cloudProviderConsoleURL": "http://aws.amazon.com",
                "cloudProviderLogoURL": "/clouds/aws.gif"
            },
            "owningAccount": {
                "accountId": 16000,
                "cloudSubscriptionId": {
                    "cloudId": 1,
                    "accountNumber": "825279278023",
                    "cloudSubscriptionId": 12620,
                    "storageAccountNumber": null
                },
                "status": "ACTIVE",
                "configured": true,
                "provisioned": true,
                "planId": 2,
                "subscribed": true,
                "billingSystemId": "16000",
                "customer": {
                    "customerId": 11111
                },
                "defaultBudget": 10287,
                "name": "CSE",
                "owner": {
                    "userId": 12346
                },
                "alertConfiguration": {
                    "allowIndividualSmsAlerts": true,
                    "stopAlertsAfterMinutes": 60,
                    "globalSmsThreshold": 11,
                    "globalEmailThreshold": 11,
                    "allowIndividualEmailAlerts": true,
                    "alertIntervalInMinutes": 5
                }
            }
        }
    ]
}
'''

one_item = '''
{
    "snapshots": [
        {
            "region": {
                "status": "ACTIVE",
                "description": "AWS Southeast Asia/Pacific (2)",
                "name": "Sydney (ap-southeast-2)",
                "providerId": "ap-southeast-2",
                "cloud": {
                    "cloudId": 1
                },
                "jurisdiction": "AU",
                "customer": {
                    "customerId": 11111
                },
                "regionId": 19556
            },
            "snapshotId": 23237460,
            "budget": 10287,
            "createdTimestamp": "2012-11-20T01:31:53.000+0000",
            "status": "ACTIVE",
            "removable": true,
            "label": null,
            "available": true,
            "customer": {
                "businessName": "CSE",
                "customerId": 11111,
                "createdTimestamp": "2012-11-07T16:38:26.885+0000",
                "status": "ACTIVE",
                "accountingCurrency": "USD",
                "created": "2012-11-07T16:38:26.885+0000",
                "timeZone": "UTC",
                "automatedExchangeRates": true
            },
            "encrypted": false,
            "description": "snap-b0810e80",
            "sharable": true,
            "name": "snap-b0810e80",
            "sizeInGb": 8,
            "volume": {
                "region": {
                    "regionId": 19556
                },
                "budget": 10287,
                "volumeId": 209179,
                "status": "INACTIVE",
                "removable": false,
                "sizeString": "8GB",
                "dataCenter": {
                    "dataCenterId": 64716
                },
                "available": false,
                "customer": {
                    "customerId": 11111
                },
                "owningGroups": [
                    {
                        "groupId": 9465
                    }
                ],
                "encrypted": false,
                "description": "vol-9a31cda9",
                "sizeInGb": 8,
                "name": "vol-9a31cda9",
                "providerId": "vol-9a31cda9",
                "cloud": {
                    "cloudId": 1
                },
                "server": {
                    "serverId": 319622
                },
                "creationTimestamp": "1970-01-01T00:00:00.000+0000",
                "owningUser": {
                    "userId": 12345
                },
                "deviceId": "/dev/sda1",
                "owningAccount": {
                    "accountId": 16000
                }
            },
            "providerId": "snap-b0810e80",
            "cloud": {
                "computeDelegate": "org.dasein.cloud.aws.AWSCloud",
                "cloudId": 1,
                "computeX509KeyLabel": "AWS_PRIVATE_KEY",
                "status": "ACTIVE",
                "computeEndpoint": "https://ec2.us-east-1.amazonaws.com,https://ec2.us-west-1.amazonaws.com,https://ec2.eu-west-1.amazonaws.com",
                "privateCloud": false,
                "computeSecretKeyLabel": "AWS_SECRET_ACCESS_KEY",
                "computeX509CertLabel": "AWS_CERTIFICATE",
                "computeAccountNumberLabel": "AWS_ACCOUNT_NUMBER",
                "documentationLabel": null,
                "name": "Amazon Web Services",
                "cloudProviderName": "Amazon",
                "computeAccessKeyLabel": "AWS_ACCESS_KEY",
                "cloudProviderConsoleURL": "http://aws.amazon.com",
                "cloudProviderLogoURL": "/clouds/aws.gif"
            },
            "owningAccount": {
                "accountId": 16000,
                "cloudSubscriptionId": {
                    "cloudId": 1,
                    "accountNumber": "825279278023",
                    "cloudSubscriptionId": 12620,
                    "storageAccountNumber": null
                },
                "status": "ACTIVE",
                "configured": true,
                "provisioned": true,
                "planId": 2,
                "subscribed": true,
                "billingSystemId": "16000",
                "customer": {
                    "customerId": 11111
                },
                "defaultBudget": 10287,
                "name": "CSE",
                "owner": {
                    "userId": 12346
                },
                "alertConfiguration": {
                    "allowIndividualSmsAlerts": true,
                    "stopAlertsAfterMinutes": 60,
                    "globalSmsThreshold": 11,
                    "globalEmailThreshold": 11,
                    "allowIndividualEmailAlerts": true,
                    "alertIntervalInMinutes": 5
                }
            }
        }
    ]
}
'''
