__all__ = [
    "Behaviour"
]

class Behaviour:
    def __init__(self, obj):
        self.obj = obj

    def tick(self, dt: float): ...
    def render(self): ...