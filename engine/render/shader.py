from OpenGL.GL import *
from OpenGL.GL.shaders import compileShader, compileProgram

from engine.math_utils.matrix import Matrix4

class Shader:
    def __init__(self, vertex_path: str, fragment_path: str) -> None:
        vert_src = open(vertex_path, "r").read()
        vertex_shader = compileShader(vert_src, GL_VERTEX_SHADER)

        frag_src = open(fragment_path, "r").read()
        fragment_shader = compileShader(frag_src, GL_FRAGMENT_SHADER)

        self.program = compileProgram(vertex_shader, fragment_shader)
        glDeleteShader(vertex_shader)
        glDeleteShader(fragment_shader)

    def use(self):
        glUseProgram(self.program)

    def pass_mat4(self, location: str, mat: Matrix4) -> None:
        glUniformMatrix4fv(glGetUniformLocation(self.program, location), 1, False, mat())