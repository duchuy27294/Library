from abc import abstractmethod
from Status import NetzteilStatus
from Instrument.Instrument import Instrument

class Netzteil(Instrument):
    def __init__(self):
        pass

    @abstractmethod
    def get_voltage(self) -> float:
        pass

    @abstractmethod
    def get_current(self) -> float:
        pass

    @abstractmethod
    def set_voltage(self,value:float):
        pass

    @abstractmethod
    def set_current(self,value:float):
        pass

    @abstractmethod
    def get_max_voltage(self)->float:
        pass

    @abstractmethod
    def get_max_current(self)->float:
        pass
    
    @abstractmethod
    def set_status(self,status:NetzteilStatus):
        pass

    @abstractmethod
    def get_status(self)->NetzteilStatus:
        pass

    @abstractmethod
    def turnOn(self):
        pass

    @abstractmethod
    def turnOff(self):
        pass

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def resume(self):
        pass