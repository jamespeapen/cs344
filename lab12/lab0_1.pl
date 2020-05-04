/* Exercise 12.1
 * 1.4
 * every verb or adjective is used as the function and the people who act on
 them, or who are acted on or are described are the variables in the rules
 if there is a condition around a rule, the result of the condition is set up 
 as an implication of the rule
 */

killer(butch).
married(mia, marsellus).
dead(zed). 
kills(marsellus, A):- givesFootMassage(A, mia). 
loves(mia, B):- goodDancer(B). 
eats(julie, F): - nutritious(F); tasty(F). 

/* 1.5

1. true: there is a rule set up
2. false: there is no rule for witch
3. false: herminone is not in the rules as satisfying the conditions of being a wizard
4. false: herminone is not in the rules as satisfying the conditions of being a wizard
5. true: harry is a quidditch player and therefore has a broom, since he has a broom and a wand, he is a wizard
6. harry: harry satisfies the conditions of being a wizard
7. no proc for witch: there is no procedure for a witch

*/


