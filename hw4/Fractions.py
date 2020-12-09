import math


class Franction:
    def __init__(self, num, den):
        self.num = num
        self.den = den
        self.n = 0
        self.d = 0
        if den == 0:
            raise ZeroDivisionError("The demoninator cannot be zero.")

    def __add__(self, other):
        if self.den == other.den:
            self.n = self.num + other.num
            return self
        else:
            cd = int(self.den * other.den / math.gcd(self.den, other.den))
            rn = int(cd / self.den * self.num + cd / other.den * other.num)
            g2 = math.gcd(rn, cd)
            self.n = int(rn / g2)
            self.d = int(cd / g2)
            return self if self.num != self.den else self.n

    def __sub__(self, other):
        if self.den == other.den:
            self.n = self.num - other.num
            return self
        else:
            cd = int(self.den * other.den / math.gcd(self.den, other.den))
            rn = int(cd / self.den * self.num - cd / other.den * other.num)
            g2 = math.gcd(rn, cd)
            self.n = int(rn / g2)
            self.d = int(cd / g2)
            return self if self.num != self.den else self.n

    def __mul__(self, other):
        self.n = self.num * other.nun
        self.d = self.den * other.den
        return self

    def __eq__(self, other):
        return self is other


    # def __divmod__(self,other):
    #     div = self.num*other.den//(self.den*other.num)
    #     mod = self.num*other.den%(self.den*other.num)
    #     return div, mod


    def __ne__(self,other):
        return self is not other

    def __str__(self):
        if self.d == 1:
            return '{}'.format(self.n)
        else:
            return '{}/{}'.format(self.n, self.d)

    def __repr__(self):
        if self.d == 1:
            return '{}'.format(self.n)
        else:
            return '{}/{}'.format(self.n, self.d)


frec = Franction(30, 6)
frec1 = Franction(30, 5)
print(frec - frec1)
print(frec1 + frec)
is_eq = (frec != frec1)
print(is_eq)
