from NetzteilStatus import NetzteilStatus
from Off import Off
from Instrument.Netzteil import Netzteil

class Disconnected(NetzteilStatus):
    def __init__(self,netzteil:Netzteil):
        super().__init__(netzteil = netzteil)

    def turnOn(self)->NetzteilStatus:
        return self

    def turnOff(self)->NetzteilStatus:
        return self

    def connect(self)->NetzteilStatus:
        off = Off(self._netzteil)
        self._netzteil.set_status(off)
        return (off)

    def disconnect(self)->NetzteilStatus:
        return self

    def run(self)->NetzteilStatus:
        return self

    def pause(self)->NetzteilStatus:
        return self

    def stop(self)->NetzteilStatus:
        return self