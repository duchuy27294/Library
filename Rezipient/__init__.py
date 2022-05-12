try:
    from .Rezipient import Rezipient
    from .ERA_Rezipient import *
except (ModuleNotFoundError,ImportError):
    from Rezipient import Rezipient
    from ERA_Rezipient import *