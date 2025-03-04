from .graphics.mesh import *
from .math import *

__all__ = [
    "load_mesh"
]

def load_mesh(path: str) -> Mesh:
    if not path.endswith(".obj"): raise "Mesh file must be of wavefront (.obj) type!"
    vertices: list[Vector3] = []
    indices: list[int] = []
    normals: list[Vector3] = []
    with open(path, "r") as file:
        data = file.read()
        lines = data.splitlines()
        for l in lines:
            words = l.split()
            while "" in words:
                words.remove("")
            if len(words) == 0: continue
            if words[0] == "#": continue
            if words[0] == "v":
                vertices.append(Vector3(float(words[1]), float(words[2]), float(words[3])))
            if words[0] == "f":
                for vertex in words[1:]:
                    indices_lst = vertex.split("/")
                    indices.append(int(indices_lst[0]) - 1)
            if words[0] == "vn":
                normals.append(Vector3(words[1], words[2], words[3]))

        return Mesh(vertices, indices, normals)
