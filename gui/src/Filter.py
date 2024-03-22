from gui.src.Exceptions import *


def check_float(string, _type: str):
    try:
        tmp = float(string)
        return tmp
    except ValueError:
        raise InvalidNumber(_type)


def check_int(string, _type: str):
    try:
        tmp = int(string)
        return tmp
    except ValueError:
        raise InvalidNumber(_type)

