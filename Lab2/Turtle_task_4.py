import turtle
t=turtle.Turtle()
t.shape('turtle')
t.width(5)
t.color('blue')
r=50
t.left(90)
for i in range(r):
    t.forward(2*3.142)
    t.left(360/r)
