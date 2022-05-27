#####################################################################
try:
    from .DCNetzteilAutomation import DCNetzteilAutomation
    from .VoltageAutomation import VoltageAutomation
    from .CurrentAutomation import CurrentAutomation
except (ModuleNotFoundError,ImportError):
    from DCNetzteilAutomation import DCNetzteilAutomation
    from VoltageAutomation import VoltageAutomation
    from CurrentAutomation import CurrentAutomation