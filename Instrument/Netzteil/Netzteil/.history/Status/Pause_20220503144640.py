from Status import Status
from Working import Working
from On import On
from Off import Off
from Disconnected import Disconnected
from Netzteil import Netzteil

class Pause(Status):
    def __init__(self,netzteil:Netzteil):
        super().__init__(netzteil)

    def turnOn(self)->Status:
        return self

    def turnOff(self)->Status:
        off = Off(self._netzteil)
        self._netzteil.set_status(off)
        return off

    def connect(self)->Status:
        return self

    def disconnect(self)->Status:
        self.turnOff()
        return self._netzteil.get_status().disconnect()

    def run(self)->Status:
        return self

    def pause(self)->Status:
        return self

    def stop(self)->Status:
        on = On(self._netzteil)
        self._netzteil.set_status(on)
        return on

    def resume(self)->Status:
        working = Working(self._netzteil)
        self._netzteil.set_status(working)
        return working