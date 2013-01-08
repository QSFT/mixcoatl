#!/usr/bin/env python

import json
import sys
import pprint
sys.path.append('../mixcoatl')
from mixcoatl import resource

# Usage examples (uses normal ES_* env vars for mixcoatl):
# --------------------------------------------------------
# bin/dump.py infrastructure/Server
# bin/dump.py infrastructure/Server "{}" basic
# bin/dump.py infrastructure/Server "{'regionId':12345}"
# bin/dump.py infrastructure/Server/12345 "{}" basic

# Yes I should have used optparse....
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
if params is None:
    z = r.get()
else:
    z = r.get(params=params)

output = sys.stdout
headers = r.last_request.headers
data = json.loads(r.last_request.content)
#print('HEADERS\n-------\n')
#pprint.pprint(headers)
#print('\nRESPONSE\n--------\n')
json.dump(data, output, sort_keys=True, indent=2)
output.write('\n')

