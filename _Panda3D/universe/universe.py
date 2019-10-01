from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
from direct.gui.DirectGui import *
from direct.showbase.DirectObject import DirectObject

import sys
import gltf

base = ShowBase()

class World(object):

    def genLabelText(self, text, i):
        return  OnscreenText(text=text, pos=(0.06, -.06 * (i + 0.5)), fg=(1, 1, 1, 1),
                            parent=base.a2dTopLeft,align=TextNode.ALeft, scale=.05)

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
        self.yearscale = 60
        self.dayscale = self.yearscale / 365.0 * 10

        self.loadPlanets()
        self.rotatePlanets()

    def loadPlanets(self):

        self.orbit_root_earth = render.attachNewNode('orbit_root_earth')

        # Sky Sphere
        self.sky = loader.loadModel("meshes/sky2.glb")
        self.sky.reparentTo(render)
        self.sky.setScale(4)
        self.sky.setPos(0, 5, -25)
        self.sky_tex = loader.loadTexture("textures/stars_1k_tex.jpg")
        self.sky.setTexture(self.sky_tex, 1)

        # Sun
        self.sun = loader.loadModel("meshes/sun.glb")
        self.sun.reparentTo(render)
        self.sun_tex = loader.loadTexture("textures/sun_tex.jpg")
        self.sun.setTexture(self.sun_tex, 1)

        # Earth
        self.earth = loader.loadModel("meshes/earth.glb")
        self.earth.reparentTo(self.orbit_root_earth)
        self.earth.setPos(10, 0, 0)
        self.earth.setScale(3.5 * self.sizescale)
        self.earth_tex = loader.loadTexture("textures/sky_stars_2.jpg")
        self.earth.setTexture(self.earth_tex, 1)

    def rotatePlanets(self):

        # Rotate Sun
        self.day_period_sun = self.sun.hprInterval(20, (360, 0 ,0))
        self.day_period_sun.loop()

        # Rotate Earth
        self.orbit_period_earth = self.orbit_root_earth.hprInterval(
            self.yearscale, (360, 0, 0))
        self.day_period_earth = self.earth.hprInterval(
            self.dayscale, (360, 0, 0))

        self.orbit_period_earth.loop()
        self.day_period_earth.loop()


w = World()
base.run()