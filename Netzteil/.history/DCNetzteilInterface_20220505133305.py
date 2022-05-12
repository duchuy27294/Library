from Netzteil.Netzteil import Netzteil
from abc import abstractmethod
from DCNetzteilStatus.DCNetzteilStatus import DCNetzteilStatus

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

    @abstractmethod
    def set_status(self,status:DCNetzteilStatus):
        pass

    @abstractmethod
    def get_status(self)->DCNetzteilStatus:
        pass

    @abstractmethod
    def getVoltageAutomation(self):
        pass

    @abstractmethod
    def getCurrentAutomation(self):
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
    def resume(self):
        pass

    @abstractmethod
    def pause(self):
        pass