import time

# TODO: refactor this out as it creates a circular import issue
def wait_for_job(job_id, status='COMPLETE'):
    from mixcoatl.admin import job
    j = job.get(job_id)
    initial_status = j['status']
    if initial_status == 'ERROR':
        return False
    while job.get(job_id)['status'] != status:
        time.sleep(5)
        j = job.get(job_id)
        if j['status'] == 'ERROR':
            return False
        else:
            continue

    return True

def uncamel(str):
    import re
    s = lambda str: re.sub('(((?<=[a-z])[A-Z])|([A-Z](?![A-Z]|$)))', '_\\1', str).lower().strip('_')
    return s(str)

def uncamel_keys(d1):
    d2 = dict()
    if not isinstance(d1, dict):
        return d1
    for k,v in d1.iteritems():
        new_key = uncamel(k)
        if isinstance(v, dict):
            d2[new_key] = uncamel_keys(v)
        elif isinstance(v, list):
            d2[new_key] = [uncamel_keys(item) for item in v]
        else:
            d2[new_key] = v
    return d2

def camelize(str):
    s = ''.join([t.title() for t in str.split('_')])
    return s[0].lower()+s[1:]

def camel_keys(d1):
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

def convert(input):
    if isinstance(input, dict):
        return dict((convert(key), convert(value)) for key, value in input.iteritems())
    elif isinstance(input, list):
        return [convert(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input