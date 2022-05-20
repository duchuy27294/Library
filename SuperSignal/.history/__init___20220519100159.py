try:
    from .MathSignal import *
    from .SuperSignal import *
except (ModuleNotFoundError,ImportError):
    from MathSignal import *
    from SuperSignal import *