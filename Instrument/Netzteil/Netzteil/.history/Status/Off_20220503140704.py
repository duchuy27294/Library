from Status import Status
from Disconnected import Disconnected
from Netzteil import Netzteil

class Off(Status):
    def __init__(self,netzteil:Netzteil):
        super().__init__(netzteil)

    def turnOn(self)->Status:
        on = On(self._netzteil)
        self._netzteil.set_status(on)
        return (on)

    def turnOff(self)->Status:
        return self

    def connect(self)->Status:
        return self

    def disconnect(self)->Status:
        disconnected = Disconnected(self._netzteil)
        self._netzteil.set_status(disconnected)
        return disconnected

    def run(self)->Status:
        return self

    def pause(self)->Status:
        return self

    def stop(self)->Status:
        return self