from abc import abstractmethod
from NetzteilStatus.NetzteilStatus import NetzteilStatus
from Instrument.Instrument import Instrument

class Netzteil(Instrument):

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

    @abstractmethod
    def get_min_voltage(self):
        pass

    @abstractmethod
    def get_min_current(self):
        pass

    @abstractmethod
    def get_max_voltage(self):
        pass

    @abstractmethod
    def get_max_current(self):
        pass