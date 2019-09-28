import graphics as gr
import random
window = gr.GraphWin("Model", 600, 600)
# global variables
potential_well_depth = 0
zero_dist = 0
particles_amount = 0


def main():
    request_for_constant_parameters()
    particles = []
    speeds = []
    for i in range(particles_amount):
        particle = particle_init()
        particles.append(particle)
        speeds.append(gr.Point(0, 0))
    start_modelling(particles, speeds)
    window.getMouse()
    window.close()


def start_modelling(particles, speeds):
    draw_particles(particles)
    move_particles(particles, speeds)


def draw_particles(particles):
    for i in range(particles_amount):
        particles[i].draw(window)


def move_particles(particles, speeds):
    for i in range(particles_amount):
        for j in range(particles_amount):
            if i != j:
                update_particles_speed(particles[i], particles[j], speeds[i])


def update_particles_speed(particle1, particle2, speed):
    pass


def particle_init():
    random.seed()
    x = random.randint(10, 590)
    y = random.randint(10, 590)
    coords = gr.Point(x, y)
    particle = gr.Circle(coords, 5)
    particle.setFill('blue')
    return particle


def request_for_constant_parameters():
    global particles_amount, potential_well_depth, zero_dist
    print("Enter potential well depth")
    potential_well_depth = int(input())
    print("Enter zero dist")
    zero_dist = int(input())
    print("Enter particles amount")
    particles_amount = int(input())


main()
