import turtle
t=turtle.Turtle()
t.shape('turtle')
t.width(3)
t.color('blue')
for i in range(20):
    t.left(90)
    t.forward(10*i)
    t.left(90)
    t.forward(10*i)
