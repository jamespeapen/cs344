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
happy = BayesNet([
    ('Sunny', '', 0.7),
    ('Raise', '', 0.01),
    ('Happy', 'Sunny Raise', {(T, T): 1.0, (T, F): 0.7, (F, T): 0.9, (F, F): 0.1})
    ])

'''
Exercise 5.3 a i.
P(Raise | sunny)
Raise is not dependent on sunny so the probability is only that of raise
= a.⟨P(Raise), P(¬Raise)⟩
= a.⟨0.01, 0.99⟩
= ⟨0.01, 0.99⟩
'''
print('P(Raise | Sunny)')
print(enumeration_ask('Raise', dict(Sunny=T), happy).show_approx())
# elimination_ask() is a dynamic programming version of enumeration_ask().
#print(elimination_ask('Cancer', dict(Test1=T, Test2=T), happy).show_approx())
## gibbs_ask() is an approximation algorithm helps Bayesian Networks scale up.
#print(gibbs_ask('Cancer', dict(Test1=T, Test2=T), happy).show_approx())

'''
Exercise 5.3 a ii.
P(Raise | happy ∧ sunny)
= a.⟨P(Raise).P(Happy|Raise∧Sunny), P(¬Raise).P(Happy|¬Raise∧Sunny)⟩
= a.⟨0.01*1, 0.99*0.7⟩
= a.⟨0.01, 0.693⟩
= 1.422⟨0.01, 0.693⟩
= ⟨0.0142, 0.986⟩
The probability is lower than I expected, but it makes sense since the probability of a raise is quite small.
'''
print('P(Raise|Happy and Sunny)')
print(enumeration_ask('Raise', dict(Happy=T, Sunny=T), happy).show_approx())

'''
Exercise 5.3 b i.
The chances that a raise caused happiness is much smaller than the chance that it being sunny caused it so this answer makes sense.
'''
print('P(Raise|Happy)')
print(enumeration_ask('Raise', dict(Happy=T), happy).show_approx())
'''
Exercise 5.3 b ii.
The probability of being happy without sun or a raise is still higher than the probability of getting a raise so it makes sense that the probability is low for a raise even without sunny.
'''
print('P(Raise|Happy and not Sunny)')
print(enumeration_ask('Raise', dict(Happy=T, Sunny=F), happy).show_approx())
