from abc import abstractmethod
from Instrument.Instrument import Instrument

class Netzteil(Instrument):
    def __init__(self,min_voltage,min_current,max_voltage,max_current):
        self.__min_voltage = min_voltage
        self.__min_current = min_current
        self.__max_current = max_current
        self.__max_voltage = max_voltage

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

    @abstractmethod
    def get_voltage(self):
        pass

    @abstractmethod
    def set_voltage(self,value):
        pass

    @abstractmethod
    def get_current(self):
        pass

    @abstractmethod
    def set_current(self,value):
        pass

    def get_min_voltage(self):
        return self.__min_voltage

    def get_min_current(self):
        return self.__min_current

    def get_max_voltage(self):
        return self.__max_voltage

    def get_max_current(self):
        return self.__max_current