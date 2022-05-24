######################################
try:
    from .PeriodicSignal import PeriodicSignal
    from .Sin import Sin
    from .Cos import Cos
except (ModuleNotFoundError,ImportError):
    from PeriodicSignal import PeriodicSignal
    from Sin import Sin
    from Cos import Cos