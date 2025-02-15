import pygame
from OpenGL.GL import *
import numpy

from engine import Matrix4, Shader

SHADERS_DIR = "./shaders"

screen = pygame.display.set_mode((800, 600), pygame.OPENGL | pygame.DOUBLEBUF)
pygame.display.set_caption("Engine Window")

BG = (30 / 255, 30 / 255, 30 / 255, 255 / 255)

vertices = numpy.array([
    -1, -1,
    0, 1,
    1, -1
], dtype=numpy.float32)

model = Matrix4(identity=True)

shader = Shader(f"{SHADERS_DIR}/unlit.vert", f"{SHADERS_DIR}/unlit.frag")

vao = glGenVertexArrays(1)
vbo = glGenBuffers(1)

glBindVertexArray(vao)
glBindBuffer(GL_ARRAY_BUFFER, vbo)
glBufferData(GL_ARRAY_BUFFER, vertices.size * 4, vertices, GL_STATIC_DRAW)
glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 2 * 4, None)
glEnableVertexAttribArray(0)

close = False
while not close:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close = True

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(BG[0], BG[1], BG[2], BG[3])

    shader.use()
    shader.pass_mat4("model", model)

    glDrawArrays(GL_TRIANGLES, 0, 3)

    pygame.display.flip()
