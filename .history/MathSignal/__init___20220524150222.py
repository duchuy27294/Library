#############################################
try:
    from .MathSignal import *
    from .ConstantSignal import CustomSignal
    from .PeriodicSignal import *
except (ModuleNotFoundError,ImportError):
    from MathSignal import *
    from MathSignal.ConstantSignal import CustomSignal
    from PeriodicSignal import *