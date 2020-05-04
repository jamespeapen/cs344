/* Exercise 12.3
 * Burn the witch
 */

witch(X):- burn(X).
burn(A):- madeOfWood(A).
madeOfWood(A):- floatsInWater(A).
floatsInWater(B):- weighsLikeDuck(B).
weighsLikeDuck(woman).

witch(woman). %true
