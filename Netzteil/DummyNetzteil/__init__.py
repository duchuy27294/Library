try:
    from .DummyNetzteil import DummyNetzteil
    from .Tdk import Tdk
    from .Syskon import Syskon
except (ModuleNotFoundError,ImportError):
    from DummyNetzteil import DummyNetzteil
    from Tdk import Tdk
    from Syskon import Syskon
