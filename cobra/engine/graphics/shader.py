from OpenGL.GL import *
from OpenGL.GL.shaders import compileShader, compileProgram

from cobra.engine.math import Matrix4, Vector3

__all__ = [
    "Shader"
]

class Shader:
    def __init__(self, vertex_path: str, fragment_path: str) -> None:
        vert_f = open(vertex_path, "r", encoding="utf-8")
        vert_src = vert_f.read()
        vertex_shader = compileShader(vert_src, GL_VERTEX_SHADER)

        frag_f = open(fragment_path, "r", encoding="utf-8")
        frag_src = frag_f.read()
        fragment_shader = compileShader(frag_src, GL_FRAGMENT_SHADER)

        self.__program = compileProgram(vertex_shader, fragment_shader)
        glDeleteShader(vertex_shader)
        glDeleteShader(fragment_shader)
        vert_f.close()
        frag_f.close()
        

    def use(self):
        glUseProgram(self.__program)

    def pass_bool(self, location: str, val: bool):
        glUniform1i(glGetUniformLocation(self.__program, location), val)

    def pass_mat4(self, location: str, mat: Matrix4) -> None:
        glUniformMatrix4fv(glGetUniformLocation(self.__program, location), 1, False, mat())

    def pass_vec3(self, location: str, vec: Vector3) -> None:
        glUniform3fv(glGetUniformLocation(self.__program, location), 1, vec())

