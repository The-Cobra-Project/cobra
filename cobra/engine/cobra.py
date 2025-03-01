from ..backend import *

__all__ = [
    "add_object",
    "init",
    "run"
]

def init():
    global app
    app = Application("Window", 800, 600)

def run():
    app.run()
