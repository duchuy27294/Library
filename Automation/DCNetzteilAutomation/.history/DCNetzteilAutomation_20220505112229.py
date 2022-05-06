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
        self.__timer:List[Timer] = []
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
            self.__type = type.lower()

    def generate(self):
        if not self.__event:
            self.__event.clear()
        if self.__signal is not None:
            self.__event = self.__signal.generate()

    def getNetzteil(self):
        return self.__netzteil

    def do(self):
        if self.__type == 'voltage':
            self.__netzteil.set_voltage(self.__event[self.__currentIndex].getValue())
        else:
            self.__netzteil.set_current(self.__event[self.__currentIndex].getValue())
        thisTimer = self.__timer.pop(0)
        self.__currentIndex += 1
        if self.__currentIndex == len(self.__event):
            self.__currentIndex = 0
            self.stop()

    def run(self):
        if not self.__timer:
            self.__timer.clear()
        startTimer = 0
        if self.__event:
            for event in self.__event:
                newTimer = Timer(startTimer,self.do)
                startTimer += event.getDuration()
                self.__timer.append(newTimer)
        self.__start = time.time()
        if self.__timer:
            for timer in self.__timer:
                timer.start()

    def pause(self):
        for timer in self.__timer:
            timer.cancel()
        self.__timer.clear()
        self.__save = time.time()
        past = self.__save - self.__start
        pastDuration = 0
        for i in range (0,self.__currentIndex,1):
            pastDuration += self.__event[i].getDuration()

    def resume(self):
        pass

    def stop(self):
        pass
