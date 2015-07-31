import json
import xmltodict
"""Common helper utilities for use with mixcoatl"""

def to_csv(data):
    """Formats a list of dictionaries into a CSV

    :param data: a list of dictionaries
    :returns str: a str formatted in csv

    .. warning::

        A python dictionary object can't be fully represented in in csv form. Hence, the result returned will
        contain cells that have a text representation of a sub elements.
    """
    csv = ""
    for i in data[0].keys():
        csv += '"'+i.replace('"','\"')+'"'+","
    csv = csv.rstrip(",")

    for x in data:
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

def print_format(data, payload_format):
    """Format the public instance variables of list of objects into either json, xml or csv . The contents of `__dict__`
    including those instance variables that are name mangled using __

    :param data: a list object to be formatted
    :param str payload_format: the the format that should be returned, either "json","xml","csv"
    :returns str: formatted string
    """


    newdata = []
    for i in data:
        thedict = {}
        for key, value in i.__dict__.iteritems():
            if '__' not in key:
                thedict[key] = value
        newdata.append(thedict)

    if payload_format == "xml":
        return "%s %s %s"% ('<?xml version="1.0" ?><root>',
                            xmltodict.unparse({"item":newdata}, full_document=False),
                            '</root>')
    elif payload_format == "csv":
        return to_csv(newdata)
    else:
        return json.dumps(newdata, indent=4, sort_keys=True)


def format_dict(thedict, payload_format):
    """Format a dictionary into json, xml, or csv and return a string

    :param dict thedict: dictionary to be formatted
    :param str payload_format: the format to return either "json", "xml", or "csv"
    :returns str: formatted string
    """


    if payload_format == "json":
        return json.dumps(thedict, indent=4, sort_keys=True)
    elif payload_format == "xml":
        return "%s %s %s"% ('<?xml version="1.0" ?><root>',
                            xmltodict.unparse({"item":thedict}, full_document=False),
                            '</root>')
    elif payload_format == "csv":
        return to_csv([thedict])
    else:
        raise ValueError("Unknown format requested, use payload_format json, xml, csv")


def add_argparse_output_formats(parser):
    """Add the supported cli output formats to the :attr:`parser` ArgumentParser object. Flags added are:
    `--json --xml --csv`

    :param ArgumentParser parser: object parser to append flags to"""

    parser.add_argument('--json', dest='format', action='store_const', const='json',
                        help='print API response in JSON format.')
    parser.add_argument('--xml', dest='format', action='store_const', const='xml',
                    help='print API response in XML format.')
    parser.add_argument('--csv', dest='format', action='store_const', const='csv',
                    help='print API response in CSV format.')


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
