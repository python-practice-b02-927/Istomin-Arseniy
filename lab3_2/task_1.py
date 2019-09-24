import graphics as gr

window = gr.GraphWin("Model", 600, 600)
g = 10

def main(window):
    coords0 = gr.Point(50, 100)
    velocity0 = gr.Point(10, 5)
    move_circle(coords0, velocity0, window)
    window.getMouse()
    window.close()


def move_circle(coords0, velocity0, window):
    circle = init_circle(coords0, 10, 'blue')
    velocity = velocity0
    circle.draw(window)
    for i in range(1000):
        circle.move(velocity.x, velocity.y)
        gr.time.sleep(0.01)
        velocity = change_velocity(circle, velocity)


def change_velocity(circle, velocity):
    centre = circle.getCenter()
    if centre.x > 600 or centre.x < 0:
        velocity.x = -velocity.x
    if centre.y < 0 or centre.y > 600:
        velocity.y = - velocity.y
    return velocity


def init_circle(coords0, size, color):
    """size is a radius"""
    circle = gr.Circle(coords0, size)
    circle.setFill(color)
    return circle


main(window)
