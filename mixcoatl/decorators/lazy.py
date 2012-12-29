def lazy(**dargs):
    """
    Class decorator for lazy loading attribute
    """

    def decorator(cls):
        cls.primary_key = dargs['key']
        orig_init = cls.__init__
        def wrapped_init(self, *args, **kwargs):
            self.primary_key = cls.primary_key
            if not ('load' in dir(self)):
                raise Exception("Lazy decorated classes must implement load()")
            orig_init(self, *args, **kwargs)

        def wrapped__getattr__(self, item):
            if item == getattr(self, cls.primary_key):
                pass
            else:
                return __lazyload(self, item)

        def __lazyload(self, attr):
            if self.__dict__.has_key(attr):
                pass
            elif self.__dict__.has_key('loaded'):
                pass
            elif getattr(self, cls.primary_key) is not None:
                self.load()
            else:
                try:
                    return self.__dict__[attr]
                except KeyError:
                    raise AttributeError("%r object has no attribute %r" %
                                            (type(self).__name__, attr))
        cls.__getattr__ = wrapped__getattr__
        cls.__init__ = wrapped_init
        return cls
    return decorator
