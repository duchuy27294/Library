from SuperSignal.SuperSignal import SignalAlreadyExist


try:
    from .SuperSignal import SuperSignal
    from ..MathSignal import *
except (ModuleNotFoundError,ImportError):
    from SuperSignal import SuperSignal
    from MathSignal import *

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
