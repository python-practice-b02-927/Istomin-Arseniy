from typing import Any, Union

import graphics as gr
import random
window = gr.GraphWin("Model", 600, 600)
# global variables
potential_well_depth = 0
zero_dist = 0
particles_amount = 0
dt = 0.0002
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
    if center.x < 5 or center.x > 595:
        flag = True
        velocity.x = -velocity.x
    if center.y < 5 or center.y > 595:
        flag = True
        velocity.y = -velocity.y
    if not flag:
        velocity.x = velocity.x + force(particle1, particle2).x / mass * dt
        velocity.y = velocity.y + force(particle1, particle2).y / mass * dt
    return velocity


def force(particle1, particle2):
    center1 = particle1.getCenter()
    center2 = particle2.getCenter()
    r = ((center1.x - center2.x) ** 2 + (center1.y - center2.y) ** 2)**0.5
    x_dist = center2.x - center1.x
    y_dist = center2.y - center1.y
    force = 4 * potential_well_depth * (7 * zero_dist ** 6 / r ** 7 - 12 * zero_dist ** 12 / r ** 13)
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
