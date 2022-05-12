from DCNetzteilStatus.DCNetzteilStatus import DCNetzteilStatus
from DCNetzteilStatus.Working import Working
from DCNetzteilStatus.On import On
from DCNetzteilStatus.Off import Off
from DCNetzteilStatus.Disconnected import Disconnected
from Netzteil.Netzteil import Netzteil

class Pause(DCNetzteilStatus):
    def __init__(self,netzteil:Netzteil):
        super().__init__(netzteil)

    def turnOn(self)->DCNetzteilStatus:
        return self

    def turnOff(self)->DCNetzteilStatus:
        off = Off(self._netzteil)
        self._netzteil.set_status(off)
        return off

    def connect(self)->DCNetzteilStatus:
        return self

    def disconnect(self)->DCNetzteilStatus:
        self.turnOff()
        return self._netzteil.get_status().disconnect()

    def run(self)->DCNetzteilStatus:
        return self

    def pause(self)->DCNetzteilStatus:
        return self

    def stop(self)->DCNetzteilStatus:
        on = On(self._netzteil)
        self._netzteil.set_status(on)
        return on

    def resume(self)->DCNetzteilStatus:
        working = Working(self._netzteil)
        self._netzteil.set_status(working)
        return working