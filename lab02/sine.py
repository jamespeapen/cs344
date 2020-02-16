"""
This module implements local search on a simple abs function variant.
The function is a linear function  with a single, discontinuous max value
(see the abs function variant in graphs.py).

@author: kvlinden
@version 6feb2013
"""
from search import Problem, hill_climbing, simulated_annealing, \
    exp_schedule, genetic_search
from random import randrange
import math


class SineVariant(Problem):
    """
    State: x value for the abs function variant f(x)
    Move: a new x value delta steps from the current x (in both directions) 
    """

    def __init__(self, initial, maximum=30.0, delta=0.001):
        self.initial = initial
        self.maximum = maximum
        self.delta = delta

    def actions(self, state):
        return [state + self.delta, state - self.delta]

    def result(self, stateIgnored, x):
        return x

    def value(self, x):
        return math.fabs(x * math.sin(x))


if __name__ == '__main__':

    # Formulate a problem with a 2D hill function and a single maximum value.
    maximum = 30
    initial = randrange(0, maximum)
    p = SineVariant(initial, maximum, delta=1.1)
    print('Initial                      x: ' + str(p.initial)
          + '\t\tvalue: ' + str(p.value(initial))
          )

    # Solve the problem using hill-climbing.
    hill_solution = hill_climbing(p)
    annealing_solution = simulated_annealing(p,
                                             exp_schedule(k=20, lam=0.005, limit=1000))

    hill_restarts = hill_solution
    hill_value_accumulator = 0
    hill_x_accumulator = 0

    annealing_restarts = annealing_solution
    annealing_value_accumulator = 0
    annealing_x_accumulator = 0

    restarts = 100
    for i in range(restarts):
        initial = randrange(0, maximum)
        p = SineVariant(initial, maximum, delta=1.1)

        hill_solution = hill_climbing(p)
        hill_x_accumulator += int(hill_solution)
        hill_value_accumulator += int(p.value(hill_solution))

        annealing_solution = simulated_annealing(p)
        annealing_value_accumulator += int(p.value(annealing_solution))
        annealing_x_accumulator += int(annealing_solution)

        if int(p.value(hill_solution)) > int(p.value(hill_restarts)):
            hill_restarts = hill_solution
        if int(p.value(annealing_solution)) > int(p.value(annealing_restarts)):
            annealing_restarts = annealing_solution

    print('Hill-climbing solution       x: ' + str(hill_solution)
          + '\tvalue: ' + str(p.value(hill_solution))
          + '\nRandom restarts              x: ' + str(hill_restarts)
          + '\tvalue: ' + str(p.value(hill_restarts))
          + '\naverage                      x: ' +
          str(hill_x_accumulator/restarts)
          + '\tvalue: ' + str(hill_value_accumulator/restarts)
          + '\n'
          )

    # Solve the problem using simulated annealing.
    print('Simulated annealing solution x: ' + str(annealing_solution)
          + '\tvalue: ' + str(p.value(annealing_solution))
          + '\nRandom restarts              x: ' + str(annealing_restarts)
          + '\tvalue: ' + str(p.value(annealing_restarts))
          + '\naverage                      x: ' +
          str(annealing_x_accumulator/restarts)
          + '\tvalue: ' + str(p.value(annealing_value_accumulator/restarts))
          )
