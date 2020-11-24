import random


def comparator(a, prob):
    if a >= prob:
        return 1
    else:
        return 0


def n1(prob, num_of_tests):
    rnum = random.random()
    if num_of_tests == 1:
        return comparator(rnum, prob)
    else:
        l = []
        while num_of_tests > 0:
            rnum = random.random()
            l.append(comparator(rnum, prob))
            num_of_tests -= 1
        return l


print(n1(0.6, 10))


def n2(prob, num_of_tests, num_of_tries):
    l = []
    i = 0
    n = 0
    while num_of_tests > 0:
        while num_of_tries > 0:
            rnum = random.random()
            n += comparator(rnum, prob)
            num_of_tries -= 1
            break
        l.append(n)
        num_of_tests -= 1
        continue
    return l


print(n2(0.8, 4, 3))
