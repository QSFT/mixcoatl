class lazy_property(object):
    def __init__(self, func):
        self._func = func
        self.__name__ = func.__name__
        self.__doc__ = func.__doc__

    def __get__(self, obj, klass=None):
        myname = self.__name__
        if obj is None: return self
        if obj.__dict__.has_key('loaded'):
            if myname in dir(obj):
                # load() will have already populated
                # so we defer
                return self._func(obj)
            else:
                raise AttributeError("%r object has no attribute %r" %
                                     (type(obj).__name__, self.__name__))
        elif obj.__dict__.has_key(self.__name__):
            return getattr(obj, self.__name__)
        else:
            if getattr(obj, obj.primary_key) is not None:
                try:
                    obj.load()
                    val = getattr(obj, '_'+obj.__class__.__name__+'__'+myname)
                except AttributeError:
                    if obj.last_error is not None:
                        return obj.last_error
                    else:
                        raise AttributeError("%r object has no attribute %r" %
                                         (type(obj).__name__, self.__name__))
            else:
                val = None

            setattr(obj, myname, val)
            return val
