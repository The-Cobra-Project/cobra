from .graphics.mesh import *
from .math import *

__all__ = [
    "load_mesh"
]

def load_mesh(path: str) -> Mesh:
    if not path.endswith(".obj"):
        raise ValueError("Mesh file must be of wavefront (.obj) type!")
    
    vertices: list[Vector3] = []
    indices: list[int] = []
    normals: list[Vector3] = []
    vertex_normals: list[Vector3] = []
    has_normal_data = False
    
    with open(path, "r") as file:
        data = file.read()
        lines = data.splitlines()
        for l in lines:
            words = l.split()
            while "" in words:
                words.remove("")
            if not words: continue
            if words[0] == "#": continue
            
            if words[0] == "v":
                vertices.append(Vector3(float(words[1]), float(words[2]), float(words[3])))
                vertex_normals.append(Vector3(0, 0, 0))
            elif words[0] == "vn":
                has_normal_data = True
                normals.append(Vector3(float(words[1]), float(words[2]), float(words[3])))
            elif words[0] == "f":
                face_vertices = []
                for vertex in words[1:]:
                    vertex_data = vertex.split('/')
                    vertex_idx = int(vertex_data[0]) - 1  # Convert to 0-based indexing
                    
                    # Handle normal index if present
                    if len(vertex_data) >= 3 and vertex_data[2]:
                        normal_idx = int(vertex_data[2]) - 1
                        vertex_normals[vertex_idx] = normals[normal_idx]
                    
                    face_vertices.append(vertex_idx)
                
                # Triangulate the face (fan triangulation)
                for i in range(1, len(face_vertices) - 1):
                    indices.extend([
                        face_vertices[0],
                        face_vertices[i],
                        face_vertices[i + 1]
                    ])

    # If no normals were found in the file, generate them
    if True:
        # Reset vertex normals
        vertex_normals = [Vector3(0, 0, 0) for _ in range(len(vertices))]
        
        # Calculate normals for each triangle
        for i in range(0, len(indices), 3):
            v0 = vertices[indices[i]]
            v1 = vertices[indices[i + 1]]
            v2 = vertices[indices[i + 2]]
            
            # Calculate triangle edges
            edge1 = v1 - v0
            edge2 = v2 - v0
            
            # Calculate normal using cross product
            normal = edge1.cross(edge2).get_normalized()
            
            # Add this normal to all three vertices of the triangle
            vertex_normals[indices[i]] += normal
            vertex_normals[indices[i + 1]] += normal
            vertex_normals[indices[i + 2]] += normal
        
        # Normalize all vertex normals
        for i in range(len(vertex_normals)):
            if vertex_normals[i].get_magnitude() > 0:
                vertex_normals[i] = vertex_normals[i].get_normalized()

    return Mesh(vertices, indices, vertex_normals)