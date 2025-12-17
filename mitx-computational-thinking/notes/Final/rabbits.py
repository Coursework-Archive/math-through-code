import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 50
CURRENTFOXPOP = 300

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP

    if CURRENTRABBITPOP < 10:
        return

    prob_birth = 1.0 - (CURRENTRABBITPOP / float(MAXRABBITPOP))
    births = 0
    for _ in range(CURRENTRABBITPOP):
        if random.random() < prob_birth:
            births += 1
    CURRENTRABBITPOP += births
    if CURRENTRABBITPOP > MAXRABBITPOP:
        CURRENTRABBITPOP = MAXRABBITPOP
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    if CURRENTFOXPOP < 10:
        return
    if CURRENTRABBITPOP < 10:
        return

    prob_eat = CURRENTRABBITPOP / float(MAXRABBITPOP)
    foxes_start = CURRENTFOXPOP
    for _ in range(foxes_start):
        ate = False
        if CURRENTRABBITPOP > 10 and random.random() < prob_eat:
            CURRENTRABBITPOP -= 1
            ate = True
        if ate:
            if random.random() < (1.0 / 3.0):
                CURRENTFOXPOP += 1
        else:
            if random.random() < (1.0 / 10.0):
                CURRENTFOXPOP -= 1


            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """
    rabbit_populations = []
    fox_populations = []
    for _ in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbit_populations.append(CURRENTRABBITPOP)
        fox_populations.append(CURRENTFOXPOP)
    return (rabbit_populations, fox_populations)

def plot_with_quad_fit(pop_over_time, title):
    x = pylab.array(range(len(pop_over_time)))
    y = pylab.array(pop_over_time)

    coeffs = pylab.polyfit(x, y, 2)
    y_est = pylab.polyval(coeffs, x)

    pylab.plot(x, y, 'b.', label='data')
    pylab.plot(x, y_est, 'r-', label='quad fit')
    pylab.title(title)
    pylab.xlabel('Time step')
    pylab.ylabel('Population')
    pylab.legend(loc='best')

    return coeffs

rabbit_pop_over_time, fox_pop_over_time = runSimulation(200)

pylab.figure()

pylab.subplot(2, 1, 1)
r_coeffs = plot_with_quad_fit(rabbit_pop_over_time, 'Rabbits')

pylab.subplot(2, 1, 2)
f_coeffs = plot_with_quad_fit(fox_pop_over_time, 'Foxes')

pylab.tight_layout()
pylab.show()

print("Rabbit coeffs (a,b,c):", r_coeffs)
print("Fox coeffs (a,b,c):", f_coeffs)

for t in range(len(rabbit_pop_over_time)):
    if fox_pop_over_time[t] > rabbit_pop_over_time[t]:
        print("At time step {}: foxes = {}, rabbits = {}"
              .format(t, fox_pop_over_time[t],
                      rabbit_pop_over_time[t]))
