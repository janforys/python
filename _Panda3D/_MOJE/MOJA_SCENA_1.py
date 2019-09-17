# importujemy moduly (pakiety)
from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor
from panda3d.core import Point3
from direct.interval.IntervalGlobal import Sequence

class MyApp(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)

        # tworzymy bazowa scene
        self.scena1 = self.loader.loadModel("models/environment")
        self.scena1.reparentTo(self.render)
        self.scena1.setScale(0.10, 0.10, 0.10)
        self.scena1.setPos(-8, 42, 0)

        # wstawiamy aktora
        self.aktorPanda = Actor("models/panda-model",{"walk": "models/panda-walk4"})
        self.aktorPanda.setScale(0.005, 0.005, 0.005)
        self.aktorPanda.reparentTo(self.render)
		
		# animacja chodu
        self.aktorPanda.loop("walk")
        przemieszczenie1 = self.aktorPanda.posInterval(5, Point3(0, -3, 0), startPos=Point3(0, 3, 0))
        obrot1 = self.aktorPanda.hprInterval(3, Point3(-180, 0, 0), startHpr=Point3(0, 0, 0))
        przemieszczenie2 = self.aktorPanda.posInterval(5, Point3(0, 3, 0), startPos=Point3(0, -3, 0))
        obrot2 = self.aktorPanda.hprInterval(3, Point3(0, 0, 0), startHpr=Point3(-180, 0, 0))
        self.Idzie = Sequence(przemieszczenie1, obrot1, przemieszczenie2, obrot2)
        self.Idzie.loop()
        self.aktorPanda.setPos(0, 0, 0)

        # wstawiamy drugiego aktora
        self.aktorPanda2 = Actor("models/panda-model", {"walk": "models/panda-walk4"})
        self.aktorPanda2.setScale(0.01, 0.01, 0.01)
        self.aktorPanda2.reparentTo(self.render)
        self.aktorPanda2.loop("walk")
        self.aktorPanda2.setPos(-6, 2, 0)

app = MyApp()
app.run()