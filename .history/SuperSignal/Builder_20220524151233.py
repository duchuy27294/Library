try:
    from .SuperSignal import *
    from ..MathSignal import *
except (ModuleNotFoundError,ImportError):
    from SuperSignal import *
    from MathSignal import *
from typing import List

class Builder(object):
    def __init__(self,signal:SuperSignal = None):
        self.__signal = signal

    def add(self,signal:MathSignal):
        try:
            self.__signal.add(signal)
        except SignalAlreadyExist:
            pass
        return self

    def remove(self,signal:MathSignal):
        try:
            self.__signal.remove(signal)
        except SignalNotExist:
            pass
        return self

    def generate(self):

