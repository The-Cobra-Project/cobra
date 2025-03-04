#version 330 core

layout (location = 0) in vec3 vertexPosition;
layout (location = 1) in vec3 normal;

uniform mat4 mvp;
out vec3 norm;

void main() {
    gl_Position = mvp * vec4(vertexPosition, 1.0);
    norm = normal;
}
