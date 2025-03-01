from ..math import *

__all__ = [
    "Transform"
]

class Transform:
    def __init__(self, start_position: Vector3 = Vector3(), start_rotation: Vector3 = Vector3(), start_scale: Vector3 = Vector3(1, 1, 1)):
        self.position = start_position
        self.rotation = start_rotation
        self.scale = start_scale

    def get_trans_matrix(self):
        trans = Matrix4(True)
        trans.translate(self.position)
        trans.rotate(Vector3(1, 0, 0), self.rotation.x)
        trans.rotate(Vector3(0, 1, 0), self.rotation.y)
        trans.rotate(Vector3(0, 0, 1), self.rotation.z)
        trans.scale(self.scale)
        return trans