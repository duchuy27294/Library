from Automation.Automation import Automation
from Netzteil.DCNetzteilInterface import DCNetzteilInterface
from MathSignal.MathSignal import MathSignal
from threading import Timer
from Event.Event import Event
from typing import List
import time

class DCNetzteilAutomation(Automation):
    def __init__(self,netzteil:DCNetzteilInterface,signal:MathSignal = None, type = 'voltage'):
        self.__netzteil = netzteil
        self.__type:str = type
        self.__signal:MathSignal = signal
        self.__event:List[Event] = []
        self.__stopTimer = None
        self.__timer[Timer] = []
        self.__currentIndex = 0
        self.__start = 0
        self.__save = None

    def getSignal(self):
        return self.__signal

    def setSignal(self,signal:MathSignal):
        self.__signal = signal

    def getType(self):
        return self.__type

    def setType(self,type:str):
        if (type.lower() == 'voltage') or (type.lower() == 'current'):
            self.__type = type 

    def generate(self):
        if not self.__event:
            self.__event.clear()
        if self.__signal is not None:
            self.__event = self.__signal.generate()

    def getNetzteil(self):
        return self.__netzteil

    def run(self):
        duration = self.__signal.getDuration()
        self.__stopTimer = Timer(duration,self.stop)


    def pause(self):
        pass

    def resume(self):
        pass

    def stop(self):
        pass
