#############################################
try:
    from .MathSignal import MathSignal
    from .CustomSignal import CustomSignal
    from .PeriodicSignal import *
except (ModuleNotFoundError,ImportError):
    from MathSignal import MathSignal
    from CustomSignal import CustomSignal
    from PeriodicSignal import *