from Status import Status
from Netzteil import Netzteil

class Disconnected(Status):
    def __init__(self,netzteil:Netzteil):
        super().__init__(netzteil = netzteil)
        print('Disconnected')