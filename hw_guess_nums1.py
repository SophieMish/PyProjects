import random
import sys


def choose_level():
    print(" Выбери уровень ->")
    lvl = int(input())
    if lvl == 1 or lvl == 2:
        return lvl
    else:
        print("Ошибка!!! Выберите уровень еще раз")
        choose_level()


def generate_random_num(lvl):
    if lvl == 1:
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
        fnum = random.randrange(start, end)
    else:
        print("Сейчас компьютер предложит тебе отгадать число...")
        fnum = random.randint(0, 500)
    return fnum


def end_game():
    print("Продолжить игру или выйти? любая цифра/любая буква")
    ans = input()
    if ans.isdigit():
        start_game()
    else:
        print("Игра окончена(((")
        sys.exit()


def start_game():
    lvl = choose_level()
    fnum = generate_random_num(lvl)
    print('Теперь попытайся отгадать число из промежутка, если решишь сдаться, то набери любую букву')
    print("Введи число сюда ->")
    num = input()
    if num.isdigit():
        num = int(num)
        while fnum != num:
            num = int(num)
            if fnum > num:
                print("Ваше число меньше, введите число ещё раз")
                num = input()
                if num.isdigit():
                    continue
                else:
                    print("Кажеться вы сдались!")
                    end_game()
            elif fnum < num:
                print("Ваше число больше, введите число ещё раз")
                num = input()
                if num.isdigit():
                    continue
                else:
                    print("Кажется вы сдались!")
                    end_game()
    else:
        end_game()
    print("Победа!!!")
    end_game()


print("""\nПривет, это игра "Угадай цифру". В ней существует 2 уровня сложности.\n
1) Ты задаешь промежуток и программа рандомно выбирает число для угадывания\n
2) Программа сама выбирает промежуток и загадывает число. """)

start_game()
