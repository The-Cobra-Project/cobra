from engine.math_utils import Vector2
from .window import Window

__all__ = [
    "Application"
]

class Application:
    def __init__(self, caption: str, dimensions: Vector2):
        self.__window = Window(caption, dimensions.x, dimensions.y)

    def run(self) -> None:
        while not self.__window.should_close():
            self.__window.handle_events()
            
            self.__window.swap_buf()
            