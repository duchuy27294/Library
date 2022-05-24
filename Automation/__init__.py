############################################################
try:
    from .Automation import Automation
except (ModuleNotFoundError,ImportError):
    from Automation import Automation