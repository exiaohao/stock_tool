__author__ = 'exiaohao@gmail.com'


def try_int(val):
    try:
        return int(val)
    except:
        return val


def try_float(val, to_int=True):
    try:
        if to_int and try_int(val) != val:
            return try_int(val)

        return float(val)

    except:
        return val
