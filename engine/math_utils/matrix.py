import numpy as np

__all__ = [
    "Matrix4"
]

class Matrix4:
    def __init__(self, identity=False) -> None:
        if identity:
            self.mat = np.array([
                [1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]
            ])
        else:
            self.mat = np.array([
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ])

    def __call__(self, *args, **kwds):
        return self.mat