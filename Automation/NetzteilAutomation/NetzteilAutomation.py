from InstrumentAutomation.InstrumentAutomation import InstrumentAutomation
from Instrument.Netzteil.Netzteil.Netzteil import Netzteil
from Signal.Signal.Signal import Signal
import os

class NetzteilAutomation(InstrumentAutomation):
    def __init__(self,netzteil:Netzteil,signal:Signal):
        super().__init__(instrument = netzteil)
        self.__signal = signal

    def getSignal(self):
        return self.__signal

    def setSignal(self,signal):
        self.__signal = signal

        