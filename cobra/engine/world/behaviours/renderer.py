from ..behaviour import *
from ...graphics import *
from ...math import *

from math import radians

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
        self.shader.pass_mat4("mvp", self.obj.transform() * Matrix4.perspective(800/600, radians(60), 0.9, 3))
        self.shader.pass_vec3("fragColor", Vector3(255/255, 225/255, 53/255))
        self.mesh.draw()