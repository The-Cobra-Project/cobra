import numpy as np

__all__ = [
    "Vector3",
    "Vector4"
]

class Vector3:
    def __init__(self, x: float=0, y: float=0, z: float=0):
        self.x = x
        self.y = y
        self.z = z

    def __call__(self, *args, **kwds):
        return np.array([self.x, self.y, self.z])

    def __add__(self, other):
        if type(other) is not Vector3 and type(other) is not Vector4:
            raise TypeError("You can only add a 3D or 4D vector to a 3D vector!")
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __mul__(self, other):
        if not (type(other) is int or type(other) is float):
            raise TypeError("Vectors must be multiplied only by scalars!")
        
        return Vector3(self.x * other, self.y * other, self.z * other)
        
            
class Vector4:
    def __init__(self, x: float=0, y: float=0, z: float=0, w: float=0):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def __call__(self, *args, **kwds):
        return np.array([self.x, self.y, self.z, self.w])
    
    def __add__(self, other):
        if type(other) is not Vector4:
            raise TypeError("You can only add a 4D vector to a 4D vector!")
        return Vector4(self.x + other.x, self.y + other.y, self.z + other.z, self.w + other.w)

    def __mul__(self, other):
        if not (type(other) is int or type(other) is float):
            raise TypeError("Vectors must be only multiplied by scalars!")
        
        return Vector4(self.x * other, self.y * other, self.z * other, self.w * other)