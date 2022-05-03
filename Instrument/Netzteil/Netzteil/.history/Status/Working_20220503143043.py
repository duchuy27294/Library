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
        off = Off(self._netzteil)
        self._netzteil.set_status(off)
        return self._netzteil.get_status().disconnect()

    def run(self)->Status:
        working = Working(self._netzteil)
        self._netzteil.set_status(working)
        self._netzteil.run()
        return working

    def pause(self)->Status:
        return self

    def stop(self)->Status:
        return self