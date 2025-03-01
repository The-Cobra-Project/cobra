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
    camera.transform.position.z = -2

    trans1 = Transform()
    trans1.position.x = -1
    trans1.scale = Vector3(0.7, 0.7, 0.7)

    trans2 = Transform()
    trans2.position.x = 1
    trans2.scale = Vector3(0.7, 0.7, 0.7)

    print(trans1.get_trans_matrix()())
    print(trans2.get_trans_matrix()())

    while not wnd.should_close():
        dt = wnd.tick(60)
        wnd.poll_events()

        wnd.clear()

        s.use()
        s.pass_mat4("mvp", camera.get_mvp(trans1))
        s.pass_vec3("fragColor", Vector3(249/255, 139/255, 133/255))
        m.draw()

        s.pass_mat4("mvp", camera.get_mvp(trans2))
        s.pass_vec3("fragColor", Vector3(144/255, 213/255, 255/255))
        m.draw()

        wnd.swap_buf()

if __name__ == "__main__":
    main()