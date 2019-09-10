import turtle
t=turtle.Turtle()
t.shape('turtle')
t.width(3)
t.color('blue')
for i in range(1,300):
    angle=5
    t.forward(angle*3.142/180*i)
    t.left(angle)
