class ValidationException(Exception): pass

def required_attrs(attrs):
    def wrapper(method):
        def validate(obj, *args, **kwargs):
            for ra in attrs:
                try:
                    if getattr(obj, ra) is None:
                        raise ValidationException('Required attribute "%s" is missing' % ra)
                except AttributeError:
                    raise ValidationException('Required attribute "%s" is missing' % ra)
            return method(obj, *args, **kwargs)
        return validate
    return wrapper

