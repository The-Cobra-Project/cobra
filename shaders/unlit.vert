#version 330 core

layout (location = 0) in vec2 vertexPosition;

void main() {
    gl_Position = vec3(vertexPosition, 0)
}