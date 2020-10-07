import math

def find_primes():
    print('Введите число до которого будем искать простые числа:')
    n = int(input())
    l = list()
    if n == 2 or n == 1:
        return n
    else:
        for num in range(2, n):
            if all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1)):
                l.append(num)

    return l


def find_gcd():
    a = int(input("Введите a:"))
    b = int(input("Введите b:"))
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a

    gcd = a + b
    return gcd


def find_dividers():
    num = int(input("Введите число для поиска делителей:"))
    l = list()
    for i in range(1, num + 1):
        if num % i == 0:
            l.append(i)
    return l


#print("Простое/ые число/a: ",find_primes())
#print("НОД:", find_gcd())
print("Делители числа:", find_dividers())
