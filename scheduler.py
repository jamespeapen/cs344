"""CS Class Scheduling
@author: James Eapen (jpe4)
@date: 2020 Feb 27
"""

import sys
sys.path.append("/home/james/Documents/Calvin/CS-344/cs344-code/tools/aima")

from csp import CSP, min_conflicts, backtracking_search, AC3, parse_neighbors
import random

def Scheduler():
    courses = ['cs108', 'cs112', 'cs212', 'cs232', 'cs344', 'cs342']
    professors = ['hplantin', 'adams', 'vnorman', 'kvlinden', 'pbailey']
    times = ['mwf900', 'tth1030', 'mwf1130', 'mwf1230', 't1800', 'mwf1430']
    classrooms = ['sb382', 'nh253']
    assignments = {'cs108': 'kvlinden',
                    'cs112': 'adams',
                    'cs212': 'hplantin',
                    'cs232': 'vnorman',
                    'cs342': 'pbailey',
                    'cs344': 'kvlinden'}

    variables = courses 
    domains = {}
    # make all possible combinations
    for course in variables:
        domains[course]= []
        for time in times:
            for classroom in classrooms:
                for professor in professors:
                    domains[course].append((professor, time, classroom))

    # set all classes neighbors of each other because each affects every other
    neighbors = parse_neighbors('''cs108: cs112 cs212 cs344 cs232 cs342; 
                            cs112: cs212 cs232 cs344 cs342; 
                            cs212: cs232 cs344 cs342; 
                            cs232: cs344 cs342; 
                            cs344: cs342''', variables)
    
    # set constraints
    def scheduling_constraints(A, a, B, b, recurse = 0):
        # if same prof
        if a[0] == b[0]:

            # and same time
            if a[1] == b[1]:
                return False
            # or same room 
            if a[2] == b[2]:
                return False
        
        # if same time
        if a[1] == b[1]:

            # and same prof
            if a[0] == b[0]:
                return False
            # or same room
            if a[2] == b[0]:
                return False

        # if same room
        if a[2] == b[2]:

            # and same prof
            if a[0] == b[0]:
                return False

            # or same time
            if a[1] == b[1]:
                return False 

        # check if class has assigned prof
        if (assignments[A] != a[0]) or (assignments[B] != b[0]):
            return False

        return True
    return CSP(variables, domains, neighbors, scheduling_constraints)

p = Scheduler()
result = backtracking_search(p)

for each_class in result:
    print("Class: ", each_class)
    print("Professor: ", result[each_class][0])
    print("Room: ", result[each_class][2])
    print("Time: ", result[each_class][1])
    print()