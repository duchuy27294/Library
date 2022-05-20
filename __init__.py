try:
    from .Automation import *
    from .DCNetzteilAutomation import *
    from .DCNetzteilStatus import *
    from .ERA_Rezipient import *
    from .Event import *
    from .Instrument import *
    from .MathSignal import *
    from .Netzteil import *
    from .Rezipient import *
    from .Status import *
    from .SuperSignal import *
except (ModuleNotFoundError,ImportError):
    from Automation import *
    from DCNetzteilAutomation import *
    from DCNetzteilStatus import *
    from ERA_Rezipient import *
    from Event import *
    from Instrument import *
    from MathSignal import *
    from Netzteil import *
    from Rezipient import *
    from Status import *
    from SuperSignal import *