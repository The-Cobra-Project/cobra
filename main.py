import pygame
from OpenGL.GL import *
import numpy
import math

from engine import *

SHADERS_DIR = "./shaders"

pygame.init()
pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLEBUFFERS, 1)
pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLESAMPLES, 4)
screen = pygame.display.set_mode((800, 600), pygame.OPENGL | pygame.DOUBLEBUF)
pygame.display.set_caption("Engine Window")

glEnable(GL_MULTISAMPLE)

BG = (204/255, 230/255, 230/255, 1)

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

glEnable(GL_DEPTH_TEST)

model = Matrix4(identity=True)
model.scale(Vector3(0.5, 0.5, 0.5))
view = Matrix4(identity=True)
proj = Matrix4.perspective(800/600, math.radians(60), 0.8, 100)

should_close = False
clock = pygame.time.Clock()
t = 0

player_pos = Vector3(0, 0, -3)
move_speed = 2
last_mouse_pos = Vector2()
while not should_close:
    dt = clock.tick(240) / 1000

    mouse_pos = Vector2(*pygame.mouse.get_pos())

    view.rotate(Vector3(0, 1, 0), (mouse_pos.x - last_mouse_pos.x) * dt)

    last_mouse_pos = mouse_pos

    keys = pygame.key.get_pressed()
    velocity = Vector3(0, 0, 0)
    if keys[pygame.K_w]:
        velocity.z += 1
    if keys[pygame.K_s]:
        velocity.z -= 1
    if keys[pygame.K_a]:
        velocity.x += 1
    if keys[pygame.K_d]:
        velocity.x -= 1
    
    player_pos += velocity.get_normalized() * move_speed * dt
    view.translate(player_pos)

    

    pygame.display.set_caption(str(round(clock.get_fps())))

    glClearColor(BG[0], BG[1], BG[2], BG[3])
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    shader.use()
    shader.pass_mat4("mvp", model * view * proj)
    shader.pass_vec3("fragColor", Vector3(0.2, 0.2, 0.2))

    glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, None)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            should_close = True,

    t += dt