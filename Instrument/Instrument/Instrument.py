from abc import ABC,abstractmethod

class Instrument(ABC):

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

    