import numpy as np
from math import sin, cos

from .vector import *

__all__ = [
    "Matrix4"
]

class Matrix4:
    def __init__(self, identity=False) -> None:
        if identity:
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
    
    def __mul__(self, other): # TODO: FINISH VECTOR AND MATRIX MULTIPLICATIONS
        if type(other) is Vector3:
            return Vector3(
                other.x
            )

    def get_scale(self) -> Vector3:
        return Vector3(
            self.__mat[0][0],
            self.__mat[1][1],
            self.__mat[2][2]
        )

    def scale(self, vector: Vector3) -> None:
        self.__mat[0][0] = vector.x
        self.__mat[1][1] = vector.y
        self.__mat[2][2] = vector.z

    def translate(self, vector: Vector3) -> None:
        self.__mat[3][0] = vector.x
        self.__mat[3][1] = vector.y
        self.__mat[3][2] = vector.z
    
    def rotate(self, axis: Vector3, theta: float) -> None: # TODO: FINISH TRANSLATING THE MATRIX
        rotation_matrix = np.array[[
            [cos(theta) + axis.x**2 * (1 - cos(theta)), axis.x * axis.y * (1 - cos(theta)) - axis.z * sin(theta), axis.x * axis.z * (1 - cos(theta)) + axis.y * sin(theta), 0],
            [axis.y * axis.x * (1 - cos(theta)) + axis.z * sin(theta), cos(theta) + axis.y**2 * (1 - cos(theta)), axis.y * axis.z * (1 - cos(theta)) - axis.x * sin(theta), 0],
            [axis.z * axis.x * (1 - cos(theta)) - axis.y * sin(theta), axis.z * axis.y * (1 - cos(theta)) + axis.x * sin(theta), cos(theta) + axis.z**2 * (1 - cos(theta)), 0],
            [0, 0, 0, 1],
        ]]

        trans = self.get_translation()



