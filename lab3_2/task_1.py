import graphics as gr

window = gr.GraphWin("Model", 600, 600)
g = 5000
time = 0.01
def main():
    coords0 = gr.Point(50, 100)
    velocity0 = gr.Point(5, 6)
    move_circle(coords0, velocity0)
    window.getMouse()
    window.close()


def move_circle(coords0, velocity0):
    circle = init_circle(coords0, 10, 'blue')
    velocity = velocity0
    circle.draw(window)
    for i in range(2000):
        circle.move(velocity.x, velocity.y)
        gr.time.sleep(time)
        velocity = change_velocity(circle, velocity)


def change_velocity(circle, velocity):
    centre = circle.getCenter()
    radius = circle.getRadius()
    if centre.x > 600-radius or centre.x < 0+radius:
        velocity.x = -velocity.x
    if centre.y < 0+radius or centre.y > 600-radius:
        velocity.y = - velocity.y
    velocity.y = velocity.y + g * time**2/2
    #if abs(velocity.y)<
    #print(velocity.y)
    return velocity


def init_circle(coords0, size, color):
    """size is a radius"""
    circle = gr.Circle(coords0, size)
    circle.setFill(color)
    return circle


main()
