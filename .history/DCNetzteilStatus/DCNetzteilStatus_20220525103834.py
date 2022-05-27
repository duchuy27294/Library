from __future__ import annotations
from abc import abstractmethod
from ..Status.Status import Status

class DCNetzteilStatus(Status):
    def __init__(self,netzteil):
        self._netzteil = netzteil

    @abstractmethod
    def turnOn(self):
        pass

    @abstractmethod
    def turnOff(self):
        pass

    # @abstractmethod
    # def connect(self):
    #     pass

    # @abstractmethod
    # def disconnect(self):
    #     pass

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def pause(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def resume(self):
        pass

    @abstractmethod
    def toString(self):
        pass
    
# class Disconnected(DCNetzteilStatus):
#     def __init__(self,netzteil):
#         super().__init__(netzteil = netzteil)

#     def turnOn(self):
#         pass

#     def turnOff(self):
#         pass

#     def connect(self):
#         off = self._netzteil.getOff()
#         self._netzteil.set_status(off)  #state changed

#     def disconnect(self):
#         pass

#     def run(self):
#         pass

#     def pause(self):
#         pass

#     def stop(self):
#         pass     

#     def resume(self):
#         pass

#     def toString(self):
#         return 'Disconnected'

class Off(DCNetzteilStatus):
    def __init__(self,netzteil):
        super().__init__(netzteil)

    def turnOn(self):
        on = self._netzteil.getOn()
        self._netzteil.set_status(on)   #state changed

    def turnOff(self):
        pass

    # def connect(self):
    #     pass

    # def disconnect(self):
    #     disconnected = self._netzteil.getDisconnected()
    #     self._netzteil.set_status(disconnected)

    def run(self):
        self.turnOn()   #state changed
        self._netzteil.get_status().run()

    def pause(self):
        pass

    def stop(self):
        pass

    def resume(self):
        pass

    def toString(self):
        return 'Off'

class On(DCNetzteilStatus):
    def __init__(self,netzteil):
        super().__init__(netzteil = netzteil)
    
    def turnOn(self):
        pass

    def turnOff(self):
        off = self._netzteil.getOff()
        self._netzteil.clear()
        self._netzteil.set_status(off)  #state changed

    # def connect(self):
    #     pass

    # def disconnect(self):
    #     self.turnOff()  #state changed
    #     self._netzteil.get_status().disconnect()

    def run(self):
        working = self._netzteil.getWorking()
        self._netzteil.set_status(working)  #state changed

    def pause(self):
        pass

    def stop(self):
        pass
    
    def resume(self):
        pass

    def toString(self):
        return 'On'

class Pause(DCNetzteilStatus):
    def __init__(self,netzteil):
        super().__init__(netzteil)

    def turnOn(self):
        pass

    def turnOff(self):
        self.stop() #state changed
        self._netzteil.get_status().turnOff()  #state changed

    # def connect(self):
    #     pass

    # def disconnect(self):
    #     self.turnOff()  #state changed
    #     self._netzteil.get_status().disconnect() #state changed

    def run(self):
        pass

    def pause(self):
        pass

    def stop(self):
        on = self._netzteil.getOn()
        self._netzteil.set_status(on)   #state_changed

    def resume(self):
        working = self._netzteil.getWorking()
        self._netzteil.set_status(working)  #state changed

    def toString(self):
        return 'Pause'

class Working(DCNetzteilStatus):
    def __init__(self,netzteil):
        super().__init__(netzteil = netzteil)

    def turnOn(self):
        pass

    def turnOff(self):
        self.stop() #state changed
        self._netzteil.get_status().turnOff()

    # def connect(self):
    #     pass

    # def disconnect(self):
    #     self.turnOff()  #state changed
    #     self._netzteil.get_status().disconnect()

    def run(self):
        pass

    def pause(self):
        pause = self._netzteil.getPause()
        self._netzteil.set_status(pause)

    def stop(self):
        on = self._netzteil.getOn()
        self._netzteil.set_status(on)

    def resume(self):
        pass

    def toString(self):
        return 'Working'

