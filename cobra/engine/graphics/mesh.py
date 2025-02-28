from OpenGL.GL import *

import numpy as np

__all__ = [
    "Mesh"
]

class Mesh:
    def __init__(self, vertices: list[float], indices: list[int]):
        self.__vao = glGenVertexArrays()
        glBindVertexArray(self.__vao)

        vbo = glGenBuffers()
        glBindBuffer(GL_ARRAY_BUFFER, vbo)
        glBufferData(GL_ARRAY_BUFFER, len(vertices) * 4, np.array(vertices), GL_STATIC_DRAW)