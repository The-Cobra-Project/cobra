from ..graphics import Window
from ..math import *
from .transform import *

__all__ = [
    "Camera"
]

class Camera:
    def __init__(self, wnd: Window, fov: float, near_plane: float, far_plane: float) -> None:
        self.transform = Transform()

        size: Vector2 = wnd.get_dimensions()
        self.__proj_matrix = Matrix4.perspective(size.x / size.y, fov, near_plane, far_plane)

    def get_mvp(self, model: Transform) -> Matrix4:
        return model.get_trans_matrix() * self.transform.get_trans_matrix() * self.__proj_matrix