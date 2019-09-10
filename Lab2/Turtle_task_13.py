import turtle
import math
t=turtle.Turtle()
t.shape('turtle')
t.width(2)
t.color('yellow')

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
#face
t.begin_fill()
cir(100, 1)
t.end_fill()
t.penup()
#left_eye
t.goto(t.xcor()-30, t.ycor()+120)
t.color('blue')
t.pendown()
t.begin_fill()
cir(10, 1)
t.end_fill()
t.penup()
#right_eye
t.goto(t.xcor()+60, t.ycor())
t.pendown()
t.begin_fill()
cir(10, 1)
t.end_fill()
t.penup()
#nose
t.color('black')
t.goto(t.xcor()-30, t.ycor())
t.right(90)
t.forward(15)
t.width(5)
t.pendown()
t.forward(30)
t.penup()
#mouse
t.goto(t.xcor()-30, t.ycor()-10)
t.pendown()
t.color('red')
cir(30, 0.5)
t.penup()


    
