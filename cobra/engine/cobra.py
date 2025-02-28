from ..backend import *
from .world import *

__all__ = [
    "add_object"
]

app = Application("Window", 800, 600)

def add_object(obj: Obj):
    app.add_object(obj)

app.run()
