from OpenGL.GL import *
import numpy as np

from ..math.vector import Vector3

__all__ = [
    "Mesh"
]

class Mesh:
    def __init__(self, vertices: list[Vector3], indices: list[int]):
        self.__vertices = vertices
        self.__vao = glGenVertexArrays(1)
        glBindVertexArray(self.__vao)

        self.__add_vertex_attrib(self.__list_vec3_to_arr(vertices), 0, 3, GL_FLOAT, False)

        glBindVertexArray(0)

    def __add_vertex_attrib(self, data: list, index: int, size: int, type: int, normalize: bool):
        vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, vbo)
        glBufferData(GL_ARRAY_BUFFER, len(data) * 4, data, GL_STATIC_DRAW)

        glVertexAttribPointer(index, size, type, normalize, size * 4, None)
        glEnableVertexAttribArray(index)

        glBindBuffer(GL_ARRAY_BUFFER, 0)

    def __list_vec3_to_arr(self, lst: list[Vector3]):
        n = []
        for v in lst:
            n.append(v.x)
            n.append(v.y)
            n.append(v.z)

        return np.array(n, dtype=np.float32)

    def draw(self):
        glBindVertexArray(self.__vao)
        glDrawArrays(GL_TRIANGLES, 0, len(self.__vertices))