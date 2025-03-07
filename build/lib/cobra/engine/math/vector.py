import numpy as np
import math

__all__ = [
    "Vector2",
    "Vector3",
    "Vector4"
]

class Vector2:
    def __init__(self, x: float=0, y: float=0):
        self.x = x
        self.y = y

    def __call__(self, *args, **kwds):
        return np.array([self.x, self.y])

    def __add__(self, other):
        if type(other) is not Vector2:
            raise TypeError("You can only add a 2D vector to a 2D vector!")
        return Vector2(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        if type(other) is not Vector2:
            raise TypeError("You can only subtract a 2D vector from a 2D vector!")
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if not (type(other) is int or type(other) is float):
            raise TypeError("Vectors must be only multiplied by scalars!")
        
        return Vector2(self.x * other, self.y * other)
    
    def __truediv__(self, other):
        if not (type(other) is int or type(other) is float):
            raise TypeError("Vectors must be only divided by scalars!")
        
        return Vector2(self.x / other, self.y / other)

    def get_magnitude(self) -> float:
        return np.sqrt(self.x**2 + self.y**2).item()

    def get_normalized(self):
        mag = self.get_magnitude()
        if mag == 0:
            return Vector2()
        return self / mag

class Vector3:
    def __init__(self, x: float=0, y: float=0, z: float=0):
        self.x = x
        self.y = y
        self.z = z

    def __call__(self, *args, **kwds):
        return np.array([self.x, self.y, self.z])

    def __add__(self, other):
        if type(other) is not Vector3:
            raise TypeError("You can only add a 3D vector to a 3D vector!")
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        if type(other) is not Vector3:
            raise TypeError("You can only subtract a 3D vector from a 3D vector!")
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        if not (type(other) is int or type(other) is float):
            raise TypeError("Vectors must be multiplied only by scalars!")
        
        return Vector3(self.x * other, self.y * other, self.z * other)
    
    def __truediv__(self, other):
        if not (type(other) is int or type(other) is float):
            raise TypeError("Vectors must be divided only by scalars!")
        
        return Vector3(self.x / other, self.y / other, self.z / other)

    def get_magnitude(self) -> float:
        return np.sqrt(self.x**2 + self.y**2 + self.z**2).item()

    def get_normalized(self):
        mag = self.get_magnitude()
        if mag == 0:
            return Vector3()
        return self / mag
    
    def get_angle(self):
        return math.atan2(self.y, self.x)
    
    def cross(self, other):
        if type(other) is not Vector3:
            raise TypeError("Cross product is only defined between two 3D vectors!")
        
        return Vector3(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )
        
            
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

    def __sub__(self, other):
        if type(other) is not Vector4:
            raise TypeError("You can only subtract a 4D vector from a 4D vector!")
        return Vector4(self.x - other.x, self.y - other.y, self.z - other.z, self.w - other.w)

    def __mul__(self, other):
        if not (type(other) is int or type(other) is float):
            raise TypeError("Vectors must be only multiplied by scalars!")
        
        return Vector4(self.x * other, self.y * other, self.z * other, self.w * other)
    
    def __truediv__(self, other):
        if not (type(other) is int or type(other) is float):
            raise TypeError("Vectors must be only divided by scalars!")
        
        return Vector4(self.x / other, self.y / other, self.z / other, self.w / other)

    def get_magnitude(self):
        return np.sqrt(self.x**2 + self.y**2 + self.z**2 + self.w**2)
    
    def get_normalized(self):
        mag = self.get_magnitude()
        if mag == 0:
            return Vector4()
        return Vector4(self.x / mag, self.y / mag, self.z / mag, self.w / mag)