from ..graphics import Window
from ..math import *
from .transform import *

__all__ = [
    "Camera"
]

class Camera:
    def __init__(self, wnd: Window, fov: float, near_plane: float, far_plane: float) -> None:
        self.position = Vector3()
        self.scale = Vector3()
        self.rotation = Vector3()
        self.__view = Matrix4(True)

        size: Vector2 = wnd.get_dimensions()
        self.__proj_matrix = Matrix4.perspective(size.x / size.y, fov, near_plane, far_plane)

    def look_at(self, target: Vector3):
        up = Vector3(0, 1, 0)
        cam_direction = (self.position - target).get_normalized()
        cam_right = up.cross(cam_direction).get_normalized()
        cam_up = cam_direction.cross(cam_right)
        self.__view = Matrix4.look_at(self.position, cam_direction, cam_right, cam_up)


    def get_mvp(self, model: Transform) -> Matrix4:
        return model.get_trans_matrix() * self.__view * self.__proj_matrix