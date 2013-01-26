class LazyPropertyException(BaseException): pass

class lazy_property(object):
    """decorator for marking an attribute as lazy loaded

    When using the `@lazy_property` decorator, the subsequent function is
    in essence made a property that is lazily loaded.

    In practice, all attributes of a given resource should be lazy except
    the resource's id. This ensures that simply instantiating a resource will
    not cause an expensive API call to be made.

    .. note::

        * lazy properties adhere to the descriptor protocol
        * Classes with lazy properties will need to implement a `load()` function
        * Once any lazy property is loaded, **ALL** lazy properties in the instance are loaded as a result of the API call.
        * Once all lazy properties are loaded, no further API calls will be made for the current instance.

    :raises: :class:`LazyPropertyException`
    """
    def __init__(self, func=None):
        self._func = func
        self.__doc__ = func.__doc__
        self.__name__ = func.__name__
        self._sfunc = None

    def __get__(self, instance, owner=None):
        myname = self.__name__

        if instance is None: return self

        if self._func is None:
            raise AttributeError, "unknown attribute %s" % myname
        # Check if we've already loaded from API
        if 'loaded' in instance.__dict__:
            if myname in dir(instance):
                return self._func(instance)
            else:
                raise AttributeError, "unknown attribute %s" % myname
        elif myname in instance.__dict__:
            return self._func(instance)
        else:
            if getattr(instance, instance.PRIMARY_KEY) is not None:
                try:
                    instance.load()
                except AttributeError as detail:
                    if instance.last_error is not None:
                        return instance.last_error
                    else:
                        raise LazyPropertyException(detail)

        return self._func(instance)

    def __set__(self, instance, value):
        if self._sfunc is None:
            raise TypeError, "immutable attribute: %s" % self.__name__
        else:
            try:
                old_val = getattr(instance, self.__name__)
            except AttributeError:
                # This is okay in cases where we're instantiating a new resource
                old_val = None
            instance.track_change(self.__name__, old_val, value)
            self._sfunc(instance, value)

    def setter(self, sfunc):
        self._sfunc = sfunc
        return self
