from abc import abstractmethod
from .DCNetzteilInterface import DCNetzteilInterface
from ..DCNetzteilStatus.DCNetzteilStatus import * 

class DCNetzteil(DCNetzteilInterface):
    count:int = 0

    def __init__(self,name = 'DCNetzteil', max_voltage = 20.0, max_current = 20.0):
        super().__init__(max_voltage = max_voltage,max_current = max_current)
        self.__name = name 
        self.__on = On(self)
        self.__off = Off(self)
        # self.__disconnected = Disconnected(self)
        self.__working = Working(self)
        self.__pause = Pause(self) 
        self.__status = self.__off
        self.__observer = []
        DCNetzteil.count += 1

    @classmethod
    def getCount(cls):
        return DCNetzteil.count
    
    def get_name(self)->str:
        return self.__name

    def set_name(self,name:str):
        self.__name = name


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

    # @abstractmethod
    # def connect(self):
    #     pass

    # @abstractmethod
    # def disconnect(self):
    #     pass

    # @abstractmethod
    # def save(self):
    #     pass

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

    def isOn(self):
        return (self.__status == self.__on)

    def isOff(self):
        return (self.__status == self.__off)

    # def isDisconnected(self):
    #     return (self.__status == self.__disconnected)

    # def isConnected(self):
    #     return (not (self.__status == self.__disconnected))

    def isWorking(self):
        return (self.__status == self.__working)

    def isPause(self):
        return (self.__status == self.__pause)

    def getOn(self):
        return self.__on

    def getOff(self):
        return self.__off

    def getDisconnected(self):
        return self.__disconnected
    
    def getWorking(self):
        return self.__working

    def getPause(self):
        return self.__pause

    def show(self):
        pass

    def add(self,observer):
        if (observer not in self.__observer):
            self.__observer.append(observer)

    def remove(self,observer):
        if (observer in self.__observer):
            self.__observer.remove(observer)

    def getObserver(self,index):
        try:
            return self.__observer[index]
        except IndexError:
            return None

    def getObservers(self):
        return self.__observer

    def notify(self):
        for observer in self.__observer:
            observer.update(self)

    



