from MathSignal.PeriodicSignal import PeriodicSignal
from Event.Event import Event
import math
from typing import List

class Sin(PeriodicSignal):
    def __init__(self,duration:float = 0.1, xOffset:float = 0.0, yOffset:float = 0.0):
        super().__init__(duration = duration, xOffset = xOffset,yOffset = yOffset)

    def getValue(self,time):
        if (time < self.getDuration()):
            return math.sin(time-self.getXOffset()) + self.getYOffset()

    def generate(self)->List[Event]:
        event:List[Event] = []
        size = self.getDuration() / 0.1
        for i in range (0,size,1):
            newEvent = Event(i*0.1,self.getValue(i*0.1))
            event.append(newEvent)
        return event