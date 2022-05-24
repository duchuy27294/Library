try:
    from .Observable import Observable
    from .Observer import Observer
except (ModuleNotFoundError,ImportError):
    from Observable import Observable
    from Observer import Observer
    