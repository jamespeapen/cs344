'''
Ex 4.1b.
Hand calculation: 
P(Cavity|Catch) = (P(Catch|Cavity).P(Cavity))/P(Catch)

P(Cavity) = 0.20
P(Catch) = 0.34
P(Catch|Cavity) = (0.108 + 0.072)/0.2 = 0.9

P(Cavity|Catch) = 0.9(0.20)/0.34 = 0.529

AIMA result:
    True = 0.529

c. 
P(Coin2|Coin1 = heads) = 0.5
'''

'''
Ex 4.3a.

 User  | Non-user
 -----------------
 0.99  | 0.02
 -----------------
 0.01  | 0.98

i. P(User)

'''

'''
This module implements a simple classroom example of probabilistic inference
over the full joint distribution specified by AIMA, Figure 13.3.
It is based on the code from AIMA probability.py.

@author: kvlinden
@version Jan 1, 2013
'''
import sys
sys.path.append("/home/james/Documents/Calvin/CS-344/cs344-code/tools/aima")
from probability import JointProbDist, enumerate_joint_ask

# The Joint Probability Distribution Fig. 13.3 (from AIMA Python)
P = JointProbDist(['Toothache', 'Cavity', 'Catch'])
T, F = True, False
P[T, T, T] = 0.108; P[T, T, F] = 0.012
P[F, T, T] = 0.072; P[F, T, F] = 0.008
P[T, F, T] = 0.016; P[T, F, F] = 0.064
P[F, F, T] = 0.144; P[F, F, F] = 0.576

# Compute P(Cavity|Toothache=T)  (see the text, page 493).
PC = enumerate_joint_ask('Cavity', {'Toothache': T}, P)
print("P(Cavity|Toothache):")
print(PC.show_approx())

# Compute P(Cavity|Catch=T)
print("P(Cavity|Catch):")
print(PC.show_approx())
PC = enumerate_joint_ask('Cavity', {'Catch': T}, P)
print(PC.show_approx())

C = JointProbDist(['Coin1', 'Coin2'])
H, T = 'Heads', 'Tails'
C['Heads', 'Heads'] = 0.25; C['Tails', 'Tails'] = 0.25
C['Heads', 'Tails'] = 0.25; C['Tails', 'Heads'] = 0.25

print('P(Coin2|Coin1=heads)')
PC = enumerate_joint_ask('Coin2', {'Coin1': 'Heads'}, C)
print(PC.show_approx())
