import graphics as gr
import random
window = gr.GraphWin("Model", 600, 600)
# global variables
potential_well_depth = 0
zero_dist = 0
particles_amount = 0
dt = 0.0001
mass = 1

def main():
    request_for_constant_parameters()
    particles = []
    velocities = []
    for i in range(particles_amount):
        particle = particle_init()
        particles.append(particle)
        velocities.append(gr.Point(0, 0))
    start_modelling(particles, velocities)
    window.getMouse()
    window.close()


def start_modelling(particles, velocities):
    draw_particles(particles)
    move_particles(particles, velocities)


def draw_particles(particles):
    for i in range(particles_amount):
        particles[i].draw(window)


def move_particles(particles, velocities):
    for t in range(10000):
        for i in range(particles_amount):
            for j in range(particles_amount):
                if i != j:
                    velocities[i] = update_particles_velocity(particles[i], particles[j], velocities[i])
        for i in range(particles_amount):
            particles[i].move(velocities[i].x, velocities[i].y)
            gr.time.sleep(dt)


def update_particles_velocity(particle1, particle2, velocity):
    center = particle1.getCenter()
    flag = False
    if center.x <= 5:
        velocity.x = -velocity.x
        particle1.move(7 - center.x, 0)
        flag = True
    if center.x >= 595:
        velocity.x = -velocity.x
        particle1.move(593 - center.x, 0)
        flag = True
    if center.y <= 5:
        velocity.y = -velocity.y
        particle1.move(0, 7 - center.y)
        flag = True
    if center.y >= 595:
        velocity.y = -velocity.y
        particle1.move(0, 593 - center.y)
        flag = True
    if not flag:
        velocity.x = velocity.x + force(particle1, particle2).x / mass * dt
        velocity.y = velocity.y + force(particle1, particle2).y / mass * dt
    return velocity


def force(particle1, particle2):
    center1 = particle1.getCenter()
    center2 = particle2.getCenter()
    r = ((center1.x - center2.x) ** 2 + (center1.y - center2.y) ** 2)**0.5
    r = max(5, r)
    x_dist = center1.x - center2.x
    if x_dist >= 0:
        x_dist = max(x_dist, 5)
    else:
        x_dist = min(x_dist, -5)
    y_dist = center1.y - center2.y
    if y_dist >= 0:
        y_dist = max(y_dist, 5)
    else:
        y_dist = min(y_dist, -5)
    max_force = 4 * potential_well_depth * (-7 * zero_dist ** 6 / (zero_dist / 1.2) ** 7 + 12 * zero_dist ** 12 / (zero_dist / 1.2) ** 13)
    force = min(max_force, 4 * potential_well_depth * (-7 * zero_dist ** 6 / r ** 7 + 12 * zero_dist ** 12 / r ** 13))
    print(max_force)
    return gr.Point(force * x_dist / r, force * y_dist / r)


def particle_init():
    random.seed()
    x = random.randint(10, 590)
    y = random.randint(10, 590)
    coords = gr.Point(x, y)
    particle = gr.Circle(coords, 5)
    particle.setFill('blue')
    return particle


def request_for_constant_parameters():
    global particles_amount, potential_well_depth, zero_dist, mass
    print("Enter potential well depth")
    potential_well_depth = float(input())
    print("Enter zero energy dist")
    zero_dist = float(input())
    print("Enter mass")
    mass = float(input())
    print("Enter particles amount")
    particles_amount = int(input())


main()
