from DCNetzteilStatus.DCNetzteilStatus import DCNetzteilStatus
from DCNetzteilStatus.On import On
from DCNetzteilStatus.Pause import Pause
from DCNetzteilStatus.Off import Off
from Netzteil.DCNetzteilInterface import DCNetzteilInterface

class Working(DCNetzteilStatus):
    def __init__(self,netzteil:DCNetzteilInterface):
        super().__init__(netzteil = netzteil)

    def turnOn(self)->DCNetzteilStatus:
        return self

    def turnOff(self)->DCNetzteilStatus:
        self.stop() #state changed
        self._netzteil.turnOff()
        return off

    def connect(self)->DCNetzteilStatus:
        return self

    def disconnect(self)->DCNetzteilStatus:
        self.turnOff()
        return self._netzteil.get_status().disconnect()

    def run(self)->DCNetzteilStatus:
        return self

    def pause(self)->DCNetzteilStatus:
        pause = Pause(self._netzteil)
        self.save()
        self._netzteil.set_status(pause)
        return pause

    def stop(self)->DCNetzteilStatus:
        on = On(self._netzteil)
        self._netzteil.set_status(on)
        return on

    def save(self):
        self._netzteil.save()