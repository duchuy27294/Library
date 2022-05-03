from Status import Status
from Netzteil import Netzteil

class Disconnected(Status):
    def __init__(self,netzteil:Netzteil):
        super().__init__(netzteil = netzteil)

    def turnOn(self)->Status:
        return self

    def turnOff(self)->Status:
        return self

    def connect(self)->Status:
        return (Off(self.netzteil))

    @abstractmethod
    def disconnect(self)->Status:
        pass

    @abstractmethod
    def run(self)->Status:
        pass

    @abstractmethod
    def pause(self)->Status:
        pass

    @abstractmethod
    def stop(self)->Status:
        pass