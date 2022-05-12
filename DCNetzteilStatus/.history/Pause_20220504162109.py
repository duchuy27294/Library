from NetzteilStatus.NetzteilStatus import NetzteilStatus
from NetzteilStatus.Working import Working
from NetzteilStatus.On import On
from NetzteilStatus.Off import Off
from NetzteilStatus.Disconnected import Disconnected
from Netzteil.Netzteil import Netzteil

class Pause(NetzteilStatus):
    def __init__(self,netzteil:Netzteil):
        super().__init__(netzteil)

    def turnOn(self)->NetzteilStatus:
        return self

    def turnOff(self)->NetzteilStatus:
        off = Off(self._netzteil)
        self._netzteil.set_status(off)
        return off

    def connect(self)->NetzteilStatus:
        return self

    def disconnect(self)->NetzteilStatus:
        self.turnOff()
        return self._netzteil.get_status().disconnect()

    def run(self)->NetzteilStatus:
        return self

    def pause(self)->NetzteilStatus:
        return self

    def stop(self)->NetzteilStatus:
        on = On(self._netzteil)
        self._netzteil.set_status(on)
        return on

    def resume(self)->NetzteilStatus:
        working = Working(self._netzteil)
        self._netzteil.set_status(working)
        return working