#####################################################################
try:
    from .DCNetzteilAutomation import DCNetzteilAutomation
    from .VoltageAutomation import VoltageAutomage
except (ModuleNotFoundError,ImportError):
    from DCNetzteilAutomation import DCNetzteilAutomation
    from VoltageAutomation import VoltageAutomation