from Status import Status
from On import On
from Pause import Pause
from Off import Off
from Netzteil import Netzteil

class Working(Status):
    def __init__(self,netzteil:Netzteil):
        super().__init__(netzteil = netzteil)

    def turnOn(self)->Status:
        return self

    def turnOff(self)->Status:
        off = Off(self._netzteil)
        self._netzteil.set_status(off)
        return off

    def connect(self)->Status:
        return self

    def disconnect(self)->Status:
        return self

    def run(self)->Status:
        return self

    def pause(self)->Status:
        pause = Pause(self._netzteil)
        self._netzteil.set_status(pause)
        return pause

    def stop(self)->Status:
        on = On(self._netzteil)
        self._netzteil.set_status(on)
        return on