/* Exercise 12.3
 * 2.1
 * 1. unify
 * 2. won't unify
 * 8. unify when bread(X)
 * 9. unify when X is sausage and Y is bread
 * 14. unify when X is drink(beer) and X is food bread
 * 
 * 2.2 
 * Prolog does unification by checking if the terms are the same or if their variables can be instantiated and hold true.
 */

house_elf(dobby).
witch(hermione).
witch('McGonagall').
witch(rita_skeeter).
magic(X):-  house_elf(X).
magic(X):-  witch(X).

magic(house_elf) % not satisfied by rules since house_elf is not defined as being magic
wizard(harry) %  not satisfied, harry is not defined in the rules
magic(wizard) % there is no procedure for wizard
magic(’McGonagall’) % true since it is defined that McGonagall is a witch and a witch is magic
magic(Hermione) % Hermione = dobby; Hermione = hermione; Hermione = 'McGonagall', Hermione = rita_skeeter
  
 /* Search tree for magic(Hermione)
 *                                          magic(Hermione)
 *                                                 |
 *                                          Hermione = _G1
 *                                                 |                                                     
 *          house_elf(_G1)                     wizard(_G1)                              witch(_G1)
 *              |                                  |                                /      |            \
 *           _G1 = dobby                        error                _G1 = hermione   _G1='MCGonagall'   _G1 = rita_skeeter
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 */ 
 
