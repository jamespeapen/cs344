"""
Homework 2 code
@author: James Eapen (jpe4)
@date: 2020 March 12
"""

import sys
sys.path.append('/home/james/Documents/Calvin/CS-344/cs344-code/tools/aima')
from probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask, rejection_sampling, likelihood_weighting

# Utility variables
T, F = True, False

wet_lawns = BayesNet([
    ('Cloudy', '', 0.5),
    ('Sprinkler', 'Cloudy', {T: 0.1, F: 0.5}),
    ('Rain', 'Cloudy', {T: 0.8, F: 0.2}),
    ('WetGrass', 'Sprinkler Rain', {(T, T): 0.99, (T, F): 0.90, (F, T): 0.9, (F, F): 0.0})
    ])

# d. 
print('P(Cloudy)')
print(enumeration_ask('Cloudy', dict(),  wet_lawns).show_approx())

print('P(Sprinker | cloudy')
print(enumeration_ask('Sprinker', dict(Cloudy=T), wet_lawns).show_approx())

print('P(Cloudy| the sprinkler is running and it’s not raining)')
print(enumeration_ask('Cloudy', dict(Sprinker=T, Rain=F), wet_lawns).show_approx())

print('P(WetGrass | it’s cloudy, the sprinkler is running and it’s raining)')
print(enumeration_ask('WetGrass', dict(Cloudy=T, Sprinker=T, Rain=T), wet_lawns).show_approx())

print('P(Cloudy | the grass is not wet)')
print(enumeration_ask('Cloudy', dict(WetGrass=F), wet_lawns).show_approx())
