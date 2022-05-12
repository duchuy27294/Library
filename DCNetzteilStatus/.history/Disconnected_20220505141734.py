from DCNetzteilStatus.DCNetzteilStatus import DCNetzteilStatus
from DCNetzteilStatus.Off import Off
from Netzteil.DCNetzteilInterface import DCNetzteilInterface

class Disconnected(DCNetzteilStatus):
    def __init__(self,netzteil):
        super().__init__(netzteil = netzteil)

    def turnOn(self)->DCNetzteilStatus:
        return self

    def turnOff(self)->DCNetzteilStatus:
        return self

    def connect(self)->DCNetzteilStatus:
        off = Off(self._netzteil)
        self._netzteil.set_status(off)  #state changed
        return (off)

    def disconnect(self)->DCNetzteilStatus:
        return self

    def run(self)->DCNetzteilStatus:
        return self

    def pause(self)->DCNetzteilStatus:
        return self

    def stop(self)->DCNetzteilStatus:
        return self