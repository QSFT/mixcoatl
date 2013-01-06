all_items = """
{
    "loadBalancers": [
        {
            "address": "Keith-LB.us-west-2.elb.amazonaws.com", 
            "budget": 10287, 
            "cloud": {
                "cloudId": 1
            }, 
            "cnameBased": true, 
            "customer": {
                "customerId": 11111
            }, 
            "description": "Keith-LB", 
            "loadBalancerId": 10924, 
            "name": "Keith-LB", 
            "owningAccount": {
                "accountId": 16000
            }, 
            "providerId": "Keith-LB", 
            "region": {
                "regionId": 19344
            }, 
            "status": "ACTIVE"
        }, 
        {
            "address": "wordpress-deployment.us-west-2.elb.amazonaws.com", 
            "budget": 10287, 
            "cloud": {
                "cloudId": 1
            }, 
            "cnameBased": true, 
            "customer": {
                "customerId": 11111
            }, 
            "description": "Cloud Load Balancer for wordpress demo deployment", 
            "loadBalancerId": 12516, 
            "name": "wordpress-deployment", 
            "owningAccount": {
                "accountId": 16000
            }, 
            "owningGroups": [
                {
                    "groupId": 9465
                }
            ], 
            "owningUser": {
                "userId": 12345
            }, 
            "providerId": "wordpress-deployment", 
            "region": {
                "regionId": 19344
            }, 
            "status": "ACTIVE"
        }
    ]
}
"""

one_item = """
{
    "loadBalancers": [
        {
            "address": "wordpress-deployment.us-west-2.elb.amazonaws.com", 
            "budget": 10287, 
            "cloud": {
                "cloudId": 1
            }, 
            "cnameBased": true, 
            "customer": {
                "customerId": 11111
            }, 
            "description": "Cloud Load Balancer for wordpress demo deployment", 
            "loadBalancerId": 12516, 
            "name": "wordpress-deployment", 
            "owningAccount": {
                "accountId": 16000
            }, 
            "owningGroups": [
                {
                    "groupId": 9465
                }
            ], 
            "owningUser": {
                "userId": 12345
            }, 
            "providerId": "wordpress-deployment", 
            "region": {
                "regionId": 19344
            }, 
            "status": "ACTIVE"
        }
    ]
}
"""
