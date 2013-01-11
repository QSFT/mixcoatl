from functools import wraps

def required_attrs(attrs):
    """decorator for marking a list of attributes required before calling a function

    :param attrs: List of attributes that must be set
    :type attrs: list.
    :raises: `ValidationException`
    """
    def wrapper(method):
        @wraps(method)
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

class ValidationException(Exception): pass