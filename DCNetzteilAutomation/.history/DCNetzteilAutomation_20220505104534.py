from Automation.Automation import Automation
from Netzteil.DCNetzteilInterface import DCNetzteilInterface
from MathSignal.MathSignal import MathSignal

class DCNetzteilAutomation(Automation):
    def __init__(self,netzteil:DCNetzteilInterface,signal:MathSignal = None, type = 'voltage'):
        self.__netzteil = netzteil
        self.__type:str = type
        self.__signal:MathSignal = signal
