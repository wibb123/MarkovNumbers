from snake import snake
from Markov import Markov
from Pythagoras import pythag
import math
def sqrt(x):
    return math.sqrt(x)

f = open("results.txt", "w")

base = Markov(1, 2, 5)

markov_triples = [
    base
]

print("(" + str(base.num1)+"," + str(base.num2) + "," + str(base.num3) + ")")
for trip in markov_triples:
    if len(markov_triples) < 20:
        sol = trip.next_two_trips()
        for i in sol:
            markov_triples.append(i)
            m = i.maximum()
            for b in range(m):
                if ((sqrt(2) - 1) * m) > b > (((3 - sqrt(5)) / 2) * m):
                    if pow(b, 2, m) == m - 1:
                        matchings = snake(m, b)
                        result = pythag(matchings)
                        f.write("(" + str(i.num1) + "," + str(i.num2) + "," + str(i.num3) + ") ")
                        f.write(str(result) + " ")
            if int(m) == int(result):
                f.write("CORRECT" + "\n")
            else:
                f.write("WRONG" + "\n")

f.close()