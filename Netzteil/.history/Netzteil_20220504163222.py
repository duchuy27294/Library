from abc import abstractmethod
from NetzteilStatus.NetzteilStatus import NetzteilStatus
from Instrument.Instrument import Instrument

class Netzteil(Instrument):
    def __init__(self):
        pass

    @abstractmethod
    def get_status(self):
        pass

    @abstractmethod
    def set_status(self,status):
        pass

    @abstractmethod
    def turnOn(self):
        pass

    @abstractmethod
    def turnOff(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def pause(self):
        pass

    @abstractmethod
    def stop(self):
        pass