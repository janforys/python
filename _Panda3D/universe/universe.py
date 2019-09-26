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

        self.loadCube()

    def loadCube(self):
        self.cube = loader.loadModel("models/cube.glb")
        self.cube.reparentTo(render)
        self.cube.setPos(10, 0, 0)
        self.cube.setScale(4 * self.sizescale)

        self.sun = loader.loadModel("models/sun.glb")
        self.sun.reparentTo(render)

w = World()

base.run()