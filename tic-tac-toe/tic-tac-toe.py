from turtle import *
import math

side = 80

# draws single square
def square():
    for i in range(4):
        fd(side)
        left(90)

def board():
    for i in range(3):
        for j in range (3):
            pd()
            square()
            pu()
            fd(side)
        bk(3*side)
        left(90)
        fd(side)
        right(90)

def cross(a,b):
    pu()
    setx(a*side + side/2)
    sety(b*side + side/2)
    pd()
    left(45)
    for i in range(4):
        fd(side/4)
        bk(side/4)
        left(90)
    right(45)
    pu()

def circle(a,b):
    pu()
    setx(a*side + side/2)
    sety(b*side + side/2 - 54/math.pi)
    pd()
    for i in range(36):
        fd(3)
        left(10)
    pu()
