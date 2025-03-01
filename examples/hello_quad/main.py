from cobra import * 

def main():
    wnd = Window("Game", Vector2(800, 600))

    m = Mesh([
        Vector3( 1,  1, 0),
        Vector3( 1, -1, 0),
        Vector3(-1, -1, 0),
        Vector3(-1,  1, 0)
    ], [
        0, 1, 3,
        1, 2, 3
    ])
    s = Shader("./assets/shaders/unlit.vert", "./assets/shaders/unlit.frag")

    camera = Camera(wnd, 70, 1, 100)
    camera.transform.position.z = -1
    triangle_transform = Transform()

    while not wnd.should_close():
        dt = wnd.tick(60)
        wnd.poll_events()

        wnd.clear()

        s.use()
        s.pass_mat4("mvp", camera.get_mvp(triangle_transform))
        s.pass_vec3("fragColor", Vector3(1, 1, 1))
        m.draw()

        wnd.swap_buf()

if __name__ == "__main__":
    main()