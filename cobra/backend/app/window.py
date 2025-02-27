import pygame

__all__ = [
    "Window"
]

class Window:
    def __init__(self, caption: str, size_x: int, size_y: int):
        pygame.init()
        self.__surface = pygame.display.set_mode((size_x, size_y), pygame.OPENGL | pygame.DOUBLEBUF)
        pygame.display.set_caption(caption)

        self.__should_quit = False

    def swap_buf(self) -> None:
        pygame.display.flip()

    def handle_events(self) -> None:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.__should_quit = True

    def should_close(self) -> bool:
        return self.__should_quit