from ..backend import *
from .world import *

__all__ = [
    "add_object",
    "init",
    "run"
]


def add_object(obj: Obj):
    app.add_object(obj)

def init():
    global app
    app = Application("Window", 800, 600)

def run():
    app.run()
