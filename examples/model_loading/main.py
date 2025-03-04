from cobra import *
import random
from math import radians

def main():
    wnd = Window("Game", Vector2(800, 600))

    ogre = load_mesh("./assets/3d/ogre.obj")
    bunny = load_mesh("./assets/3d/stanford-bunny.obj")
    nefertiti = load_mesh("./assets/3d/nefertiti.obj")

    unlit = Shader("./assets/shaders/unlit.vert", "./assets/shaders/unlit.frag")

    camera = Camera(wnd, 70, 1, 100)
    camera.transform.position.z = -5

    ogre_trans = Transform()
    ogre_trans.position = Vector3(random.uniform(-3, 3), random.uniform(-3, 3), random.uniform(-3, 3))
    ogre_trans.scale /= 20

    bunny_trans = Transform()
    bunny_trans.position = Vector3(random.uniform(-3, 3), random.uniform(-3, 3), random.uniform(-3, 3))
    bunny_trans.scale *= 10

    nefertiti_trans = Transform()
    nefertiti_trans.position = Vector3(random.uniform(-3, 3), random.uniform(-3, 3), random.uniform(-3, 3))
    nefertiti_trans.rotation.x = radians(90)
    nefertiti_trans.scale /= 160

    while not wnd.should_close():
        dt = wnd.tick(60)
        wnd.poll_events()

        ogre_trans.rotation.y += dt
        bunny_trans.rotation.y += dt
        nefertiti_trans.rotation.y += dt

        wnd.clear(Vector3(0.05, 0.05, 0.05))

        unlit.use()
        unlit.pass_bool("debug", True)
        unlit.pass_mat4("mvp", camera.get_mvp(ogre_trans))
        unlit.pass_vec3("fragColor", Vector3(1, 0.6, 0.6))
        ogre.draw()

        unlit.pass_mat4("mvp", camera.get_mvp(bunny_trans))
        unlit.pass_vec3("fragColor", Vector3(1, 1, 1))
        bunny.draw()

        unlit.pass_mat4("mvp", camera.get_mvp(nefertiti_trans))
        unlit.pass_vec3("fragColor", Vector3(1, 1, 1))
        nefertiti.draw()

        wnd.swap_buf()

if __name__ == "__main__":
    main()