import turtle
import math
t=turtle.Turtle()
t.shape('turtle')
t.width(4)
t.color('blue')
def star(n, size):
    angle=180-360/n/2
    for i in range(n):
        t.forward(size)
        t.right(angle)
n=int(input())
size=int(input())
star(n, size)
