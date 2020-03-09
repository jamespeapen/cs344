'''
This module implements the Bayesian network shown in the text, Figure 14.2.
It's taken from the AIMA Python code.

@author: kvlinden
@version Jan 2, 2013

@author: James Eapen (jpe4)
@date: 2020 March 6
'''

import sys
sys.path.append('/home/james/Documents/Calvin/CS-344/cs344-code/tools/aima')
from probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask, rejection_sampling, likelihood_weighting


# Exercise 5.1
# Utility variables
T, F = True, False

# From AIMA code (probability.py) - Fig. 14.2 - burglary example
burglary = BayesNet([
    ('Burglary', '', 0.001),
    ('Earthquake', '', 0.002),
    ('Alarm', 'Burglary Earthquake', {(T, T): 0.95, (T, F): 0.94, (F, T): 0.29, (F, F): 0.001}),
    ('JohnCalls', 'Alarm', {T: 0.90, F: 0.05}),
    ('MaryCalls', 'Alarm', {T: 0.70, F: 0.01})
    ])

# Compute P(Burglary | John and Mary both call).
print('P(Burglary | John and Mary both call)')
print(enumeration_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
# elimination_ask() is a dynamic programming version of enumeration_ask().
print(elimination_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
# gibbs_ask() is an approximation algorithm helps Bayesian Networks scale up.
print(gibbs_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
# See the explanation of the algorithms in AIMA Section 14.4.
# Exercise 5.1 ai.
print('P(Alarm | burglary ∧ ¬earthquake)')
print(enumeration_ask('Alarm', dict(Burglary=T, Earthquake=F), burglary).show_approx())

# Exercise 5.1 aii.
print('P(John | burglary ∧ ¬earthquake)')
print(enumeration_ask('John', dict(Burglary=T, Earthquake=F), burglary).show_approx())

# Exercise 5.1 aiii.
print('P(Burglary | alarm)')
print(enumeration_ask('Burglary', dict(Alarm=T), burglary).show_approx())

# Exercise 5.1 aiv.
print('P(Burglary | john ∧ mary)')
print(enumeration_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())

'''Exercise 5.4
elimination_ask has the same probabilities as enumeration_ask because it is a dynamic version of enumeration_ask.
Rejection sampling works by using the network created to generate samples. It then removes the samples that don't match the conditions given like the condition that both john and mary call. The final probability is the number of times a burglary occurs in the remaining samples. In this case, it overestimates the probability that the burglary occurs because it rejects the samples that are important in finding a good approximation.
Liklihood weighting skips the generating and rejection steps by generating only those samples that fit the specified conditions of the case. It gets closer to the exact inference values but is still an overestimate for burglary.
Gibbs sampling gets the same probabilities as the enumeration_ask and elimination_ask. It works well because the way it transitions between the samples is dependent on those samples' probabilities and allows the sampling to find better estimates that are closer to the actual probabilities.
'''

print("\nElimination ask")
print(elimination_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())

print("Rejection sampling")
print(rejection_sampling('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())

print("Liklihood estimate")
print(likelihood_weighting('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())

print("Gibbs Sampling ")
print(gibbs_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())

