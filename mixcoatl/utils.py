import json
#from prettytable import PrettyTable

"""Common helper utilities for use with mixcoatl"""

def print_format(data, payload_format):
    import dicttoxml

    if payload_format == "xml":
        return dicttoxml.dicttoxml(data)
    else:
        return json.dumps(data, sort_keys=True)

# Work in progress.  Dynamically generate PrettyTable from results. --Brian
# class PrintTable:
#     def __init__(self, results):
#         self.keys = []
#         self.print_table(results)

#     def find(self, lst, key, value):
#         for i, dic in enumerate(lst):
#             if dic[key] == value:
#                 return i
#         return -1

#     def print_table(self, results):
#         table = None
#         for r in results:
#             result = sorted(r.__dict__.iteritems())
#             keys = []
#             values = []
#             counter = 0
#             missing_key = None
#             missing_key_index = None

#             if table is None:
#                 for key, value in result:
#                     if '__' not in key:           
#                         self.keys.append(key)

#                 table = PrettyTable(self.keys)
#             else:
#                 for key, value in result:
#                     if '__' not in key:           
#                         keys.append(key)

#                 key_diffs = set(self.keys) - set(keys)
#                 for i in key_diffs:
#                     missing_key = i
#                     missing_key_index = self.keys.index(i)

#             for key, value in result:
#                 thevalue = None
#                 if '__' not in key:
#                     counter = counter + 1
#                     if key in self.keys:
#                         if isinstance(value, dict):
#                             for i in value:
#                                 thevalue = value[i]
#                         elif isinstance(value, list):
#                             for i in value[0]:
#                                 thevalue = value[0][i]
#                         else:
#                             if len(str(value)) > 0:
#                                 thevalue = value

#                         if thevalue is None or thevalue == "":
#                             thevalue = "N/A"
#                     else:
#                         #print "OUT: "+key
#                         thevalue = "N/A"

#                     if missing_key_index is not None:
#                         # print "Debug"
#                         # print missing_key_index
#                         # print counter
#                         # print "End Debug"
#                         if counter == missing_key_index:
#                             #print "Would add a value!"
#                             thevalue = "N/A"

#                     values.append(thevalue)
#                     print "Test ("+key+") -- ("+str(counter)+"): "+str(thevalue)

#             print "------"
#             # if len(values) == len(self.keys):
#             #     table.add_row(values)

#         table.align = 'l'
#         print table


def uncamel(val):
    """Return the snake case version of :attr:`str`

    >>> uncamel('deviceId')
    'device_id'
    >>> uncamel('dataCenterName')
    'data_center_name'
    """
    import re
    s = lambda val: re.sub('(((?<=[a-z])[A-Z])|([A-Z](?![A-Z]|$)))', '_\\1', val).lower().strip('_')
    return s(val)

def uncamel_keys(d1):
    """Return :attr:`d1` with all keys converted to snake case

    >>> d = {'myThings':[{'thingId':1,'someThings':{'firstThing':'a_thing'}}]}
    >>> uncamel_keys(d)
    {'my_things': [{'thing_id': 1, 'some_things': {'first_thing': 'a_thing'}}]}
    """
    d2 = dict()
    if not isinstance(d1, dict):
        return d1
    for k, v in d1.iteritems():
        new_key = uncamel(k)
        if isinstance(v, dict):
            d2[new_key] = uncamel_keys(v)
        elif isinstance(v, list):
            d2[new_key] = [uncamel_keys(item) for item in v]
        else:
            d2[new_key] = v
    return d2

def camelize(val):
    """Return the camel case version of a :attr:`str`

    >>> camelize('this_is_a_thing')
    'thisIsAThing'
    """
    s = ''.join([t.title() for t in val.split('_')])
    return s[0].lower()+s[1:]

def camel_keys(d1):
    """Return :attr:`d1` with all keys converted to camel case

    >>> b = {'my_things': [{'thing_id': 1, 'some_things': {'first_thing': 'a_thing'}}]}
    >>> camel_keys(b)
    {'myThings': [{'thingId': 1, 'someThings': {'firstThing': 'a_thing'}}]}
    """
    d2 = dict()
    if not isinstance(d1, dict):
        return d1
    for k, v in d1.iteritems():
        new_key = camelize(k)
        if isinstance(v, dict):
            d2[new_key] = camel_keys(v)
        elif isinstance(v, list):
            d2[new_key] = [camel_keys(item) for item in v]
        else:
            d2[new_key] = v
    return d2

def convert(val):
    """Return :attr:`input` converted from :class:`unicode` to :class:`str`

    >>> convert(u'bob')
    'bob'
    >>> convert([u'foo', u'bar'])
    ['foo', 'bar']
    >>> convert({u'foo':u'bar'})
    {'foo': 'bar'}
    """
    if isinstance(val, dict):
        return dict((convert(key), convert(value)) for key, value in val.iteritems())
    elif isinstance(val, list):
        return [convert(element) for element in val]
    elif isinstance(val, unicode):
        return val.encode('utf-8')
    else:
        return val
