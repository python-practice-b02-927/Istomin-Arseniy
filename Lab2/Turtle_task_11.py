import turtle
import math
t=turtle.Turtle()
t.shape('turtle')
t.width(3)
t.color('blue')
t.left(90)
def cir(r, k):
    if r>0:
        for i in range(int(r*k)):
            t.forward(2*3.142)
            t.left(360/r)
    else:
        r*=-1
        for i in range(int(r*k)):
            t.forward(2*3.142)
            t.right(360/r)
for i in range(1, 11):
    cir(50+10*i, 1)
    cir(-50-10*i, 1)
    
