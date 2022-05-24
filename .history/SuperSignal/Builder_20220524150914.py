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
        self.__signal.add(signal)