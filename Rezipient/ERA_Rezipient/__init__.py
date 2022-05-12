try:
    from .ERA_Rezipient_Interface import ERA_Rezipient_Interface
    from .Dummy_ERA_Rezipient import Dummy_ERA_Rezipient
    from .ERA_Rezipient import ERA_Rezipient
except (ModuleNotFoundError,ImportError):
    from ERA_Rezipient_Interface import ERA_Rezipient_Interface
    from Dummy_ERA_Rezipient import Dummy_ERA_Rezipient
    from ERA_Rezipient import ERA_Rezipient