from Status import Status
from Off import Off
from Netzteil import Netzteil

class Disconnected(Status):
    def __init__(self,netzteil:Netzteil):
        super().__init__(netzteil = netzteil)

    def turnOn(self)->Status:
        return self

    def turnOff(self)->Status:
        return self

    def connect(self)->Status:
        return (Off(self._netzteil))

    def disconnect(self)->Status:
        return self

    def run(self)->Status:
        return self

    def pause(self)->Status:
        return self

    def stop(self)->Status:
        return self