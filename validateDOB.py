import datetime


def validatedob(name, dob):
    dob_obj = datetime.datetime.strptime(dob, "%m/%d/%y")
    birth_year = dob_obj.year
    current_year = datetime.date.today().year

    if current_year < birth_year:
        age = birth_year - current_year
    else:
        age = current_year - birth_year - 1
    print(age)
    print("Hello " + name + ", you are " + str(age) + " old")


if __name__ == '__main__':
    validatedob("ashish", "05/10/1993")