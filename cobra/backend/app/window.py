import pygame

__all__ = [
    "Window"
]

class Window:
    def __init__(self, caption: str, size_x: int, size_y: int):
        pygame.init()
        self.__surface = pygame.display.set_mode((size_x, size_y), pygame.OPENGL | pygame.DOUBLEBUF)
        self.__clock = pygame.time.Clock()
        pygame.display.set_caption(caption)

        self.__should_quit = False

    def tick(self, framerate) -> float:
        return self.__clock.tick(framerate) / 1000

    def swap_buf(self) -> None:
        pygame.display.flip()

    def poll_events(self) -> None:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.__should_quit = True

    def should_close(self) -> bool:
        return self.__should_quit