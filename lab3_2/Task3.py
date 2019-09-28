# global variables
potential_well_depth = 0
zero_dist = 0
particles_amount = 0


def main():
    request_for_constant_parameters()
    particles = []
    for i in range(zero_dist):
        particle = particle_init()
        particles.append(particle)


def particle_init():
    pass

def request_for_constant_parameters():
    global particles_amount, potential_well_depth, zero_dist
    print("Enter potential well depth")
    potential_well_depth = int(input())
    print("Enter zero dist")
    zero_dist = int(input())
    print("Enter particles amount")
    particles_amount = int(input())


main()
