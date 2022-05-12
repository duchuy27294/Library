from Netzteil.DummyNetzteil import DummyNetzteil

class Tdk(DummyNetzteil):
    tdk_count:int = 0

    def __init__(self, name:str = "TDK?",   \
                max_voltage: float = 18.0, max_current: float = 18, \
                tolerance_voltage:float = 0.05, tolerance_current:float = 0) -> None:
        DummyNetzteil.__init__(self,name,max_voltage,max_current,tolerance_voltage,tolerance_current)
        self.__tdk_id:str = 'Tdk' + str(Tdk.tdk_count+1)
        Tdk.tdk_count += 1

    def get_tdk_id(self) -> str:
        return self.__tdk_id

    @classmethod
    def get_tdk_count(cls)->int:
        return Tdk.tdk_count
