all_machine_images = '''{
    "images": [
        {
            "region": {
                "regionId": 19344
            },
            "budget": 10287,
            "platform": "UBUNTU",
            "status": "ACTIVE",
            "removable": false,
            "owningCloudAccountNumber": "825279278023",
            "architecture": "I64",
            "customer": {
                "customerId": 11111
            },
            "owningGroups": [
                {
                    "groupId": 9465
                }
            ],
            "description": "dpando-Ubuntu1204-enStratus17-LAMP-121108",
            "sharable": true,
            "name": "deployment_image_121203",
            "cloud": {
                "cloudId": 1
            },
            "providerId": "ami-087ef738",
            "machineImageId": 281141,
            "creationTimestamp": "1970-01-01T00:00:00.000+0000",
            "owningUser": {
                "userId": 12345
            },
            "owningAccount": {
                "accountId": 16000
            }
        },
        {
            "region": {
                "regionId": 19344
            },
            "budget": 10287,
            "platform": "UBUNTU",
            "status": "ACTIVE",
            "removable": true,
            "owningCloudAccountNumber": "825279278023",
            "architecture": "I64",
            "customer": {
                "customerId": 11111
            },
            "owningGroups": [
                {
                    "groupId": 9465
                }
            ],
            "description": "dpando-dynLB-121122",
            "sharable": true,
            "name": "dpando-dynLB-121122",
            "providerId": "ami-10ea6220",
            "machineImageId": 284436,
            "cloud": {
                "cloudId": 1
            },
            "creationTimestamp": "1970-01-01T00:00:00.000+0000",
            "agentVersion": 17,
            "owningUser": {
                "userId": 12345
            },
            "owningAccount": {
                "accountId": 16000
            }
        },
        {
            "region": {
                "regionId": 19344
            },
            "budget": 10287,
            "platform": "UBUNTU",
            "status": "ACTIVE",
            "removable": true,
            "owningCloudAccountNumber": "825279278023",
            "architecture": "I64",
            "customer": {
                "customerId": 11111
            },
            "owningGroups": [
                {
                    "groupId": 9465
                }
            ],
            "description": "deployment_Ubuntu1004_121210_debug",
            "sharable": true,
            "name": "deployment_Ubuntu1004_121210_debug",
            "cloud": {
                "cloudId": 1
            },
            "providerId": "ami-1669e126",
            "machineImageId": 287034,
            "creationTimestamp": "1970-01-01T00:00:00.000+0000",
            "owningUser": {
                "userId": 12345
            },
            "owningAccount": {
                "accountId": 16000
            }
        }
    ]
}
'''

one_image = '''{
    "images": [
        {
            "region": {
                "regionId": 19344
            },
            "budget": 10287,
            "platform": "UBUNTU",
            "status": "ACTIVE",
            "removable": true,
            "owningCloudAccountNumber": "099720109477",
            "architecture": "I64",
            "customer": {
                "customerId": 11111
            },
            "description": "ubuntu-lucid-10.04-amd64-server-20120913 (x86_64 Ubuntu)",
            "sharable": false,
            "name": "ubuntu/images/ebs/ubuntu-lucid-10.04-amd64-server-20120913",
            "cloud": {
                "cloudId": 1
            },
            "machineImageId": 284542,
            "providerId": "ami-1a4fc12a",
            "creationTimestamp": "1970-01-01T00:00:00.000+0000",
            "owningUser": {
                "userId": 12345
            },
            "agentVersion": 17
        }
    ]
}
'''
