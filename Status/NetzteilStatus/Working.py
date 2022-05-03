from NetzteilStatus import NetzteilStatus
from On import On
from Pause import Pause
from Off import Off
from Netzteil import Netzteil

class Working(NetzteilStatus):
    def __init__(self,netzteil:Netzteil):
        super().__init__(netzteil = netzteil)

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
        pause = Pause(self._netzteil)
        self.save()
        self._netzteil.set_status(pause)
        return pause

    def stop(self)->NetzteilStatus:
        on = On(self._netzteil)
        self._netzteil.set_status(on)
        return on

    def save(self):
        self._netzteil.save()