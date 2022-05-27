#from Lib.Netzteil.DCNetzteilInterface import DCNetzteilInterface
from abc import abstractmethod
try:
    from ..Automation.Automation import Automation
    from ..MathSignal import MathSignal,ConstantSignal
    from ..SuperSignal import SuperSignal
    from ..ResumableTimer import ResumableTimer
except (ModuleNotFoundError,ImportError):
    from Automation.Automation import Automation
    from MathSignal import MathSignal,ConstantSignal
    from SuperSignal import SuperSignal
    from ResumableTimer import ResumableTimer
#from threading import Timer
#from ..Event.Event import Event
from typing import List
import time

class DCNetzteilAutomation(Automation):
    def __init__(self,netzteil,signal:SuperSignal = None):
        self._netzteil = netzteil
        self._signal:SuperSignal = signal
        #self.__event:List[Event] = []
        self.__contantSignal:List[ConstantSignal] = []
        self.__timer:List[ResumableTimer] = []
        self.__currentIndex = 0
        #self.__start = 0
        #self.__save = None

    def getSignal(self):
        return self._signal

    def setSignal(self,signal:SuperSignal):
        self._signal = signal

    def getType(self):
        return self.__type

    def generate(self):
        if self.__constantSignal:
            self.__constantSignal.clear()
        if self._signal is not None:
            self.__constantSignal = self._signal.generate()

    def getNetzteil(self):
        return self._netzteil

    @abstractmethod
    def do(self):
        pass
        # if self.__type.lower() == 'voltage':
        #     self.__netzteil.set_voltage(self.__event[self.__currentIndex].getValue())
        # else:
        #     self.__netzteil.set_current(self.__event[self.__currentIndex].getValue())
        # self.__currentIndex += 1
        # if self.__currentIndex >= len(self.__event):
        #     self.__currentIndex = 0
        #     self.stop()

    def run(self):
        if self._signal is not None:
            if self.__timer:
                for i in range (len(self.__timer)-1,-1,-1):
                    timer = self.__timer[i]
                    self.__timer.remove(timer)
                    del timer
            startTimer = 0.1
            self.generate()
            self.__currentIndex = 0
            # if self.__event:
            if self.__constantSignal:
                for i in range (0,len(self.__constantSignal),1):
                    # newTimer = Timer(startTimer,self.do)
                    newTimer = ResumableTimer(startTimer,self.do)
                    startTimer += self.__constantSignal[i].getDuration()
                    self.__timer.append(newTimer)
            self.__start = time.time()
            if self.__timer:
                for t in self.__timer:
                    t.start()

    def pause(self):
        for timer in self.__timer:
            timer.cancel()
        self.__timer.clear()
        self.__save = time.time()
        past = self.__save - self.__start
        pastDuration = 0
        for i in range (0,self.__currentIndex,1):
            pastDuration += self.__event[i].getDuration()
        rest = self.__signal.getDuration() - past
        startTimer = self.__event[self.__currentIndex].getDuration() - (past - pastDuration)
        for i in range (self.__currentIndex,len(self.__event),1):
            newTimer = Timer(startTimer,self.do)
            if (i != len(self.__event)-1):
                startTimer += self.__event[i+1].getDuration()
            self.__timer.append(newTimer)

    def resume(self):
        self.__start = time.time()
        self.__save = time.time()
        if self.__timer:
            for timer in self.__timer:
                timer.start()

    def cancel(self):
        if self.__timer:
            for timer in self.__timer:
                timer.cancel()
        self.stop()

    def stop(self):
        self.__start = time.time()
        self.__save = None
        self.__currentIndex = 0
        #self.__netzteil.set_status(self.__netzteil.getOn())
