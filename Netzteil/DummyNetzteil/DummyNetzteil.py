from Lib.Netzteil.DCNetzteilInterface import DCNetzteilInterface
from threading import Timer
from Lib.DCNetzteilStatus import *
from Lib.DCNetzteilAutomation.DCNetzteilAutomation import DCNetzteilAutomation
from Lib.MathSignal.MathSignal import MathSignal

class DummyNetzteil(DCNetzteilInterface):
    count:int = 0

    def __init__(self,name:str = "Dummy", \
                    max_voltage:float = 20.0, max_current:float = 20.0,  \
                    tolerance_voltage:float = 0, tolerance_current:float = 0.0):
        #voltage in V, current in mA
        super().__init__(max_voltage = max_voltage,max_current = max_current)
        self.__name:str = name
        self.__voltage:float = 0
        self.__current:float = 0
        self.__on = On(self)
        self.__off = Off(self)
        self.__disconnected = Disconnected(self)
        self.__working = Working(self)
        self.__pause = Pause(self) 
        self.__status = self.__off
        self.__tolerance_voltage = tolerance_voltage
        #echter Voltage-wert = self.__voltage - self.__tolerance_voltage
        self.__tolerance_current = tolerance_current
        #echter Current-wert = self.__current - self.__tolerance_current
        self.__voltageAutomation:DCNetzteilAutomation = DCNetzteilAutomation(netzteil = self,type = 'voltage')
        self.__currentAutomation:DCNetzteilAutomation = DCNetzteilAutomation(netzteil = self,type = 'current')
        DummyNetzteil.count += 1

    def __del__(self):
        DummyNetzteil.count -= 1

    def get_voltage(self) -> float:
        return self.__voltage

    def get_current(self) -> float:
        return self.__current

    def set_voltage(self,value:float):
        if (not self.isOff()) and (not self.isDisconnected()) and (not self.isPause()):
            if (value <= self.get_max_voltage()) and (value >= 0):
                self.__voltage = value

    def set_current(self,value:float):
        if (not self.isOff()) and (not self.isDisconnected()) and (not self.isPause()):
            if (value <= self.get_max_current()) and (value >= 0):
                self.__current = value

    def clear(self):
        self.set_voltage(0)
        self.set_current(0)

    def get_resistance(self)->float:
        try:
            return (self.__voltage/self.__current)
        except ZeroDivisionError:
            print("Current = 0 mA")

    def get_power(self)->float:
        return self.__voltage*self.__current

    def get_name(self)->str:
        return self.__name

    def set_name(self,value:str):
        self.__name = value

    def get_tolerance_voltage(self)->float:
        return self.__tolerance_voltage

    def get_tolerance_current(self)->float:
        return self.__tolerance_current

    def measure_voltage(self)->float:
        ret = self.__voltage - self.__tolerance_voltage
        if ret <= 0:
            return 0
        else:
            return ret

    def measure_current(self)->float:
        ret = self.__current - self.__tolerance_current
        if ret <= 0:
            return 0
        else:
            return ret

    def measure_power(self)->float:
        return self.measure_voltage()*self.measure_current()
    
    def set_status(self,status:DCNetzteilStatus):
        statusList = [self.__on,self.__off,self.__pause,self.__disconnected,self.__working]
        if (status in statusList):
            if (status != self.__status):
                self.__status = status

    def get_status(self)->DCNetzteilStatus:
        return self.__status

    @classmethod
    def get_count(cls)->int:
        return DummyNetzteil.count

    def getVoltageAutomation(self):
        return self.__voltageAutomation

    def generateVoltage(self):
        if self.__voltageAutomation is not None:
            self.__voltageAutomation.run()

    def getCurrentAutomation(self):
        return self.__currentAutomation

    def generateCurrent(self):
        if self.__currentAutomation is not None:
            self.__currentAutomation.run()

    def setVoltageSignal(self,signal:MathSignal):
        self.__voltageAutomation.setSignal(signal)

    def setCurrentSignal(self,signal:MathSignal):
        self.__currentAutomation.setSignal(signal)

    def getVoltageSignal(self):
        return self.__voltageAutomation.getSignal()

    def getCurrentSignal(self):
        return self.__currentAutomation.getSignal()

    def getDuration(self):
        maxDuration = self.getVoltageAutomation().getDuration()
        if maxDuration < self.getCurrentAutomation().getDuration():
            maxDuration = self.getCurrentAutomation().getDuration()
        return maxDuration
    
    def endAutomation(self):
        self.stop(self)

    def run(self):
        self.__status.run()
        if self.isWorking:
            self.__voltageAutomation.run()
            self.__currentAutomation.run()

    def pause(self):
        if self.isWorking():
            self.__voltageAutomation.pause()
            self.__currentAutomation.pause()
        self.__status.pause()

    def turnOn(self):
        self.__status.turnOn()

    def turnOff(self):
        if (self.isWorking()):
            self.__voltageAutomation.stop()
            self.__currentAutomation.stop()
        self.__status.turnOff()

    def connect(self):
        self.__status.connect()

    def disconnect(self):
        if (self.isWorking()):
            self.__voltageAutomation.stop()
            self.__currentAutomation.stop()
        self.__status.disconnect()

    def resume(self):
        if (self.isPause()):
            self.__voltageAutomation.resume()
            self.__currentAutomation.resume()
        self.__status.resume()

    def stop(self):
        if (self.isWorking()):
            self.__voltageAutomation.stop()
            self.__currentAutomation.stop()
        self.__status.stop()
        
    def isOn(self):
        return (self.__status == self.__on)

    def isOff(self):
        return (self.__status == self.__off)

    def isDisconnected(self):
        return (self.__status == self.__disconnected)

    def isConnected(self):
        return (not (self.__status == self.__disconnected))

    def isWorking(self):
        return (self.__status == self.__working)

    def isPause(self):
        return (self.__status == self.__pause)

    def getOn(self):
        return self.__on

    def getOff(self):
        return self.__off

    def getDisconnected(self):
        return self.__disconnected
    
    def getWorking(self):
        return self.__working

    def getPause(self):
        return self.__pause


