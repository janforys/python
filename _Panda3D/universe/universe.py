from direct.showbase.ShowBase import ShowBase
base = ShowBase()

from panda3d.core import *
from direct.gui.DirectGui import *

import sys


class World(object):
    def __init__(self):
        self.title = OnscreenText(
            text="Universe",
            parent=base.a2dBottomLeft, align=TextNode.A_left,
            style=1, fg=(1, 1, 1, 1), pos=(0.03, 0.05), scale=.1
        )

        base.setBackgroundColor(0.5, 0.5, 0)

        base.disableMouse()

        camera.setPos(0, 0, 45)

        camera.setHpr(0, -90, 0)

w = World()

base.run()