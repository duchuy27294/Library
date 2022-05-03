from NetzteilStatus import NetzteilStatus
from Disconnected import Disconnected
from On import On
from Netzteil import Netzteil

class Off(NetzteilStatus):
    def __init__(self,netzteil:Netzteil):
        super().__init__(netzteil)

    def turnOn(self)->NetzteilStatus:
        on = On(self._netzteil)
        self._netzteil.set_status(on)
        return (on)

    def turnOff(self)->NetzteilStatus:
        return self

    def connect(self)->NetzteilStatus:
        return self

    def disconnect(self)->NetzteilStatus:
        disconnected = Disconnected(self._netzteil)
        self._netzteil.set_status(disconnected)
        return disconnected

    def run(self)->NetzteilStatus:
        on = On(self._netzteil)
        self._netzteil.set_status(on)
        self._netzteil.get_status().run()
        return on

    def pause(self)->NetzteilStatus:
        return self

    def stop(self)->NetzteilStatus:
        return self