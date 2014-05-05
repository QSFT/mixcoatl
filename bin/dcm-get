#!/usr/bin/env python

import json
import sys
import pprint
sys.path.append('../mixcoatl')
from mixcoatl import resource

# Usage examples
# --------------------------------------------------------
# dcm-get.py infrastructure/Server
# dcm-get.py infrastructure/Server "{}" basic
# dcm-get.py infrastructure/Server "{'regionId':12345}"
# dcm-get.py infrastructure/Server/12345 "{}" basic

if len(sys.argv) < 2:
    sys.exit('Usage: %s basepath <optional query params dict> [basic|extended]' % sys.argv[0])

basepath = sys.argv[1]
if len(sys.argv) == 3:
    params = eval(sys.argv[2])
else:
    params = None

if len(sys.argv) == 4:
    params = eval(sys.argv[2])
    details = sys.argv[3]
else:
    details = 'extended'

r = resource.Resource(basepath)
r.request_details = details
if params is not None:
    qparms = params
else:
    qparms = {}
z = r.get(params=qparms)

output = sys.stdout
headers = r.last_request.headers
data = json.loads(r.last_request.content)
#print('HEADERS\n-------\n')
#pprint.pprint(headers)
#print('\nRESPONSE\n--------\n')
json.dump(data, output, sort_keys=True, indent=2)
output.write('\n')
