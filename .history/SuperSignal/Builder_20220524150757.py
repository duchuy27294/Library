try:
    from .SuperSignal import SuperSignal
except (ModuleNotFoundError,ImportError):
    from SuperSignal import SuperSignal

class Builder(object):
    def __init__(self,signal:SuperSignal = None):
        self.__signal:SuperSignal = None
        if (signal is not None):
            self.__signal = signal