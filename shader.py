from OpenGL.GL import *
from OpenGL.GL.shaders import compileShader, compileProgram

class Shader:
    def __init__(self, vertex_path, fragment_path):
        vert_src = open(vertex_path, "r").read()
        vertex_shader = compileShader(vert_src, GL_VERTEX_SHADER)

        frag_src = open(fragment_path, "r").read()
        fragment_shader = compileShader(frag_src, GL_FRAGMENT_SHADER)

        self.program = compileProgram(vertex_shader, fragment_shader)
        glDeleteShader(vertex_shader)
        glDeleteShader(fragment_shader)

    def use(self):
        glUseProgram(self.program)