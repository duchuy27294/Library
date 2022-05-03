from Status import Status
from Off import Off
from Disconnected import Disconnected
from Netzteil import Netzteil

class On(Status):
    def __init__(self,netzteil):
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
        self._netzteil.get_status().disconnect()
        return self._netzteil.get_status()

    def run(self)->Status:
        on = On(self._netzteil)
        self._netzteil.set_status(on)
        self._netzteil.run()
        return on

    def pause(self)->Status:
        return self

    def stop(self)->Status:
        return self