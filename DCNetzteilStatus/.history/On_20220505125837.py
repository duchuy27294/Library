from DCNetzteilStatus.DCNetzteilStatus import DCNetzteilStatus
from DCNetzteilStatus.Off import Off
from DCNetzteilStatus.Working import Working
from Netzteil.DCNetzteilInterface import DCNetzteilInterface

class On(DCNetzteilStatus):
    def __init__(self,netzteil:DCNetzteilInterface):
        super().__init__(netzteil = netzteil)
    
    def turnOn(self)->DCNetzteilStatus:
        return self

    def turnOff(self)->DCNetzteilStatus:
        off = Off(self._netzteil)
        self._netzteil.set_status(off)  #state changed
        return off

    def connect(self)->DCNetzteilStatus:
        return self

    def disconnect(self)->DCNetzteilStatus:
        self.turnOff  #state changed
        return self._netzteil.get_status().disconnect()

    def run(self)->DCNetzteilStatus:
        working = Working(self._netzteil)
        self._netzteil.set_status(working)
        self._netzteil.run()
        return working

    def pause(self)->DCNetzteilStatus:
        return self

    def stop(self)->DCNetzteilStatus:
        return self