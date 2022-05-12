from Netzteil.DCNetzteilInterface import DCNetzteilInterface
from threading import Timer
import os
from DCNetzteilStatus.DCNetzteilStatus import DCNetzteilStatus
from DCNetzteilStatus.Off import Off
from DCNetzteilAutomation.DCNetzteilAutomation import DCNetzteilAutomation


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
        self.__status = Off(self)
        self.__tolerance_voltage = tolerance_voltage
        #echter Voltage-wert = self.__voltage - self.__tolerance_voltage
        self.__tolerance_current = tolerance_current
        #echter Current-wert = self.__current - self.__tolerance_current
        self.__voltageAutomation:NetzteilAutomation = NetzteilAutomation(netzteil = self,type = 'voltage')
        self.__currentAutomation:NetzteilAutomation = NetzteilAutomation(netzteil = self,type = 'current')
        DummyNetzteil.count += 1

    def __del__(self):
        DummyNetzteil.count -= 1

    def get_voltage(self) -> float:
        return self.__voltage

    def get_current(self) -> float:
        return self.__current

    def set_voltage(self,value:float):
        if (self.__status.__class__.__name__ != 'Off') and (self.__status.__class__.__name__ != 'Disconnected') and (self.__status.__class__.__name__ != 'Pause'):
            if (value <= self.__max_voltage) and (value >= 0):
                self.__voltage = value

    def set_current(self,value:float):
        if (self.__status.__class__.__name__ != 'Off') and (self.__status.__class__.__name__ != 'Disconnected') and (self.__status.__class__.__name__ != 'Pause'):
            if (value <= self.__max_current) and (value >= 0):
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
        if (status.__class__.__name__ != self.__status.__class__.__name__):
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

    def getDuration(self):
        maxDuration = self.getVoltageAutomation().getDuration()
        if maxDuration < self.getCurrentAutomation().getDuration():
            maxDuration = self.getCurrentAutomation().getDuration()
        return maxDuration
    
    def endAutomation(self):
        self.stop(self)

    def run(self):
        # if self.get_status() == Status.OFF:
        #     self.set_status(Status.ON)
        # self.set_status(Status.RUNNING)
        self.__status.run()
        # timer = Timer(self.getDuration(),self.endAutomation)
        # self.generateVoltage()
        # self.generateCurrent()
        # timer.start()

    # def cancel(self):
        # self.__voltageAutomation.cancel()
        # self.__currentAutomation.cancel()
        # self.__status.stop()

    def turnOn(self):
        self.__status.turnOn()

    def turnOff(self):
        self.__status.turnOff()

    def connect(self):
        self.__status.connect()

    def disconnect(self):
        self.__status.disconnect()

    def save(self):
        self.__status.save()

    def resume(self):
        self.__status.resume()

    def stop(self):
        self.__status.stop()
        
