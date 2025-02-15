import pygame
from OpenGL.GL import *
import numpy

from engine import *

SHADERS_DIR = "./shaders"

screen = pygame.display.set_mode((800, 600), pygame.OPENGL | pygame.DOUBLEBUF)
pygame.display.set_caption("Engine Window")

BG = (30/255, 30/255, 30/255, 255/255)

shader = Shader(f"{SHADERS_DIR}/unlit.vert", f"{SHADERS_DIR}/unlit.frag")

vertices = numpy.array([
     1,  1, 0,
     1, -1, 0,
    -1, -1, 0,
    -1,  1, 0
], dtype=numpy.float32)
indices = numpy.array([
    0, 1, 3,
    1, 2, 3
], dtype=numpy.int32)

model = Matrix4(identity=True)
model.scale(Vector3(0.5, 0.5, 1))

vao = glGenVertexArrays(1)
vbo = glGenBuffers(1)
ebo = glGenBuffers(1)

glBindVertexArray(vao)

glBindBuffer(GL_ARRAY_BUFFER, vbo)
glBufferData(GL_ARRAY_BUFFER, vertices.size * 4, vertices, GL_STATIC_DRAW)

glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ebo)
glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices.size * 4, indices, GL_STATIC_DRAW)

glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * 4, None)
glEnableVertexAttribArray(0)

should_close = False
clock = pygame.time.Clock()
t = 0
while not should_close:
    dt = clock.tick(60) / 1000
    
    model.rotate(Vector3(0, 0, 1), dt)

    glClearColor(BG[0], BG[1], BG[2], BG[3])
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    shader.use()
    shader.pass_mat4("model", model)
    
    glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, None)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            should_close = True

    t += dt