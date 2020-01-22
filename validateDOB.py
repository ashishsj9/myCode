
from datetime import datetime


def validateDOB(name, dob):
    dob_obj = datetime.strptime(dob, "%d/%m/%Y")
    birthYear = dob_obj.year
    currentDate = datetime.now()
    currentYear = currentDate.year

    if currentYear < birthYear:
        age = birthYear - currentYear
    else:
        age = currentYear - birthYear - 1
    print(age)
    print("Hello " + name + ", you are " + str(age) + " old")


if __name__ == '__main__':
    validateDOB("ashish", "05/10/1993")