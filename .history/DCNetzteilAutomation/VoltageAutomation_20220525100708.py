from re import L


try:
    from .DCNetzteilAutomation import DCNetzteilAutomation
    from ..SuperSignal import *
except (ModuleNotFoundError,ImportError):
    from DCNetzteilAutomation import DCNetzteilAutomation
    from SuperSignal import *

class VoltageAutomation(DCNetzteilAutomation):
    def __init__(self,netzteil,signal:SuperSignal = None)