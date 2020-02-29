''''
This module implements a simple classroom example of probabilistic inference
over the full joint distribution specified by AIMA, Figure 13.3.
It is based on the code from AIMA probability.py.

@author: kvlinden
@version Jan 1, 2013
'''

'''
Lab 4
@author: James Eapen
@date: 2020 Feb 28

Ex 4.2
a. 
i. It contains 16 entries.
ii. They should sum up to 1 because they are the probabilities of all possibilites in the question.
iii. No because there is no other value it can take. It can rain or not rain. This is also true for the other variables since there are no gradations of the existence of a toothache or a cavity.
iv. I chose a 50:50 chance for rain and applied it to all the cases. The chance of rain does not depend on the other probabilities and so is independent. 

b.
P(Toothache|Rain) = P(Rain|Toothache).P(Toothache)/P(Rain)
     = (0.1/0.2 * 0.2) / 0.5
     = 0.1/0.5 = 0.2

AIMA solution for P(Toothache|Rain): 0.2
'''


import sys
sys.path.append("/home/james/Documents/Calvin/CS-344/cs344-code/tools/aima")
from probability import JointProbDist, enumerate_joint_ask

# The Joint Probability Distribution Fig. 13.3 (from AIMA Python)
P = JointProbDist(['Toothache', 'Cavity', 'Catch', 'Rain'])
T, F = True, False
P[T, T, T, T] = 0.054; P[T, T, F, T] = 0.006
P[F, T, T, T] = 0.036; P[F, T, F, T] = 0.004
P[T, F, T, T] = 0.008; P[T, F, F, T] = 0.032
P[F, F, T, T] = 0.072; P[F, F, F, T] = 0.288

P[T, T, T, F] = 0.054; P[T, T, F, F] = 0.006 
P[F, T, T, F] = 0.036; P[F, T, F, F] = 0.004 
P[T, F, T, F] = 0.008; P[T, F, F, F] = 0.032 
P[F, F, T, F] = 0.072; P[F, F, F, F] = 0.288 

# Compute P(Cavity|Toothache=T)  (see the text, page 493).
PC = enumerate_joint_ask('Toothache', {'Rain': T}, P)
print("P(Toothache|Rain):")
print(PC.show_approx())


