try:
    from .SuperSignal import *
    from .Builder import Builder
except (ModuleNotFoundError,ImportError):
    from SuperSignal import *
    from Builder import Builder