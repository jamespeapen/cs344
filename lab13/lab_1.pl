% Exercise 13.1
% a.

% 3.2
in(X, Y):- directlyIn(X, Y).
in(X, Z):- directlyIn(Y, Z), in(X, Y).
directlyIn(katarina, olga).
directlyIn(olga, natasha).
directlyIn(natasha, irina).

/* This function recursively checks if Y is known to be in X.
 * for in(katarina, irina) the steps are: 
 * in(katarina, irina): 
 * directlyIn(natasha, irina), in(katarina, natasha)
 *
 *  in(katarina, natasha):
 *  directlyIn(olga, natasha), in(katarina, olga)
 *
 *      in(katarina, olga):
 *      directlyIn(katarina, olga)
 */

%4.5
tran(eins,one).
tran(zwei,two).
tran(drei,three).
tran(vier,four).
tran(fuenf,five).
tran(sechs,six).
tran(sieben,seven).
tran(acht,eight).
tran(neun,nine).

listtran([],  []).
listtran(G|TG], [E|TE]):- tran(G, E), listtran(TG, TE).
listtran([eins, zwei, drei], X).
%X = [one, two, three]

/* This works by taking the head of the given list and getting its translations.
 * Then it gets the translation of the head of the tail of the list recursively making
 * its way through the list. 
 * 1. tran(eins, E), listtran([zwei, drei], TE)
 * 2. tran(zwei, E), listtran([drei], [one])
 * 3. tran(drei, E), listtran([], [one, two])
 * 4. tran(), listtran([], [one, two, three])
 */

/* b.  
 * Prolog implements a form of modus ponens because it checks conditions to make decision. 
 * With the Russian dolls, it decides that Z is in X based on whether Z is in X or Z is in Y and Y is in X. 
 * If Z in is Y and Y is in X, then Z is in X. This form fits modus ponens.
 */
