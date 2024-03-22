from PyQt5 import QtGui

class InvalidNumber(ValueError):
    def __init__(self, _type):
        self.type = _type
