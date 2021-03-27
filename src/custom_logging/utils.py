from functools import reduce


class NoDefaultProvided:
    """dummy class for getattrd"""

    pass


def getattrd(obj, name, default=NoDefaultProvided):
    """
    Same as getattr(), but allows dot notation lookup
    Discussed in: http://stackoverflow.com/questions/11975781
    """
    try:
        return reduce(getattr, name.split("."), obj)
    except AttributeError:
        if default != NoDefaultProvided:
            return default
        raise


def setattrd(obj, name, val):
    pre, _, post = name.rpartition(".")
    return setattr(getattrd(obj, pre, None) if pre else obj, post, val)
