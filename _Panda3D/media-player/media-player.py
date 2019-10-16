from panda3d.core import *
# Tell Panda3D to use OpenAL, not FMOD
loadPrcFileData("", "audio-library-name p3openal_audio")

from direct.showbase.DirectObject import DirectObject
from direct.gui.OnscreenText import OnscreenText
from direct.showbase.ShowBase import ShowBase

# function to put instructions on the screen
def addInstructions(pos, msg):
    return OnscreenText(text=msg, style=1, fg=(0, 0, 0, 1), shadow=(1, 1, 1, 1),
                        parent=base.a2dTopLeft, align=TextNode.ALeft,
                        pos=(0.08, -pos - 0.04), scale=.06)

# function to put title on the screen
def addTitle(text):
    return OnscreenText(text=text, style=1, pos=(-0.1, 0.09), scale=.08,
                        parent=base.a2dBottomRight, align=TextNode.ARight,
                        fg=(1, 1, 1, 1), shadow=(0, 0, 0, 1))


class MediaPlayer(ShowBase):

    def __init__(self, media_file):
        ShowBase.__init__(self)

        self.title = addTitle("Panda3D: MEDIA PLAYER")
        self.instruction1 = addInstructions(0.06, "for Play/Pause press P")
        self.instruction2 = addInstructions(0.12, "for Stop/Rewind press S")
        self.instruction3 = addInstructions(0.18, "for Slow Motion/Normal press M")

        # load movie texture and check it
        self.tex = MovieTexture("name")
        success = self.tex.read(media_file)
        assert success, "Failed to load video!"

        # fullscreen card set up to set the video texture
        CM = CardMaker("My Fullscren Card")
        CM.setFrameFullscreenQuad()

        CM.setUvRange(self.tex)

        # place the card in the scene graph and apply texture to it
        card = NodePath(CM.generate())
        card.reparentTo(self.render2d)
        card.setTexture(self.tex)

        self.sound = loader.loadSfx(media_file)
        self.tex.synchronizeTo(self.sound)

        self.accept('p', self.playpause)
        #self.accept('P', self.playpause)
        self.accept('m', self.fastforward)
        #self.accept('M', self.fastforward)
        self.accept('s', self.stopsound)
        #self.accept('S', self.stopsound)

    def stopsound(self):
        self.sound.stop()
        self.sound.setPlayRate(1.0)

    def fastforward(self):
        if self.sound.status() == AudioSound.PLAYING:
            t = self.sound.getTime()
            self.sound.stop()
            if self.sound.getPlayRate() == 1.0:
                self.sound.setPlayRate(0.5)
            else:
                self.sound.setPlayRate(1.0)
            self.sound.setTime(t)
            self.sound.play()

    def playpause(self):
        if self.sound.status() == AudioSound.PLAYING:
            t = self.sound.getTime()
            self.sound.stop()
            self.sound.setTime(t)
        else:
            self.sound.play()

player = MediaPlayer("benek.mp4")
player.run()