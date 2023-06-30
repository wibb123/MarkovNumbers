from snake import snake
from Markov import Markov
from Pythagoras import pythag
import math
def sqrt(x):
    return math.sqrt(x)

base = Markov(1, 2, 5)

markov_triples = [
    base
]
markov_numbers = [1, 2, 5]

for trip in markov_triples:
    if len(markov_triples) < 1000000:

        sol = trip.next_two_trips()
        for i in sol:
            markov_triples.append(i)
            m = i.maximum()
            markov_numbers.append(m)

length = len(set(markov_numbers))
length2 = len(markov_numbers)
print(length)
print(length2)
