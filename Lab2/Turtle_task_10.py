import turtle
import math
t=turtle.Turtle()
t.shape('turtle')
t.width(3)
t.color('blue')
def cir(r, k):
    if r>0:
        for i in range(int(r*k)):
            t.forward(2*3.142)
            t.left(360/r)
    else:
        for i in range(int(r*k)):
            t.forward(2*3.142)
            t.right(360/r)
for i in range(10):
    cir(50, 1)
    t.left(360/10)
