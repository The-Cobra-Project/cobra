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
        if type(other) is not Matrix4:
            raise TypeError("Addition between matrices should include same sized matrices!")
        
        lst = [[], [], [], []]
        for x, y in np.ndindex(self.__mat.shape):
            lst[x].insert(y, self.__mat[x][y] + other()[x][y])
        
        return Matrix4(False, lst)

    def __mul__(self, other):
        if type(other) is int or type(other) is float:
            lst = [[], [], [], []]
            for x, y in np.ndindex(self.__mat.shape):
                lst[x].insert(y, self.__mat[x][y] * other)
            return Matrix4(False, lst)
        elif type(other) is Matrix4:
            lst = [[], [], [], []]
            for i in range(4):
                for j in range(4):
                    n = 0
                    for k in range(4):
                        n += self.__mat[i][k] * other()[k][j]
                    lst[i].insert(j, n)
            return Matrix4(False, lst)
        elif type(other) is Vector4:
            vec = []
            for i in range(4):
                for j in range(1):
                    n = 0
                    for k in range(4):
                        n += self.__mat[i][k] * other()[k]
                    vec.insert(i, n)
            return Vector4(vec[0], vec[1], vec[2], vec[3])

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
        height = z_near * tangent
        width = height * aspect_ratio
        return Matrix4(False, [
            [z_near / width, 0, 0, 0],
            [0, z_near / height, 0, 0],
            [0, 0, -(z_far + z_near) / (z_far - z_near), -2 * z_far * z_near / (z_far - z_near)],
            [0, 0, -1, 0]
        ])

