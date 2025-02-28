from .window import Window

from ...engine.world import Obj

__all__ = [
    "Application"
]

class Application:
    def __init__(self, caption: str, size_x: int, size_y: int):
        self.__window = Window(caption, size_x, size_y)
        self.__objects: list[Obj] = []

    def run(self) -> None:
        while not self.__window.should_close():
            dt = self.__window.tick(60)
            self.__window.poll_events()
            for o in self.__objects:
                o.tick(dt)

            for o in self.__objects:
                o.render()
            self.__window.swap_buf()

    def add_object(self, obj: Obj):
        self.__objects.append(obj)
