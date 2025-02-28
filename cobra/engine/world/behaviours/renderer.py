from ..behaviour import *
from ...graphics import *
from ...math import *

__all__ = [
    "Renderer"
]

class Renderer(Behaviour):
    def set_mesh(self, mesh: Mesh):
        self.mesh = mesh

    def set_shader(self, shader: Shader):
        self.shader = shader

    def render(self):
        self.shader.use()
        self.shader.pass_mat4()
        self.shader.pass_vec3("fragColor", Vector3(1, 1, 1))
        self.mesh.draw()