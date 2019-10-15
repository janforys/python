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



