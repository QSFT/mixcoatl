import json

"""Common helper utilities for use with mixcoatl"""


def print_format(data, payload_format):
    import dicttoxml

    newdata = []
    for i in data:
        thedict = {}
        for key, value in i.__dict__.iteritems():
            if '__' not in key:
                thedict[key] = value
        newdata.append(thedict)

    if payload_format == "xml":
        return dicttoxml.dicttoxml(newdata)
    elif payload_format == "csv":
        csv = ""
        for i in newdata[0].keys():
            csv += '"'+i.replace('"','\"')+'"'+","
        csv = csv.rstrip(",")

        for x in newdata:
            csv += "\n"
            for i in x:
                if isinstance(x[i], dict):
                    if x[i]:
                        csv += '"'+str(x[i][x[i].keys()[0]]).replace('"','\"')+'"'+","
                    else:
                        csv += '"",'
                else:
                    csv += '"'+str(x[i]).replace('"','\"')+'"'+","
            csv = csv.rstrip(",")

        return csv
    else:
        return json.dumps(newdata)


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
