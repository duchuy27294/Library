from __future__ import annotations
from abc import abstractmethod
from Netzteil.DCNetzteilInterface import DCNetzteilInterface
from Status.Status import Status

class DCNetzteilStatus(Status):
    def __init__(self,netzteil:DCNetzteilInterface):
        self._netzteil = netzteil

    @abstractmethod
    def turnOn(self)->DCNetzteilStatus:
        pass

    @abstractmethod
    def turnOff(self)->DCNetzteilStatus:
        pass

    @abstractmethod
    def connect(self)->DCNetzteilStatus:
        pass

    @abstractmethod
    def disconnect(self)->DCNetzteilStatus:
        pass

    @abstractmethod
    def run(self)->DCNetzteilStatus:
        pass

    @abstractmethod
    def pause(self)->DCNetzteilStatus:
        pass

    @abstractmethod
    def stop(self)->DCNetzteilStatus:
        pass
    
        