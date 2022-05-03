from Status import Status
from Disconnected import Disconnected
from Netzteil import Netzteil

class Off(Status):
    def __init__(self,netzteil:Netzteil):
        super().__init__(netzteil)

    def turnOn(self)->Status:
        return ()

    def turnOff(self)->Status:
        return self

    def connect(self)->Status:
        return (Off(self.netzteil))

    def disconnect(self)->Status:
        return self

    def run(self)->Status:
        return self

    def pause(self)->Status:
        return self

    def stop(self)->Status:
        return self