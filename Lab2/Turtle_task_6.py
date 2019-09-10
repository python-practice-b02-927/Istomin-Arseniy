import turtle
t=turtle.Turtle()
t.shape('turtle')
t.width(3)
t.color('blue')
n=int(input())
for i in range(n):
    t.forward(100)
    t.stamp()
    t.backward(100)
    t.left(360/n)
    
