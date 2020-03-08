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
cancer = BayesNet([
    ('Cancer', '', 0.01),
    #('Cancer', 'Test1 Test2', {(T, T): 0.81, (T, F): 0.18, (F, T): 0.18, (F, F): 0.04})
    ('Test1', 'Cancer', {T: 0.90, F: 0.20}),
    ('Test2', 'Cancer', {T: 0.90, F: 0.20})
    ])

'''
Exercise 5.2 a.
P(Cancer | positive results on both tests)
= a.⟨P(Cancer).P(Test1|Cancer).P(¬Test2|Cancer), P(¬Cancer).P(Test1|¬Cancer).P(Test2|¬Cancer)⟩
= a.⟨0.0081, 0.0396⟩
= 20.96⟨0.0081, 0.0396⟩
= ⟨0.17, 0.83⟩

It makes sense that there is only 0.17 chance of cancer because the probability of cancer by itself is only 0.01.
'''

print('P(Cancer | positive results on both tests)')
print(enumeration_ask('Cancer', dict(Test1=T, Test2=T), cancer).show_approx())
# elimination_ask() is a dynamic programming version of enumeration_ask().
print(elimination_ask('Cancer', dict(Test1=T, Test2=T), cancer).show_approx())
# gibbs_ask() is an approximation algorithm helps Bayesian Networks scale up.
print(gibbs_ask('Cancer', dict(Test1=T, Test2=T), cancer).show_approx())

'''
Exercise 5.2 a.
P(Cancer | a positive result on test 1, but a negative result on test 2)
= a.⟨P(Cancer).P(Test1|Cancer).P(¬Test2|Cancer), P(¬Cancer).P(Test1|¬Cancer).P(¬Test2|¬Cancer)⟩
= a.⟨0.01*0.9*0.1, 0.99*0.2*0.8⟩
= a.⟨0.0009, 0.1782⟩
= 5.583⟨0.005, 0.994⟩
Failing one test makes the chance of cancer much smaller. This is also because a the probability of not cancer is much higher than the probability of cancer and the failed test adds to the reduction in cancer probability.
'''
print('P(Cancer | a positive result on test 1, but a negative result on test 2)')
print(enumeration_ask('Cancer', dict(Test1=T, Test2=F), cancer).show_approx())


