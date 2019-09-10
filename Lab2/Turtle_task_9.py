import turtle
import math
t=turtle.Turtle()
t.shape('turtle')
t.width(3)
t.color('blue')
def polygon(n, size):
    angle=180-360/n
    t.left(180-angle/2)
    for i in range(n):
        t.forward(size)
        t.left(360/n)
    t.right(180-angle/2)
for i in range(3, 13):
    polygon(i,10*i)
    angle1=360/i
    angle2=360/(i+1)
    r1=10*i/2/math.sin(angle1/2/180*3.142)
    r2=10*(i+1)/2/math.sin(angle2/2/180*3.142)
    t.penup()
    t.forward(r2-r1)
    t.pendown()
    
    
