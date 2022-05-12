from ERA_Rezipient.ERA_Rezipient_Interface import ERA_Rezipient_Interface
from Netzteil.DCNetzteil import DCNetzteil
from typing import List

class ERA_Rezipient(ERA_Rezipient_Interface):
    def __init__(self):
        self.__netzteil:List[DCNetzteil] = []