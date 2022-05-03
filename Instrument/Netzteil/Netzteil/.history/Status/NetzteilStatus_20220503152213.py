from __future__ import annotations
from abc import abstractmethod
from Netzteil import Netzteil

class NetzteilStatus(object):
    def __init__(self,netzteil:Netzteil):
        self._netzteil = netzteil

    @abstractmethod
    def turnOn(self)->Status:
        pass

    @abstractmethod
    def turnOff(self)->Status:
        pass

    @abstractmethod
    def connect(self)->Status:
        pass

    @abstractmethod
    def disconnect(self)->Status:
        pass

    @abstractmethod
    def run(self)->Status:
        pass

    @abstractmethod
    def pause(self)->Status:
        pass

    @abstractmethod
    def stop(self)->Status:
        pass
    
        