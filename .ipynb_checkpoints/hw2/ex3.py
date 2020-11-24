class Fraction:

    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __repr__(self):
        return self.__str__()

    def __add__(self, other_fract):
        newnum = self.num * other_fract.den + self.den * other_fract.num
        newden = self.den * other_fract.den

        return Fraction(newnum, newden)

    def __mul__(self, other_fract):
        newnum = self.num*other_fract.num
        newden = self.den*other_fract.den

        return Fraction(newnum,newden)



def func():
    for i in enumerate(start=1, i):
        print(i)


num = Fraction(6, 2)
num2 = Fraction(1,3)
print(num*num2)
func()