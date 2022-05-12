from Netzteil.DummyNetzteil.DummyNetzteil import DummyNetzteil

class Syskon(DummyNetzteil):
    syskon_count:int = 0

    def __init__(self, name:str = "Syskon?",  \
                    max_voltage = 60.0,   \
                    max_current = 30.0, tolerance_voltage = 0.04,tolerance_current = 0.02)->None:
        DummyNetzteil.__init__(self,name,max_voltage,max_current,tolerance_voltage,tolerance_current)
        self.__syskon_id:str = 'syskon' + str(Syskon.syskon_count+1)
        Syskon.syskon_count += 1

    def __del__(self):
        Syskon.syskon_count -= 1

    def get_private_id(self) -> str:
        return self.__syskon_id

    @classmethod
    def get_syskon_count(cls)->int:
        return Syskon.syskon_count