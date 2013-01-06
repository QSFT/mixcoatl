all_items = """
{
    "cmAccounts": [
        {
            "accountNumber": "", 
            "budget": -1, 
            "cmAccountId": 3610, 
            "cmService": {
                "budget": 0, 
                "cmServiceId": 3710, 
                "cmSystem": {
                    "cmSystemId": 1
                }, 
                "customer": {
                    "customerId": 11111
                }, 
                "description": "A Chef Server Account", 
                "label": "iconlightbulb", 
                "name": "chef-cm", 
                "properties": {}, 
                "removable": true, 
                "serviceEndpoint": "http://chef.server:4000", 
                "status": "ACTIVE"
            }, 
            "createdTimestamp": "2013-01-06T06:50:29.326+0000", 
            "customer": {
                "accountingCurrency": "USD", 
                "automatedExchangeRates": true, 
                "businessName": "CSE", 
                "created": "2012-11-07T16:38:26.885+0000", 
                "createdTimestamp": "2012-11-07T16:38:26.885+0000", 
                "customerId": 11111, 
                "status": "ACTIVE", 
                "timeZone": "UTC"
            }, 
            "description": "A Chef Server Account", 
            "guid": "/customer/11111/cmAccount/3610", 
            "label": "iconlightbulb", 
            "lastModifiedTimestamp": "2013-01-06T06:50:29.326+0000", 
            "name": "chef-cm", 
            "removable": true, 
            "status": "ACTIVE"
        }, 
        {
            "accountNumber": "1234567890", 
            "budget": -1, 
            "cmAccountId": 3609, 
            "cmService": {
                "budget": 0, 
                "cmServiceId": 3709, 
                "cmSystem": {
                    "cmSystemId": 3
                }, 
                "customer": {
                    "customerId": 11111
                }, 
                "description": "an object store cm account", 
                "label": "flagred", 
                "name": "object-store-1234", 
                "properties": {
                    "bucket": "object-store-1234", 
                    "cloudDelegate": "org.dasein.cloud.aws.AWSCloud", 
                    "esRegionId": "19343", 
                    "regionId": "us-east-1"
                }, 
                "removable": true, 
                "serviceEndpoint": "https://ec2.us-east-1.amazonaws.com,https://ec2.us-west-1.amazonaws.com,https://ec2.eu-west-1.amazonaws.com", 
                "status": "ACTIVE"
            }, 
            "createdTimestamp": "2013-01-06T06:48:06.699+0000", 
            "customer": {
                "accountingCurrency": "USD", 
                "automatedExchangeRates": true, 
                "businessName": "CSE", 
                "created": "2012-11-07T16:38:26.885+0000", 
                "createdTimestamp": "2012-11-07T16:38:26.885+0000", 
                "customerId": 11111, 
                "status": "ACTIVE", 
                "timeZone": "UTC"
            }, 
            "description": "an object store cm account", 
            "guid": "/customer/11111/cmAccount/3609", 
            "label": "flagred", 
            "lastModifiedTimestamp": "2013-01-06T06:48:06.699+0000", 
            "name": "object-store-1234", 
            "removable": true, 
            "status": "ACTIVE"
        }
    ]
}
"""

one_item = """
{
    "cmAccounts": [
        {
            "accountNumber": "", 
            "budget": -1, 
            "cmAccountId": 3610, 
            "cmService": {
                "budget": 0, 
                "cmServiceId": 3710, 
                "cmSystem": {
                    "cmSystemId": 1
                }, 
                "customer": {
                    "customerId": 11111
                }, 
                "description": "A Chef Server Account", 
                "label": "iconlightbulb", 
                "name": "chef-cm", 
                "properties": {}, 
                "removable": true, 
                "serviceEndpoint": "http://chef.server:4000", 
                "status": "ACTIVE"
            }, 
            "createdTimestamp": "2013-01-06T06:50:29.326+0000", 
            "customer": {
                "accountingCurrency": "USD", 
                "automatedExchangeRates": true, 
                "businessName": "CSE", 
                "created": "2012-11-07T16:38:26.885+0000", 
                "createdTimestamp": "2012-11-07T16:38:26.885+0000", 
                "customerId": 11111, 
                "status": "ACTIVE", 
                "timeZone": "UTC"
            }, 
            "description": "A Chef Server Account", 
            "guid": "/customer/11111/cmAccount/3610", 
            "label": "iconlightbulb", 
            "lastModifiedTimestamp": "2013-01-06T06:50:29.326+0000", 
            "name": "chef-cm", 
            "removable": true, 
            "status": "ACTIVE"
        }
    ]
}
"""
