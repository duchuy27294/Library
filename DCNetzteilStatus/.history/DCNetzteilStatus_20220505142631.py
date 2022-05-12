from __future__ import annotations
from abc import abstractmethod
from Status.Status import Status

class DCNetzteilStatus(Status):
    def __init__(self,netzteil):
        self._netzteil = netzteil

    @abstractmethod
    def turnOn(self)->DCNetzteilStatus:
        pass

    @abstractmethod
    def turnOff(self)->DCNetzteilStatus:
        pass

    @abstractmethod
    def connect(self)->DCNetzteilStatus:
        pass

    @abstractmethod
    def disconnect(self)->DCNetzteilStatus:
        pass

    @abstractmethod
    def run(self)->DCNetzteilStatus:
        pass

    @abstractmethod
    def pause(self)->DCNetzteilStatus:
        pass

    @abstractmethod
    def stop(self)->DCNetzteilStatus:
        pass
    
class Disconnected(DCNetzteilStatus):
    def __init__(self,netzteil):
        super().__init__(netzteil = netzteil)

    def turnOn(self)->DCNetzteilStatus:
        return self

    def turnOff(self)->DCNetzteilStatus:
        return self

    def connect(self)->DCNetzteilStatus:
        off = Off(self._netzteil)
        self._netzteil.set_status(off)  #state changed
        return (off)

    def disconnect(self)->DCNetzteilStatus:
        return self

    def run(self)->DCNetzteilStatus:
        return self

    def pause(self)->DCNetzteilStatus:
        return self

    def stop(self)->DCNetzteilStatus:
        return self      

class Off(DCNetzteilStatus):
    def __init__(self,netzteil):
        super().__init__(netzteil)

    def turnOn(self)->DCNetzteilStatus:
        on = On(self._netzteil)
        self._netzteil.set_status(on)   #state changed
        return on

    def turnOff(self)->DCNetzteilStatus:
        return self

    def connect(self)->DCNetzteilStatus:
        return self

    def disconnect(self)->DCNetzteilStatus:
        disconnected = Disconnected(self._netzteil)
        self._netzteil.set_status(disconnected)
        return disconnected

    def run(self)->DCNetzteilStatus:
        self.turnOn()   #state changed
        self._netzteil.run()
        return self._netzteil.get_status()

    def pause(self)->DCNetzteilStatus:
        return self

    def stop(self)->DCNetzteilStatus:
        return self

class On(DCNetzteilStatus):
    def __init__(self,netzteil):
        super().__init__(netzteil = netzteil)
    
    def turnOn(self)->DCNetzteilStatus:
        return self

    def turnOff(self)->DCNetzteilStatus:
        off = Off(self._netzteil)
        self._netzteil.set_status(off)  #state changed
        return off

    def connect(self)->DCNetzteilStatus:
        return self

    def disconnect(self)->DCNetzteilStatus:
        self.turnOff()  #state changed
        self._netzteil.disconnect()
        return self._netzteil.get_status()

    def run(self)->DCNetzteilStatus:
        working = Working(self._netzteil)
        self._netzteil.set_status(working)  #state changed
        return working

    def pause(self)->DCNetzteilStatus:
        return self

    def stop(self)->DCNetzteilStatus:
        return self

class Pause(DCNetzteilStatus):
    def __init__(self,netzteil):
        super().__init__(netzteil)

    def turnOn(self)->DCNetzteilStatus:
        return self

    def turnOff(self)->DCNetzteilStatus:
        self.stop() #state changed
        self._netzteil.turnOff()  #state changed
        return self._netzteil.get_status()

    def connect(self)->DCNetzteilStatus:
        return self

    def disconnect(self)->DCNetzteilStatus:
        self.turnOff()  #state changed
        self._netzteil.disconnect() #state changed
        return self._netzteil.get_status()

    def run(self)->DCNetzteilStatus:
        return self

    def pause(self)->DCNetzteilStatus:
        return self

    def stop(self)->DCNetzteilStatus:
        on = On(self._netzteil)
        self._netzteil.set_status(on)   #state_changed
        return on

    def resume(self)->DCNetzteilStatus:
        working = Working(self._netzteil)
        self._netzteil.set_status(working)  #state changed
        return working

class Working(DCNetzteilStatus):
    def __init__(self,netzteil):
        super().__init__(netzteil = netzteil)

    def turnOn(self)->DCNetzteilStatus:
        return self

    def turnOff(self)->DCNetzteilStatus:
        self.stop() #state changed
        self._netzteil.turnOff()
        return self._netzteil.get_status()

    def connect(self)->DCNetzteilStatus:
        return self

    def disconnect(self)->DCNetzteilStatus:
        self.turnOff()  #state changed
        self._netzteil.disconnect()
        return self._netzteil.get_status()

    def run(self)->DCNetzteilStatus:
        return self

    def pause(self)->DCNetzteilStatus:
        pause = Pause(self._netzteil)
        self._netzteil.set_status(pause)
        return pause

    def stop(self)->DCNetzteilStatus:
        on = On(self._netzteil)
        self._netzteil.set_status(on)
        return on

    def save(self):
        self._netzteil.save()

