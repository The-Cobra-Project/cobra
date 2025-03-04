#version 330 core

in vec3 FragPos;
in vec3 Normal;

out vec4 FragColor;

uniform vec3 lightPos;
uniform vec3 viewPos;
uniform vec3 lightColor;
uniform vec3 objectColor;

// Material properties
uniform float ambientStrength = 0.1;
uniform float specularStrength = 0.5;
uniform float shininess = 32.0;

void main()
{
    // Normalize the normal vector
    vec3 norm = normalize(Normal);
    
    // Calculate light direction
    vec3 lightDir = normalize(lightPos - FragPos);
    
    // Ambient component
    vec3 ambient = ambientStrength * lightColor;
    
    // Diffuse component
    float diff = max(dot(norm, lightDir), 0.0);
    vec3 diffuse = diff * lightColor;
    
    // Specular component
    vec3 viewDir = normalize(viewPos - FragPos);
    vec3 reflectDir = reflect(-lightDir, norm);
    float spec = pow(max(dot(viewDir, reflectDir), 0.0), shininess);
    vec3 specular = specularStrength * spec * lightColor;
    
    // Combine all components
    vec3 result = (ambient + diffuse + specular) * objectColor;
    FragColor = vec4(result, 1.0);
}