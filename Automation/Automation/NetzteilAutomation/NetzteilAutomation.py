from InstrumentAutomation.InstrumentAutomation import InstrumentAutomation
from InstrumentAutomation.Netzteil.Netzteil import Netzteil
from Signal.Signal import Signal
from threading import Timer
from typing import List

class NetzteilAutomation(InstrumentAutomation):
    def __init__(self,netzteil:Netzteil,signal:Signal = None,type = 'voltage'):
        super().__init__(instrument = netzteil)
        self.__signal = signal
        self.__type = type
        self.__timer:List[Timer] = []

    def getNetzteil(self)->Netzteil:
        return super().getInstrument()

    def setNetzteil(self,netzteil:Netzteil):
        super().setInstrument(netzteil)

    def getSignal(self)->Signal:
        return self.__signal

    def setSignal(self,signal:Signal):
        self.__signal = signal

    def getType(self):
        return self.__type

    def setType(self,type:str):
        if (type.lower() != 'voltage') and (type.lower() != 'current'):
            pass
        else:
            self.__type = type.lower()

    def run(self):
        self.__timer.clear()
        if self.__signal is not None:
            eventList = self.__signal.generate()
            time = 0
            for event in eventList:
                if self.getType() == 'voltage':
                    newTimer = Timer(time,self.getNetzteil().set_voltage,[event.getValue(time)])
                else:
                    newTimer = Timer(time,self.getNetzteil().set_current,[event.getValue(time)])
                self.__timer.append(newTimer)
        for timer in self.__timer:
            timer.start()
        
    def cancel(self):
        for timer in self.__timer:
            timer.cancel()
        self.__timer.clear()
