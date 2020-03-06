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
from probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask

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

