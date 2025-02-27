import pygame

__all__ = [
    "Window"
]

class Window:
    def __init__(self, caption: str, size_x: int, size_y: int):
        pygame.init()
        self.__surface = pygame.display.set_mode((size_x, size_y), pygame.OPENGL | pygame.DOUBLEBUF)
        pygame.display.set_caption(caption)

    def swap_buf(self) -> None:
        pygame.display.flip()

    def should_close(self) -> bool:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return True
        return False