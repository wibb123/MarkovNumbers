class Markov:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def is_markov_triple(self):
        if self.num1**2 + self.num2**2 + self.num3**2 == 3 * self.num1 * self.num2 * self.num3:
            return True
        else:
            return False

    def next_markov_triple_min(self):
        if self.num1 <= self.num2 and self.num1 <= self.num3:
            self.next_markov_triple1()
        elif self.num2 <= self.num1 and self.num2 <= self.num3:
            self.next_markov_triple2()
        else:
            self.next_markov_triple3()

    def next_markov_triple1(self):
        self.num1 = 3 * self.num2 * self.num3 - self.num1

    def next_markov_triple2(self):
        self.num2 = 3 * self.num1 * self.num3 - self.num2

    def next_markov_triple3(self):
        self.num3 = 3 * self.num1 * self.num2 - self.num3

    def next_two_trips(self):
        if self.num1 >= self.num2 and self.num1 >= self.num3:
            calc1 = 3 * self.num1 * self.num3 - self.num2
            calc2 = 3 * self.num1 * self.num2 - self.num3
            next1 = Markov(self.num1, calc1, self.num3)
            next2 = Markov(self.num1, self.num2, calc2)
            return next1, next2
        elif self.num2 >= self.num1 and self.num2 >= self.num3:
            calc1 = 3 * self.num2 * self.num3 - self.num1
            calc2 = 3 * self.num1 * self.num2 - self.num3
            next1 = Markov(calc1, self.num2, self.num3)
            next2 = Markov(self.num1, self.num2, calc2)
            return next1, next2
        elif self.num3 >= self.num2 and self.num3 >= self.num1:
            calc1 = 3 * self.num1 * self.num3 - self.num2
            calc2 = 3 * self.num3 * self.num2 - self.num1
            next1 = Markov(self.num1, calc1, self.num3)
            next2 = Markov(calc2, self.num2, self.num3)
            return next1, next2

    def maximum(self):
        m = max(self.num1, self.num2, self.num3)
        return m
