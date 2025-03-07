from cobra import *
from math import cos, sin

def main():
    wnd = Window("Game", Vector2(800, 600))

    model = load_mesh("./assets/3d/cube.obj")
    unlit = Shader("./assets/shaders/unlit.vert", "./assets/shaders/unlit.frag")

    camera = Camera(wnd, 70, 1, 100)
    trans = Transform()
    trans.scale /= 5

    radius = 10

    time = 0
    while not wnd.should_close():
        dt = wnd.tick(60)
        time += dt
        wnd.poll_events()

        # camera.position = Vector3(sin(time) * radius, 0, cos(time) * radius)
        # print(camera.get_mvp(trans)())
        # camera.position = Vector3(0, 0, 50)
        trans.position = Vector3(0, 0, -5)
        camera.position = Vector3(5, 0, 0)
        camera.look_at(trans.position)

        wnd.clear(Vector3(0.05, 0.05, 0.05))

        unlit.use()
        unlit.pass_mat4("mvp", camera.get_mvp(trans))
        unlit.pass_vec3("fragColor", Vector3(1, 1, 1))
        model.draw()

        wnd.swap_buf()

if __name__ == "__main__":

    main()