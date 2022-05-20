from SuperSignal import SuperSignal
from MathSignal import ConstantSignal
from MathSignal.PeriodicSignal import Sin,Cos
import math
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    s = SuperSignal()
    s1 = ConstantSignal(duration = 5,value = 5)
    s2 = ConstantSignal(duration = 5,value = 0)
    s3 = Sin(duration = 2*math.pi)
    s.add(s1)
    s.add(s2)
    s.add(s3)
    duration = s.getDuration()
    x = np.arange(0,duration,0.1,dtype = float)
    y = []
    for i in x:
        y.append(s.getValue(i))
    plt.plot(x,y)
    plt.show()
