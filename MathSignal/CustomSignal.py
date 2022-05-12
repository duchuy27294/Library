from Lib.Event import Event
from .MathSignal import MathSignal
from typing import List

class CustomSignal(MathSignal):
    def __init__(self,eventList:List[Event] = []):
        self.__event = eventList

    def count(self):
        return len(self.__event)

    def getEvent(self,index:int):
        if index < len(self.__event):
            return self.__event[index]

    def addEvent(self,event:Event):
        self.__event.append(event)

    def getValue(self,time):
        currentTime = 0
        for event in self.__event:
            currentTime += event.getDuration()
            if time < currentTime:
                return event.getValue()
        return None

    def getDuration(self):
        duration = 0
        for event in self.__event:
            duration += event.getDuration()
        return duration

    def removeEvent(self):
        self.__event.pop()

    def generate(self)->List[Event]:
        return self.__event

    def isEmpty(self):
        if self.__event:
            return False
        else:
            return True