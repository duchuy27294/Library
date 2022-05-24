##############################################################
try:
    from .Instrument import Instrument
except (ModuleNotFoundError,ImportError):
    from Instrument import Instrument