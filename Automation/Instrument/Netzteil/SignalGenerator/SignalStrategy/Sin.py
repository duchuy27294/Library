from SignalGenerator.SignalStrategy.PeriodicSignal import PeriodicSignal
import math
import numpy as np

class Sin(PeriodicSignal):
    def __init__(self,duration: float = 0.2, xOffset = 0, yOffset = 0, amplitude = 1, step = 0.1):
        super().__init__(duration = duration, xOffset = xOffset, yOffset = yOffset, amplitude = amplitude, step = step)

    def getValue(self,time:float):
        if (time >= self.getXOffset()) and (time < (self.getDuration() + self.getXOffset())):
            return self.getAmplitude()*math.sin(time) + self.getYOffset()
        else:
            return 0

    def generate(self):
        x = np.arange(self.getXOffset(),self.getXOffset() + self.getDuration(),self.getStep(),dtype = float)
        y = []
        for i in x:
            y.append(self.getAmplitude()*math.sin(i) + self.getYOffset())
        return x,y

     
