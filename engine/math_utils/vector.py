import numpy as np

__all__ = [
    "Vector3"
]

class Vector3:
    def __init__(self, x: float=0, y: float=0, z: float=0):
        self.x = x
        self.y = y
        self.z = z

    def __call__(self, *args, **kwds):
        return np.array([self.x, self.y, self.z])

    def __mul__(self, other):
        if type(other) is int or type(other) is float:
            return Vector3(self.x * other, self.y * other, self.z * other)
        else:
            raise TypeError("Vectors must be multiplied only by scalars!")
            