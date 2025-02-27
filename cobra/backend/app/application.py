from .window import Window

__all__ = [
    "Application"
]

class Application:
    def __init__(self, caption: str, size_x: int, size_y: int):
        self.__window = Window(caption, size_x, size_y)

    def run(self) -> None:
        while not self.__window.should_close():
            self.__window.handle_events()
            
            self.__window.swap_buf()
            