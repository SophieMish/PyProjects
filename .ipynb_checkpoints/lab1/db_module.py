from pony.orm import Database, Required, Optional, PrimaryKey, Json, db_session, select, delete, get, count, Set
from datetime import date
from prettytable import PrettyTable

db = Database()


class Person(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    surname = Required(str)
    birthday = Optional(date)

    phones = Set("Phone")


class Phone(db.Entity):
    id = PrimaryKey(int, auto=True)
    type_of_phone = Required(str)
    number = Required(str)

    person = Required("Person")


db.bind(provider='postgres', user='lms', password='Varvash4', host='hsebi.ru', database='Phonebook', port='5432')
db.generate_mapping(create_tables=True)
print("You are connected to Database 'Phonebook'")


@db_session
def print_table():
    data = select(p for p in Person)[:]
    table = PrettyTable()
    table.field_names = ["Name", "Surname", "Birthdate", "Phone"]
    for d in data:
        phone = ''
        for p in d.phones:
            phone += f'{p.type_of_phone} : {p.number}\n'
        table.add_row([d.name, d.surname, d.birthday, phone])
    print(table)


@db_session
def add_person(name, surname, phone, type_of_phone, birthday):
    if count(p for p in Person if p.name == name and p.surname == surname) != 0:
        raise Exception("Error! This person is")
    person = Person(name=name, surname=surname,
                    birthday=birthday)
    phone = Phone(type_of_phone=type_of_phone, number=phone, person=person)


@db_session
def del_person(name, surname):
    delete(p for p in Person if p.name == name and p.surname == surname)


@db_session
def del_person_by_phone(num_phone):
    delete(p for p in Person for ph in p.phones if ph.number == num_phone)


@db_session
def add_phone(name, surname, phone, type_of_phone):
    # person = select(p for p in Person if p.name == name and p.surname == surname)[:]
    person = Person.get(name=name, surname=surname)
    phone = Phone(type_of_phone=type_of_phone, number=phone, person=person)


@db_session
def change_phone(old_phone, new_phone, type_of_new_phone):
    phone = Phone.get(number=old_phone)
    phone.number = new_phone
    phone.type_of_phone = type_of_new_phone


@db_session
def del_phone(num_phone):
    delete(p for p in Phone if p.number == num_phone)


def welcome():
    print("Hello! This is a phonebook. Choose the option:\n"
          "0 - Quit\n"
          "1 - View all directory entries\n"
          "2 - Search by reference\n"
          "3 - Add a new entry\n"
          "4 - Remove an entry from the directory\n"
          "5 - Change a field\n"
          "6 - Show person's age by name and surname\n"
          )
    while True:
        try:
            ans = int(input("My choice:"))
            if ans > 7:
                return ans
                raise Exception
            break
        except ValueError:
            print('Input Error, please try to type again')
        except Exception:
            print('Input Error, please try to type again')


def search_by_reference():
    return


def addd_new_entity():
    return


def remove_entity():
    return


def change_field():
    return
def show_person_by_age():
    return
def quit():
    print("Nice to see you in the next time!")
    exit(0)

def choose_option(ans):
    if ans == 0:
        quit()
    elif ans == 1:
        print_table()
    elif ans == 2:
        search_by_reference()
    elif ans == 3:
        addd_new_entity()
    elif ans == 4:
        remove_entity()
    elif ans == 5:
        change_field()
    elif ans == 7:
        show_person_by_age()



if __name__ == "__main__":
    ans = welcome()
    choose_option(ans)

    # try:
    #     add_person(name='John', surname='Hold', type_of_phone='home', phone='123456', birthday=date(2001, 1, 31))
    # except Exception:
    #     pass
    # change_phone('16789','16789','Home')
    # del_person_by_phone('16789')
    # add_phone('John', 'Hold', '89290412152', 'Personal')
    # del_person('John', 'Hold')
    # del_phone('123456')

    print_table()
