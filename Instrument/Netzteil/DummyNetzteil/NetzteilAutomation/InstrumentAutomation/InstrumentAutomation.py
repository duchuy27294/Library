from NetzteilAutomation.InstrumentAutomation.Automation.Automation import Automation
from abc import abstractmethod
from Instrument.Instrument import Instrument

class InstrumentAutomation(Automation):
    def __init__(self,instrument:Instrument):
        self.__instrument = instrument

    def getInstrument(self):
        return self.__instrument

    @abstractmethod
    def run(self):
        pass

    # @abstractmethod
    # def pause(self):
    #     pass

    @abstractmethod
    def cancel(self):
        pass

    @abstractmethod
    def stop(self):
        pass
