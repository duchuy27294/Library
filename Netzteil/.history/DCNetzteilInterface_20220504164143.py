from Netzteil.Netzteil import Netzteil
from abc import abstractmethod
from NetzteilStatus.NetzteilStatus import NetzteilStatus

class DCNetzteilInterface(Netzteil):
    def __init__(self,max_voltage:float,max_current:float):
        super().__init__(min_voltage = 0,min_current = 0, max_voltage = max_voltage, max_current = max_current)

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

    def get_min_voltage(self)->float:
        return 0.0

    def get_min_current(self)->float:
        return 0.0

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