from direct.showbase.ShowBase import ShowBase
base = ShowBase()

from panda3d.core import *
from direct.gui.DirectGui import *

import sys
import gltf


class World(object):
    def __init__(self):
        self.title = OnscreenText(
            text="Universe",
            parent=base.a2dBottomLeft, align=TextNode.A_left,
            style=1, fg=(1, 1, 1, 1), pos=(0.03, 0.05), scale=.1
        )

        base.setBackgroundColor(0.5, 0.5, 0)
        base.disableMouse()
        camera.setPos(0, 5, 45)
        camera.setHpr(0, -90, 0)

        self.sizescale = 0.5

        self.loadPlanets()

    def loadPlanets(self):

        self.sky = loader.loadModel("meshes/sky.glb")
        self.sky.reparentTo(render)
        self.sky.setScale(4)
        self.sky.setPos(0, 5, -25)
        self.sky_tex = loader.loadTexture("textures/sky_stars.jpg")
        self.sky.setTexture(self.sky_tex, 1)

        self.earth = loader.loadModel("meshes/earth.glb")
        self.earth.reparentTo(render)
        self.earth.setPos(10, 0, 0)
        self.earth.setScale(4 * self.sizescale)

        self.sun = loader.loadModel("meshes/sun.glb")
        self.sun.reparentTo(render)

w = World()
base.run()