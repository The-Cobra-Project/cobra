from cobra import * 

def main():
    wnd = Window("Game", Vector2(800, 600))

    teapot = load_mesh("./assets/3d/teapot.obj")
    bunny = load_mesh("./assets/3d/bunny.obj")
    unlit = Shader("./assets/shaders/unlit.vert", "./assets/shaders/unlit.frag")

    camera = Camera(wnd, 70, 1, 100)
    camera.transform.position.z = -3
    teapot_trans = Transform()
    teapot_trans.position = Vector3(1, -1, 0)
    teapot_trans.scale /= 100

    bunny_trans = Transform()
    bunny_trans.position = Vector3(-1, -1, 0)

    while not wnd.should_close():
        dt = wnd.tick(60)
        wnd.poll_events()

        teapot_trans.rotation.y += dt
        bunny_trans.rotation.y += dt

        wnd.clear(Vector3(0.05, 0.05, 0.05))

        unlit.use()
        unlit.pass_bool("debug", False)
        unlit.pass_mat4("mvp", camera.get_mvp(teapot_trans))
        unlit.pass_vec3("fragColor", Vector3(1, 0.6, 0.6))
        teapot.draw()

        unlit.pass_bool("debug", True)
        unlit.pass_mat4("mvp", camera.get_mvp(bunny_trans))
        unlit.pass_vec3("fragColor", Vector3(1, 1, 1))
        bunny.draw()

        wnd.swap_buf()

if __name__ == "__main__":
    main()