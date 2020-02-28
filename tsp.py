
import sys
import random
sys.path.append("/home/james/Documents/Calvin/CS-344/cs344-code/tools/aima")

from search import Problem, hill_climbing, simulated_annealing, \
    exp_schedule, genetic_search
import logging
import time

class TSP(Problem):
    def __init__(self, initial, distances):
        self.initial = initial
        self.distances = distances

    def actions(self, state):
        """select two cities at random to swap and pass a list of their indices to actions"""

        swap_list = random.sample(self.initial, 2)
        index1, index2 = self.initial.index(swap_list[0]), self.initial.index(swap_list[1])
        actions = [[index1, index2]]
        return actions

    def result(self, state, action):
        """make a copy of the previous state and swap the two cities;
         add the first city of the new state to the end for a round trip"""

        new_state = self.initial[:]
        new_state[action[0]], new_state[action[1]] = new_state[action[1]], new_state[action[0]]
        new_state.append(new_state[0])
        return new_state

    def value(self, state):
        """find the total round trip distance of travel between the cities in the state"""
        
        total_dist = 0
        for i in range(len(state)-1):
            city1 = state[i]
            city2 = state[i+1]

            if city1 > city2:
                total_dist += self.distances[(city2, city1)]
            else:
                total_dist += self.distances[(city1, city2)]

        return total_dist
                       


cities = ["A", "B", "C", "D"]
distances = {("A", "B"): 1, ("A", "C"): 2, ("A", "D"): 4,
                ("B", "C"): 3.5, ("B", "D"): 5, 
                ("C", "D"): 3}
        
tsp = TSP(cities, distances)

hill_climbing_test = hill_climbing(tsp)

print("Hill Climbing")
print("Solution: " + str(hill_climbing_test))
print("Value: " + str(tsp.value(hill_climbing_test)))
print("\n")

simulated_annealing_test = simulated_annealing(tsp)
print("Simulated Annealing")
print("Solution: " + str(simulated_annealing_test))
print("Value: " + str(tsp.value(simulated_annealing_test)))
        