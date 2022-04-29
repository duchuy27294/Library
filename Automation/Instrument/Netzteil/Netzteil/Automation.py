from Netzteil.Netzteil import Netzteil
from typing import List
import csv
from threading import Timer

class Automation(object):
    def __init__(self,netzteil:Netzteil,file:str = 'file.csv',type:str = 'voltage'):
        self.__file = file
        self.__time:List[float] = []
        self.__value:List[float] = []
        self.__netzteil:Netzteil = netzteil
        self.__type:str = type
        self.__currentIndex:int = 0
        self.__timerList:List[Timer] = []
        #self.read()

    def read(self):
        if self.__time:
            self.__time.clear()
        if self.__value:
            self.__value.clear()
        with open(self.__file,'r',newline ='') as data:
            read = csv.reader(data,delimiter = ';')
            i = 0
            for line in read:
                if i != 0:
                    time = float(line[0])
                    value = float(line[1])
                    self.__time.append(time)
                    self.__value.append(value)
                i+=1
            data.close()

    def getFile(self):
        return self.__file

    def setFile(self,file:str):
        if file.endswith('.csv'):
            self.__file = file

    def getNetzteil(self):
        return self.__netzteil

    def setNetzteil(self,netzteil):
        self.__netzteil = netzteil

    def getCurrentIndex(self):
        return self.__currentIndex

    def getCurrentTime(self):
        return self.__time[self.__currentIndex]

    def getCurrentValue(self):
        return self.__value[self.__currentIndex]

    def getTime(self,index:int):
        if (index < len(self.__time)):
            #print("Time = " + str(self.__time[index]))
            return self.__time[index]
        else:
            return None

    def getValue(self,index:int):
        if (index < len(self.__value)):
            return self.__value[index]
        else:
            return None

    def setTime(self,index:int,time:float):
        if (index < len(self.__time)):
            self.__time[index] = time

    def setValue(self,index:int,value:float):
        if (index < len(self.__value)):
            self.__value[index] = value

    def getTimeList(self):
        return self.__time

    def getValueList(self):
        return self.__value

    def getType(self):
        return self.__type

    def setType(self,type:str):
        thisType = type.lower()
        typeList = ['voltage','current']
        if (thisType in typeList):
            self.__type = thisType

    def getDuration(self):
        self.read()
        return self.__time[-1]

    def setNetzteilValue(self):
        if self.__type == 'voltage':
            self.__netzteil.set_voltage(self.__value[self.__currentIndex])
        else:
            self.__netzteil.set_current(self.__value[self.__currentIndex])
        self.__currentIndex += 1
        if self.__currentIndex >= len(self.__value):
            self.__currentIndex = 0
    
    def cancel(self):
        if self.__timerList:
            for timer in self.__timerList:
                timer.cancel()
        self.__timerList.clear()
    
    def clearTimerList(self):
        self.__timerList.clear()

    def run(self):
        self.read()
        end = Timer(self.__time[-1]+0.2,self.clearTimerList)
        self.__currentIndex = 0
        for i in range (0,len(self.__time),1):
            newTimer:Timer = Timer(self.__time[i],self.setNetzteilValue)
            self.__timerList.append(newTimer)
        if self.__timerList:
            for timer in self.__timerList:
                timer.start()
        end.start()