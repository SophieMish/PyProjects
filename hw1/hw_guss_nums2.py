import random
import sys


def end_game():
    print("Продолжить игру или выйти? любая цифра/любая буква")
    ans = input()
    if ans.isdigit():
        start_game()
    else:
        print("Игра окончена(((")
        sys.exit()

def start_game():
    print("Введите промежуток в котором отгадывание число")
    print("Начало промежутка")
    start = int(input())
    print("Конец промежутка")
    end = int(input())
    if end < start:
        tmp = end
        end = start
        start = tmp
        del tmp
    l = list(range(start, end+1))
    print(l)
    num = l[(len(l)-1) // 2]
    print(
        'Теперь компьютер попытается отгадать число из промежутка, если решишь,что тебе надоело, то набери любую букву\n')
    while True:
        if num >= start and num <= end:
            print("Это ваше число? (да - 1/нет - 0)", num)
            ans = input()
            if ans.isdigit():
                ans = int(ans)
                if ans == 1:
                    break
                else:
                    hint = input("Оно больше (>) или меньше (<) ? ")
                    if hint == ">":
                        num = num + 1
                    elif hint == "<":
                        num = num - 1
                    else:
                        end_game()
            else:
                end_game()
        else:
            print("Выход за границы отрезка [", start, ",", end, "]")
            if num < start:
                num = num + 1
            else:
                num = num - 1
            print("Теперь ваше число:", num)
            continue
    print("Победа!!!")
    end_game()


print("""\nПривет, это игра "Угадай цифру". Основная цель - компьютер должен отгадать число\n""")

start_game()
