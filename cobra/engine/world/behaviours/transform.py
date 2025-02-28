from ..behaviour import *

from ...math import *

__all__ = [
    "Transform"
]

class Transform(Behaviour):
    def __init__(self):
        self.position = Vector3()
        self.rotation = Vector3()
        self.scale = Vector3()

    def __call__(self):
        transform = Matrix4(True)
        transform.translate(self.position)
        transform.rotate(Vector3(1, 0, 0), self.rotation.x)
        transform.rotate(Vector3(0, 1, 0), self.rotation.y)
        transform.rotate(Vector3(0, 0, 1), self.rotation.z)
        transform.scale(self.scale)
        