from .behaviour import *
from .behaviours import *

__all__ = [
    "Obj"
]

class Obj:
    def __init__(self):
        self.transform = Transform(self)
        self.__behaviours: list[Behaviour] = []

    def add_behaviour(self, behaviour: type[Behaviour]) -> Behaviour:
        b = behaviour(self)
        self.__behaviours.append(b)
        return b

    def tick(self, dt: float):
        for b in self.__behaviours:
            b.tick(dt)

    def render(self):
        for b in self.__behaviours:
            b.render()
