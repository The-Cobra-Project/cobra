import numpy

class Matrix4:
    def __init__(self, identity=False):
        if identity:
            self.mat = numpy.array([
                [1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]
            ])
        else:
            self.mat = numpy.array([
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ])

    def __call__(self, *args, **kwds):
        return self.mat