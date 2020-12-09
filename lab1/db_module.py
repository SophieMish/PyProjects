from pony.orm import Database, Required, Optional, PrimaryKey, Json, db_session, select, delete, get, count, Set
from datetime import date
from prettytable import PrettyTable


# -------------------------------Work with database---------------------------#
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


db.bind(provider='sqlite', filename='phonebook')
db.generate_mapping(create_tables=True)

# db.bind(provider='postgres', user='root', password='567066', host='localhost', database='phonebook_db')
print("You are connected to Database 'Phonebook'")


# -----------------------------------------------------------------------------------------------#


@db_session
def print_tab(data=None):
    if data == '':
        data = select(p for p in Person)[:]
    elif data is None:
        print("There are no data!!!")
    table = PrettyTable()
    print('')
    table.field_names = ["Name", "Surname", "Birthday", "Phone"]
    for d in data:
        phone = ''
        for p in d.phones:
            phone += f'{p.type_of_phone} : {p.number}\n'
        table.add_row([d.name, d.surname, d.birthday, phone])
    if len(data[:]) == 0:
        print("There are no data!!!")
    else:
        print(table)


# ----------------------------adding data--------------------------#
@db_session
def add_person(name, surname, phone, type_of_phone, birthday=None):
    if count(p for p in Person if p.name == name and p.surname == surname) != 0:
        raise Exception("Error! We already had this person in the phonebook!!!")
    person = Person(name=name, surname=surname,
                    birthday=birthday)
    phone = Phone(type_of_phone=type_of_phone, number=phone, person=person)



@db_session
def add_phone(name, surname, phone, type_of_phone):
    person = Person.get(name=name, surname=surname)
    phone = Phone(type_of_phone=type_of_phone, number=phone, person=person)
    print('You added a phone!')


# -----------------changing data------------------------------#
@db_session
def change_phone(old_phone, new_phone='', type_of_new_phone=''):
    phone = Phone.get(number=old_phone)
    if new_phone != '':
        phone.number = new_phone
    if type_of_new_phone != '':
        phone.type_of_phone = type_of_new_phone
    res = search(phone=new_phone)
    print_tab(res)


@db_session
def change_person_data(old_name='', old_surname='', new_name='', new_surname='', new_birthday=''):
    get_person_data = Person.get(name=old_name, surname=old_surname)
    if new_name != '':
        get_person_data.name = new_name
    if new_surname != '':
        get_person_data.surname = new_surname
    if new_birthday != '':
        get_person_data.birthday = new_birthday
    res = search(name=new_name,surname=new_surname,birthday=new_birthday)
    print_tab(res)


# -------------------deleting data----------------------------#
@db_session
def del_person_by_phone(num_phone):
    res = search(phone=num_phone)
    print_tab(res)
    delete(p for p in Person for ph in p.phones if ph.number == num_phone)



@db_session
def del_phone(num_phone):
    print_tab(search(phone=num_phone))
    delete(p for p in Phone if p.number == num_phone)


@db_session
def del_person(name, surname):
    print_tab(search(name=name,surname=surname))
    delete(p for p in Person if p.name == name and p.surname == surname)


# ------------------------------------------------------------------#


# ---------------search-------------------------------#
@db_session
def search(name='', surname='', phone='', birthday=None):
    query = select(p for p in Person)
    if surname != '':
        query = query.filter(lambda p: p.surname == surname)
    elif name != '':
        query = query.filter(lambda p: p.name == name)
    elif phone != '':
        query = query.filter(lambda p: phone in p.phones.number)
    # не получилось реализовать(((
    # if birthday is not None:
    #     query = query.filter(lambda p: p.birthday == birthday)
    if len(query[:]) != 0:
        return query[:]
    else:
        return None


# -----------------------------------------------------------#


@db_session
def show_person_by_age(name, surname):
    person = Person.get(name=name, surname=surname)
    today = date.today()

    return today.year - person.birthday.year - ((today.month, today.day) < (person.birthday.month, person.birthday.day))
