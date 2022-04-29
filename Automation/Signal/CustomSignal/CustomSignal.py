from CustomSignal.Event import Event
from Signal.Signal import Signal
from typing import List

class CustomSignal(Signal):
    def __init__(self,eventList:List[Event] = []):
        self.__event = eventList

    def count(self):
        return len(self.__event)

    def getEvent(self,index:int):
        if index < len(self.__event):
            return self.__event[index]

    def addEvent(self,event:Event):
        self.__event.append(event)

    def duration(self):
        duration = 0
        for event in self.__event:
            duration += event.getDuration()
        return duration

    def removeEvent(self):
        self.__event.pop()

    