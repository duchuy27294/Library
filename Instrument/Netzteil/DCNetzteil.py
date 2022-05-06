from abc import abstractmethod
from Netzteil.DCNetzteilInterface import DCNetzteilInterface
from DCNetzteilStatus import *
from DCNetzteilAutomation.DCNetzteilAutomation import DCNetzteilAutomation

class DCNetzteil(DCNetzteilInterface):
    count:int = 0

    def __init__(self,name = 'DCNetzteil', max_voltage = 20.0, max_current = 20.0):
        super().__init__(max_voltage = max_voltage,max_current = max_current)
        self.__name = name 
        self.__status = Off(self)
        self.__voltageAutomation = DCNetzteilAutomation(netzteil = self,type = 'voltage')
        self.__currentAutomation = DCNetzteilAutomation(netzteil = self,type = 'current')
        DCNetzteil.count += 1

    @classmethod
    def getCount(cls):
        return DCNetzteil.count
    
    def get_name(self)->str:
        return self.__name

    def set_name(self,name:str):
        self.__name = name
    
    def getVoltageAutomation(self)->DCNetzteilAutomation:
        return self.__voltageAutomation

    def getCurrentAutomation(self)->DCNetzteilAutomation:
        return self.__currentAutomation

    def get_max_voltage(self)->float:
        return self.__max_voltage

    def get_max_current(self)->float:
        return self.__max_current

    @abstractmethod
    def set_status(self,status:DCNetzteilStatus):
        pass

    def get_status(self):
        return self.__status

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
    def get_instrument(self):
        pass

    


