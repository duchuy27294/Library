from __future__ import annotations
from abc import ABC,abstractmethod

class Status(ABC):
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
    def resume(self)->Status:
        pass