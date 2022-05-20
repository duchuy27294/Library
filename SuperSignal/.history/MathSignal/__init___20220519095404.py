try:
    from .MathSignal import *
    from .ConstantSignal import ConstantSignal
    from .PeriodicSignal import *
except (ModuleNotFoundError,ImportError):
    from MathSignal import *
    from ConstantSignal import ConstantSignal
    from PeriodicSignal import *