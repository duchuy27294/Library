try:
    from .SuperSignal import *
    from ..MathSignal import *
except (ModuleNotFoundError,ImportError):
    from SuperSignal import *
    from MathSignal import *
from typing import List
import numpy as np

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
    
    def getSignal(self):
        return self.__signal

    def generate(self):
        duration = self.__signal.getDuration()
        t = 

