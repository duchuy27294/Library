from Status import Status
from Disconnected import Disconnected
from Netzteil import Netzteil

class Off(Status):
    def __init__(self,netzteil:Netzteil):
        super().__init__(netzteil)