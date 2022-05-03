from abc import abstractmethod
from Status.Status import Status
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
    def set_status(self,status:Status):
        pass

    @abstractmethod
    def get_status(self)->Status:
        pass