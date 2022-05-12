from NetzteilStatus.NetzteilStatus import NetzteilStatus
from NetzteilStatus.Disconnected import Disconnected
from NetzteilStatus.On import On
from Netzteil.Netzteil import Netzteil

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
        self._netzteil.turnOn()
        self._netzteil.get_status().run()
        return self._netzteil.get_status()

    def pause(self)->NetzteilStatus:
        return self

    def stop(self)->NetzteilStatus:
        return self