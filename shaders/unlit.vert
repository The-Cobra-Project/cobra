#version 330 core

layout (location = 0) in vec3 vertexPosition;

uniform mat4 model;
uniform mat4 view;
uniform mat4 proj;

void main() {
    vec4 res = proj * view * model * vec4(vertexPosition, 1.0);
    gl_Position = res;
}
