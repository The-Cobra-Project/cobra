from ..math import *
from math import acos

__all__ = [
    "Transform"
]

class Transform:
    def __init__(self):
        self.position = Vector3()
        self.rotation = Vector3()
        self.scale = Vector3(1, 1, 1)

    def get_trans_matrix(self):
        trans = Matrix4(True)
        trans.scale(self.scale)
        trans.rotate(Vector3(1, 0, 0), self.rotation.x)
        trans.rotate(Vector3(0, 1, 0), self.rotation.y)
        trans.rotate(Vector3(0, 0, 1), self.rotation.z)
        trans.translate(self.position)
        return trans