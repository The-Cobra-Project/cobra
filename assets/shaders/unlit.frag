#version 330 core

uniform vec3 fragColor;
uniform bool debug;
out vec4 FragColor;

in vec3 norm;

void main() {
    if (debug)
        FragColor = vec4(norm, 1);
    else
        FragColor = vec4(fragColor, 1);
}
