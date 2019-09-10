import turtle
t=turtle.Turtle()
t.shape('turtle')
t.width(3)
t.color('blue')
def sqare(n):
    t.forward(n)
    t.left(90)
    t.forward(n)
    t.left(90)
    t.forward(n)
    t.left(90)
    t.forward(n)
    t.left(90)
for i in range(1, 11):
    sqare(10*i)
    t.penup()
    t.right(90)
    t.forward(5)
    t.right(90)
    t.forward(5)
    t.left(90)
    t.left(90)
    t.pendown()
    
    
    
