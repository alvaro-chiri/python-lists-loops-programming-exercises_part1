import datetime


people = [
	{ "name": 'Joe', "birthDate": datetime.datetime(1986,10,24) },
	{ "name": 'Bob', "birthDate": datetime.datetime(1975,5,24) },
	{ "name": 'Erika', "birthDate": datetime.datetime(1989,6,12) },
	{ "name": 'Dylan', "birthDate": datetime.datetime(1999,12,14) },
	{ "name": 'Steve', "birthDate": datetime.datetime(2003,4,24) }
]


def calculateAge(birthDate):
    today = datetime.date.today()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    return age

name_list = list(map(lambda person:  f'Hello, my name is {person["name"]} and I am {calculateAge(person["birthDate"])} years old' , people))

print(name_list)

name_list = list(map(lambda person: person["name"], people))
age_list = list(map(lambda person: calculateAge(person["birthDate"]), people))

print(list(zip(name_list, age_list)))