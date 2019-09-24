import graphics as gr

window = gr.GraphWin("Model", 600, 600)
g = 10000
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
    collision = False
    if centre.x > window.width-radius or centre.x <radius:
        velocity.x = -velocity.x
        collision = True
    if centre.y < radius or centre.y > window.height-radius:
        velocity.y = - velocity.y
        collision = True
    if not collision:
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
