from __future__ import annotations
from abc import abstractmethod
from Netzteil import Netzteil

class NetzteilStatus(object):
    def __init__(self,netzteil:Netzteil):
        self._netzteil = netzteil

    @abstractmethod
    def turnOn(self)->NetzteilStatus:
        pass

    @abstractmethod
    def turnOff(self)->NetzteilStatus:
        pass

    @abstractmethod
    def connect(self)->NetzteilStatus:
        pass

    @abstractmethod
    def disconnect(self)->NetzteilStatus:
        pass

    @abstractmethod
    def run(self)->NetzteilStatus:
        pass

    @abstractmethod
    def pause(self)->NetzteilStatus:
        pass

    @abstractmethod
    def stop(self)->NetzteilStatus:
        pass
    
        