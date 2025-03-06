from ..math import *

import pygame
from OpenGL.GL import *

__all__ = [
    "Window"
]

class Window:
    def __init__(self, caption: str, dimensions: Vector2):
        pygame.init()
        self.__surface = pygame.display.set_mode((dimensions.x, dimensions.y), pygame.OPENGL | pygame.DOUBLEBUF)
        self.__clock = pygame.time.Clock()
        pygame.display.set_caption(caption)

        glEnable(GL_DEPTH_TEST)

        self.__should_quit = False

    def tick(self, framerate) -> float:
        return self.__clock.tick(framerate) / 1000

    def clear(self, color: Vector3):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glClearColor(*color(), 1)

    def swap_buf(self) -> None:
        pygame.display.flip()

    def poll_events(self) -> None:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.__should_quit = True

    def should_close(self) -> bool:
        return self.__should_quit
    
    def get_dimensions(self) -> Vector2:
        return Vector2(*self.__surface.get_size())