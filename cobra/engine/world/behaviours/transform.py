from ..behaviour import *

from ...math import *

__all__ = [
    "Transform"
]

class Transform(Behaviour):
    position = Vector3()
    rotation = Vector3()
    scale = Vector3(1, 1, 1)

    def __call__(self) -> Matrix4:
        transform = Matrix4(True)
        transform.translate(self.position)
        transform.rotate(Vector3(1, 0, 0), self.rotation.x)
        transform.rotate(Vector3(0, 1, 0), self.rotation.y)
        transform.rotate(Vector3(0, 0, 1), self.rotation.z)
        transform.scale(self.scale)
        
        return transform