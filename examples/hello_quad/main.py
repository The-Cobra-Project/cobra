from cobra import * 

def main():
    wnd = Window("Game", Vector2(800, 600))

    quad = Mesh([
        Vector3( 1,  1, 0),
        Vector3( 1, -1, 0),
        Vector3(-1, -1, 0),
        Vector3(-1,  1, 0)
    ], [
        0, 1, 3,
        1, 2, 3
    ])
    unlit = Shader("./assets/shaders/unlit.vert", "./assets/shaders/unlit.frag")

    camera = Camera(wnd, 70, 1, 100)
    camera.transform.position.z = -3
    trans = Transform()

    while not wnd.should_close():
        dt = wnd.tick(60)
        wnd.poll_events()

        wnd.clear()

        unlit.use()
        unlit.pass_mat4("mvp", camera.get_mvp(trans))
        unlit.pass_vec3("fragColor", Vector3(1, 1, 1))
        quad.draw()

        wnd.swap_buf()

if __name__ == "__main__":
    main()