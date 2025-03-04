from cobra import * 

def main():
    wnd = Window("Game", Vector2(800, 600))
    
    model = load_mesh("./assets/3d/suzanne.obj")
    lit = Shader("./assets/shaders/lit.vert", "./assets/shaders/lit.frag")

    camera = Camera(wnd, 70, 1, 100)
    camera.transform.position.z = -5
    trans = Transform()

    lightPos = Vector3(4, 2, 7)

    while not wnd.should_close():
        dt = wnd.tick(60)
        wnd.poll_events()

        wnd.clear(Vector3(0.05, 0.05, 0.05))

        lit.use()
        lit.pass_mat4("mvp", camera.get_mvp(trans))
        lit.pass_mat4("model", trans.get_trans_matrix())
        lit.pass_vec3("lightPos", lightPos)
        lit.pass_vec3("viewPos", camera.transform.position),
        lit.pass_vec3("lightColor", Vector3(1, 1, 1))
        lit.pass_vec3("fragColor", Vector3(1, 1, 1))
        model.draw()

        wnd.swap_buf()

if __name__ == "__main__":
    main()