from abc import abstractmethod
from Netzteil import Netzteil

class Status(object):
    def __init__(self,netzteil:Netzteil):
        self._netzteil = netzteil
        Status._disconnected = Disconnected(netzteil)
        