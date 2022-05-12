try:
    from .Netzteil import Netzteil
    from .DCNetzteilInterface import DCNetzteilInterface
    from .DCNetzteil import DCNetzteil
    from .DummyNetzteil import *
except (ModuleNotFoundError,ImportError):
    from Netzteil import Netzteil
    from DCNetzteilInterface import DCNetzteilInterface
    from DCNetzteil import DCNetzteil
    from DummyNetzteil import *