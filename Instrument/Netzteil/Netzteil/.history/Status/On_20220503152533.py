from NetzteilStatus import NetzteilStatus
from Off import Off
from Working import Working
from Netzteil import Netzteil

class On(NetzteilStatus):
    def __init__(self,netzteil):
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
        off = Off(self._netzteil)
        self._netzteil.set_status(off)
        return self._netzteil.get_status().disconnect()

    def run(self)->NetzteilStatus:
        working = Working(self._netzteil)
        self._netzteil.set_status(working)
        self._netzteil.run()
        return working

    def pause(self)->NetzteilStatus:
        return self

    def stop(self)->NetzteilStatus:
        return self