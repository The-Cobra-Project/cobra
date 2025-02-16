import numpy as np
from math import sin, cos, tan

from .vector import *

__all__ = [
    "Matrix4"
]

class Matrix4:
    def __init__(self, identity: bool=False, default: list=None) -> None:
        if default is not None:
            self.__mat = np.array(default, dtype=np.float32)
        elif identity:
            self.__mat = np.array([
                [1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]
            ],dtype=np.float32)
        else:
            self.__mat = np.array([
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ], dtype=np.float32)

    def __call__(self, *args, **kwds):
        return self.__mat
    
    def __add__(self, other):
        if not isinstance(other, Matrix4):
            raise TypeError("Addition between matrices should include same sized matrices!")
        
        return Matrix4(False, (self.__mat + other()).tolist())

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Matrix4(False, (self.__mat * other).tolist())
        elif isinstance(other, Matrix4):
            return Matrix4(False, np.matmul(self.__mat, other()).tolist())
        elif isinstance(other, Vector4):
            return Vector4(*np.dot(self.__mat, other()))
        else:
            raise TypeError("Multiplication with unsupported type")

    def get_scale(self) -> Vector3:
        return Vector3(
            self.__mat[0][0],
            self.__mat[1][1],
            self.__mat[2][2]
        )
    
    def get_translation(self) -> Vector3:
        return Vector3(
            self.__mat[3][0],
            self.__mat[3][1],
            self.__mat[3][2]
        )

    def scale(self, vector: Vector3) -> None:
        self.__mat[0][0] = vector.x
        self.__mat[1][1] = vector.y
        self.__mat[2][2] = vector.z

    def translate(self, vector: Vector3 | Vector4) -> None:
        self.__mat[3][0] = vector.x
        self.__mat[3][1] = vector.y
        self.__mat[3][2] = vector.z
    
    def rotate(self, axis: Vector3, theta: float) -> None:
        rotation_matrix = Matrix4(False, [
            [cos(theta) + axis.x**2 * (1 - cos(theta)), axis.x * axis.y * (1 - cos(theta)) - axis.z * sin(theta), axis.x * axis.z * (1 - cos(theta)) + axis.y * sin(theta), 0],
            [axis.y * axis.x * (1 - cos(theta)) + axis.z * sin(theta), cos(theta) + axis.y**2 * (1 - cos(theta)), axis.y * axis.z * (1 - cos(theta)) - axis.x * sin(theta), 0],
            [axis.z * axis.x * (1 - cos(theta)) - axis.y * sin(theta), axis.z * axis.y * (1 - cos(theta)) + axis.x * sin(theta), cos(theta) + axis.z**2 * (1 - cos(theta)), 0],
            [0, 0, 0, 1]
        ])

        self.__mat = (self * rotation_matrix)()

    @staticmethod
    def perspective(aspect_ratio: float, fov_x: float, z_near: float, z_far: float):
        tangent = tan(fov_x / 2)
        right = z_far * tangent
        top = right / aspect_ratio
        return Matrix4(False, [
            [z_far / right, 0, 0, 0],
            [0, z_far / top, 0, 0],
            [0, 0, -(z_near + z_far) / (z_far - z_near), -2 * z_near * z_far / (z_far - z_near)],
            [0, 0, -1, 0]
        ])

