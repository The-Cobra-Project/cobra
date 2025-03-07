from OpenGL.GL import *
import numpy as np

from ..math.vector import Vector3

__all__ = [
    "Mesh"
]

class Mesh:
    def __init__(self, vertices: list[Vector3], indices: list[int], normals: list[Vector3]):
        self.__vertices = vertices
        self.__indices = indices

        self.__vao = glGenVertexArrays(1)
        vbo = glGenBuffers(1)
        normal_buff = glGenBuffers(1)
        self.__ebo = glGenBuffers(1)

        glBindVertexArray(self.__vao)

        glBindBuffer(GL_ARRAY_BUFFER, vbo)
        raw_vert = self.__list_vec3_to_arr(vertices)
        glBufferData(GL_ARRAY_BUFFER, raw_vert.size * 4, raw_vert, GL_STATIC_DRAW)

        glVertexAttribPointer(0, 3, GL_FLOAT, False, 12, None)
        glEnableVertexAttribArray(0)

        glBindBuffer(GL_ARRAY_BUFFER, normal_buff)
        raw_normals = self.__list_vec3_to_arr(normals)
        glBufferData(GL_ARRAY_BUFFER, raw_normals.size * 4, raw_normals, GL_STATIC_DRAW)

        glVertexAttribPointer(1, 3, GL_FLOAT, False, 12, None)
        glEnableVertexAttribArray(1)

        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.__ebo)
        raw_indices = np.array(indices, dtype=np.int32)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, raw_indices.size * 4, raw_indices, GL_STATIC_DRAW)

        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0)

        glBindVertexArray(0)


    def __list_vec3_to_arr(self, lst: list[Vector3]):
        n = []
        for v in lst:
            n.append(v.x)
            n.append(v.y)
            n.append(v.z)

        return np.array(n, dtype=np.float32)

    def draw(self):
        glBindVertexArray(self.__vao)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.__ebo)
        glDrawElements(GL_TRIANGLES, len(self.__indices), GL_UNSIGNED_INT, None)
        glBindVertexArray(0)