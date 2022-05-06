from DCNetzteilStatus.DCNetzteilStatus import DCNetzteilStatus
from DCNetzteilStatus.Disconnected import Disconnected
from DCNetzteilStatus.On import On
from Netzteil.DCNetzteilInterface import DCNetzteilInterface

class Off(DCNetzteilStatus):
    def __init__(self,netzteil:DCNetzteilInterface):
        super().__init__(netzteil)

    def turnOn(self)->DCNetzteilStatus:
        on = On(self._netzteil)
        self._netzteil.set_status(on)   #state changed
        return on

    def turnOff(self)->DCNetzteilStatus:
        return self

    def connect(self)->DCNetzteilStatus:
        return self

    def disconnect(self)->DCNetzteilStatus:
        disconnected = Disconnected(self._netzteil)
        self._netzteil.set_status(disconnected)
        return disconnected

    def run(self)->DCNetzteilStatus:
        self.turnOn()   #state changed
        self._netzteil.run()
        return self._netzteil.get_status()

    def pause(self)->DCNetzteilStatus:
        return self

    def stop(self)->DCNetzteilStatus:
        return self