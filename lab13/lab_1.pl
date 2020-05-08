% Exercise 13.1

% 3.2
in(X, Y):- directlyIn(X, Y).
in(X, Z):- directlyIn(Y, Z), in(X, Y).
directlyIn(katarina, olga).
directlyIn(olga, natasha).
directlyIn(natasha, irina).

/* This function recursively checks if Y is known to be in X.
 * in(katarina, natasha): directlyIn(olga, natasha), in(katarina, olga)
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
