#version 330 core

uniform vec3 fragColor;
out vec4 FragColor;

void main() {
    FragColor = vec4(fragColor, 1);
}
