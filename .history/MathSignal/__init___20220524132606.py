#############################################
try:
    from .MathSignal import *
    from .CustomSignal import CustomSignal
    from .PeriodicSignal import *
except (ModuleNotFoundError,ImportError):
    from MathSignal import *
    from CustomSignal import CustomSignal
    from PeriodicSignal import *