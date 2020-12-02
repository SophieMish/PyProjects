from pony.orm import db_session
import datetime
from db_module import *
import os


# <<<Просмотр всех записей справочника:>>>
# вывод всего справочника так, чтобы было читабельно. +
# <<<Поиск по справочнику.>>>
# Поиск может осуществляться по любому из полей,
# а также по нескольким полям одновременно (например, найти запись с именем «А» и фамилией «Б»).+
# В результате поиска должны быть выведены найденные записи со значением полей. +
# <<<Добавление новой записи>>>
# NB: Обязательна проверка на то, что такая запись не содержится в справочнике (по уникальному идентификатору). +
# Если такая запись уже содержится в справочнике,
# сообщить об этом пользователю и предложить: изменить существующую запись, -доделать!!!!!
# изменить (Имя, Фамилия) новой записи или вернуться к выбору команды. -
# <<<Валидация>>
# NB: При вводе Имени и Фамилии обязательна автозамена первой буквы на заглавную. -
# Удаление записи из справочника по Имени и Фамилии
# Изменение любого поля в определенной записи справочника
# Вывод возраста человека (записи) по Имени и Фамилии +

def welcome():
    print(f'{os.linesep}', "Choose the option:", f'{os.linesep}',
          "0 <- Quit", f'{os.linesep}',
          "1 <- View all directory entries", f'{os.linesep}',
          "2 <- Search by reference", f'{os.linesep}',
          "3 <- Add a new entry", f'{os.linesep}',
          "4 <- Remove an entry from the directory", f'{os.linesep}',
          "5 <- Change a field", f'{os.linesep}'
                                 " 6 <- Show person's age by name and surname", f'{os.linesep}')
    return validate_choice(6)


def validate_choice(n):
    while True:
        try:
            ans = input("My choice ᐅ ")
            if not ans:
                ans = ''
            if ans == 'exit':
                raise Exception
            else:
                ans = int(ans)
            if ans > n:
                continue
            break
        except ValueError:
            print('Input Error, please try to type again!')
    return ans


def validate_date():
    while True:
        try:
            ans = input('Enter the date ᐅ')
            if ans =='':
                ans = None
            elif ans == 'exit':
                raise Exception
            else:
                ans = datetime.datetime.strptime(ans, '%d-%m-%Y')
            break
        except ValueError:
            print('Input Error, please try to type again. Incorrect data format, should be DD-MM-YYYY')
    return ans


#  Input 0 - validate type of phone or 1 - validate phone
#  Output - ans. It is the type of phone or the phone
def validate_phone(param=0):
    while True:
        try:
            if param == 0:
                print("Enter the type of your phone", f'{os.linesep}',
                      "Personal - 0", f'{os.linesep}',
                      "Home - 1")
                ans = validate_choice(2)
                if ans == 0:
                    ans = ' Personal'
                elif ans == 1:
                    ans = "Home"
                elif ans == '':
                    ans = ''
                break


            elif param == 1:
                ans = str(input("Enter your phone. It can be 11(Personal) or 6(Home) numbers long ᐅ"))

                if ans == 'exit':
                    raise Exception
                elif ans == '':
                    break
                elif ans[0] == '+' and ans[1] == '7' and len(ans) == 12:
                    ans = '8' + ans[2:]
                    break
                elif ans[0] == '8' and len(ans) == 11:
                    break
                elif len(ans) == 6:
                    break
                else:
                    print("Error! Input is wrong! Try again")
                    continue
            else:
                print("Error!")
                return 0
        except ValueError:
            print('Input Error, please try to type again')
    return ans


#  Input 0 - validate name or 1 - validate surname
#  Output - ans. It is the name or the surname
def validate_name_and_surname(param=0):
    while True:
        try:
            if param == 0:
                ans = str(input('Enter the name of the person ᐅ'))
                if ans == '':
                    break
                if ans == 'exit':
                    raise Exception
                if ans.isdigit():
                    continue
                break

            elif param == 1:
                ans = str(input('Enter the surname of the person ᐅ'))
                if ans == 'exit':
                    raise Exception
                if ans == '':
                    break
                if ans.isdigit():
                    continue
                break
            else:
                print("Error!")
                return 0
        except ValueError:
            print('Input Error, please try to type again')
    return ans.title()


