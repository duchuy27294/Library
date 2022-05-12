class Event(object):
    def __init__(self,duration:float = 0.0,value:float = 0.0):
        if duration < 0:
            self.__duration = 0
        else:
            self.__duration = duration
        self.__value = value

    def getDuration(self):
        return self.__duration

    def setDuration(self,duration:float):
        if duration >= 0:
            self.__duration = duration

    def getValue(self):
        return self.__value

    def setValue(self,value:float):
        self.__value = value

    def toString(self):
        ret = 'Duration = ' + str(self.__duration) + ', Value = ' + str(self.__value)
        return ret
