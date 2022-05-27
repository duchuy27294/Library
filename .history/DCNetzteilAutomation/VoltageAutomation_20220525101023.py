try:
    from .DCNetzteilAutomation import DCNetzteilAutomation
    from ..SuperSignal import *
except (ModuleNotFoundError,ImportError):
    from DCNetzteilAutomation import DCNetzteilAutomation
    from SuperSignal import *

class VoltageAutomation(DCNetzteilAutomation):
    def __init__(self,netzteil,signal:SuperSignal = None):
        super().__init__(netzteil = netzteil, signal = signal)

    def do(self):
        self._netzteil.set_voltage(self._constantSignal[self._currentIndex].getValue())
        self._currentIndex += 1
        if self._currentIndex >= len(self._constantSignal):
            self._currentIndex = 0