def add_new_entity():
    print(" Person - 0", f'{os.linesep}',
          "Phone - 1")
    ans = validate_choice(2)
    if ans == 0:
        name = validate_name_and_surname(0)
        surname = validate_name_and_surname(1)
        type_of_phone = validate_phone(0)
        phone = validate_phone(1)
        birthday = validate_date()
        try:
            add_person(name, surname, phone, type_of_phone, birthday)
            print('You added a person!')
        except Exception as e:
            print(e)
            return 0

    elif ans == 1:
        name = validate_name_and_surname(0)
        surname = validate_name_and_surname(1)
        type_of_phone = validate_phone(0)
        phone = validate_phone(1)
        add_phone(name, surname, phone, type_of_phone)


def quit():
    print("Nice to see you in the next time!")
    exit(0)


def print_table():
    print("ALL INFORMATION:")
    print_tab('')


@db_session
def search_by_reference():
    print("You can write the parameters below or skip, tap the enter key")
    name = validate_name_and_surname(0)
    surname = validate_name_and_surname(1)
    phone = validate_phone(1)
    try:
        query = search(name, surname, phone)
    except ValueError:
        query = search(name, surname, phone)
    print_tab(query)


@db_session
def show_person_age():
    name = validate_name_and_surname(0)
    surname = validate_name_and_surname(1)
    res = search(name, surname)
    if res is not None:
        print_tab(res)
        print("The age of", name, surname, 'is', show_person_by_age(name, surname))
    else:
        print("Error! It is impossible to find the person!")
        show_person_age()


def remove_entity():
    print("Enter the type of deleting", f'{os.linesep}',
          "Delete person by phone - 0", f'{os.linesep}',
          "Delete phone - 1", f'{os.linesep}',
          "Delete person by name and surname - 2", f'{os.linesep}')
    ans = validate_choice(3)
    if ans == 0:
        del_person_by_phone(validate_phone(1))
        print("We deleted this person!")
    elif ans == 1:
        del_phone(validate_phone(1))
        print("We deleted this phone!")
    elif ans == 2:
        del_person(validate_name_and_surname(0), validate_name_and_surname(1))
        print("We deleted this person!")
    else:
        print("Error! Please try to type again!")
        remove_entity()


@db_session
def change_field():
    print("Enter the type of changing", f'{os.linesep}',
          "Change phone - 0", f'{os.linesep}',
          "Change personal data - 1", f'{os.linesep}')
    ans = validate_choice(2)
    if ans == 0:
        print('Old phone')
        old_phone = validate_phone(1)
        if search(phone = old_phone) is not None:
            print('New phone')
            new_phone = validate_phone(1)
            print('The type of new phone')
            type_of_new_phone = validate_phone(0)
            change_phone(old_phone, new_phone, type_of_new_phone)
            print("Data was changed!")
        else:
            print("It is impossible to find a person!",f'{os.linesep}')
            change_field()

    elif ans == 1:
        print('Old name and surname')
        old_name = validate_name_and_surname(0)
        old_surname = validate_name_and_surname(1)
        if search(name = old_name,surname = old_surname) is not None:
            print('New name and surname')
            new_name = validate_name_and_surname(0)
            new_surname = validate_name_and_surname(1)
            new_birthday = validate_date()
            change_person_data(old_name, old_surname, new_name, new_surname, new_birthday)
            print("Data was changed!")
        else:
            print("It is impossible to find a person!",f'{os.linesep}')
            change_field()
    else:
        print("Error! Please try to type again!")


def choose_option(ans):
    if ans == 0:
        quit()
    elif ans == 1:
        print_table()
    elif ans == 2:
        search_by_reference()
    elif ans == 3:
        add_new_entity()
    elif ans == 4:
        remove_entity()
    elif ans == 5:
        change_field()
    elif ans == 6:
        show_person_age()


if __name__ == "__main__":
    print('Hello! This is a phonebook')
    while True:
        while True:
            try:
                ans = welcome()
                choose_option(ans)
            except Exception:
                break
