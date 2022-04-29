from abc import abstractmethod
from Netzteil.Netzteil import Netzteil
from Netzteil.Status import Status
from Netzteil.Automation import Automation

class DCNetzteil(Netzteil):
    count:int = 0

    def __init__(self,name = 'DCNetzteil', max_voltage = 20.0, max_current = 20.0):
        self.__name = name 
        self.__max_voltage = max_voltage
        self.__max_current = max_current
        self.__status = Status.OFF
        self.__voltageAutomation = Automation(netzteil = self,log = self.__name + '_voltage.csv',type = 'voltage')
        self.__currentAutomation = Automation(netzteil = self,log = self.__name + '_current.csv',type = 'current')
        DCNetzteil.count += 1

    @classmethod
    def getCount(cls):
        return DCNetzteil.count
    
    def get_name(self)->str:
        return self.__name

    def set_name(self,name:str):
        self.__name = name
        self.__voltageAutomation.setLog(self.__name + '_voltage.csv')
        self.__currentAutomation.setLog(self.__name + '_current.csv')
    
    def getVoltageAutomation(self)->Automation:
        return self.__voltageAutomation

    def getCurrentAutomation(self)->Automation:
        return self.__currentAutomation

    def get_max_voltage(self)->float:
        return self.__max_voltage

    def get_max_current(self)->float:
        return self.__max_current

    def get_status(self):
        return self.__status

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
    def set_status(self,status:Status):
        pass

    @abstractmethod
    def get_instrument(self):
        pass



