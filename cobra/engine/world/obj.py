from .behaviours import *

__all__ = [
    "Obj"
]

class Obj:
    def __init__(self):
        self.transform = Transform()

    def tick(self, dt: float):
        ...

    def render(self):
        ...