from Netzteil.Netzteil import Netzteil
from threading import Timer
import os
from Netzteil.Status import Status
from Netzteil.Automation import Automation


class DummyNetzteil(Netzteil):
    count:int = 0

    def __init__(self,name:str = "Netzteil", \
                    max_voltage:float = 20.0, max_current:float = 20.0,  \
                    tolerance_voltage:float = 0, tolerance_current:float = 0.0):
        #voltage in V, current in mA
        self.__name:str = name
        self.__voltage:float = 0
        self.__current:float = 0
        self.__max_voltage:float = max_voltage
        self.__max_current:float = max_current
        self.__status:Status = Status.OFF  
        self.__tolerance_voltage = tolerance_voltage
        #echter Voltage-wert = self.__voltage - self.__tolerance_voltage
        self.__tolerance_current = tolerance_current
        #echter Current-wert = self.__current - self.__tolerance_current
        self.__voltageAutomation:Automation = Automation(netzteil = self,\
            log = os.getcwd() + "\\log\\" + self.get_name() + "_voltage.csv",type = "voltage")
        self.__currentAutomation:Automation = Automation(netzteil = self,\
            log = os.getcwd() + "\\log\\" + self.get_name() + "_current.csv",type = "current")
        DummyNetzteil.count += 1

    def __del__(self):
        DummyNetzteil.count -= 1

    def get_voltage(self) -> float:
        return self.__voltage

    def get_current(self) -> float:
        return self.__current

    def set_voltage(self,value:float):
        if (self.__status != Status.OFF) and (self.__status != Status.DC):
            if (value <= self.__max_voltage):
                self.__voltage = value

    def set_current(self,value:float):
        if (self.__status != Status.OFF) and (self.__status != Status.DC):
            if (value <= self.__max_current):
                self.__current = value

    def get_max_voltage(self)->float:
        return self.__max_voltage

    def get_max_current(self)->float:
        return self.__max_current

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
    
    def set_status(self,value:Status):
        if self.get_status() != value:
            if (value == Status.OFF) or (value == Status.DC):
                if (self.__status == Status.RUNNING):
                    self.__voltageAutomation.cancel()
                    self.__currentAutomation.cancel()
                self.clear()
            self.__status = value

    def get_status(self)->Status:
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
        self.set_status(Status.ON)

    def run(self):
        self.set_status(Status.ON)
        self.set_status(Status.RUNNING)
        timer = Timer(self.getDuration(),self.endAutomation)
        self.generateVoltage()
        self.generateCurrent()
        timer.start()
        
