#version 330 core

layout (location = 0) in vec3 vertexPosition;
layout (location = 1) in vec3 vertexNormal;

uniform mat4 mvp;
uniform mat4 model;

out vec3 FragPos;
out vec3 Normal;

void main() {
    vec4 res = mvp * vec4(vertexPosition, 1.0);
    gl_Position = res;
    FragPos = vec3(model * vec4(vertexPosition, 1.0));
    Normal = vertexNormal;
}
