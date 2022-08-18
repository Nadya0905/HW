'''# шнурки
a = 2
b = 1
N = 8
n = N // 2
print((2 * a * n - a) + 2 * b * (n - 1))


# sum digits
num = 123
print(num % 10 + ((num // 10)) % 10 + num // 100)

# stroka srezy
s = "abcdefg"
print(s[2])
print(s[-2])
print(s[:5])
print(s[:-2])
print(s[::2])
print(s[1::2])
print(s[::-1])
print(s[::-2])
print(len(s))

# replace H
s = 'hhhhhhh'
s = s.replace('h', 'H', s.count('h') - 1)
s = s.replace('H', 'h', 1)
print(s)

# last digit
a = 123
print(a % 10)

# 10-s count
n = 546
print(n // 10 % 10)

firstname = 'John'
lastname = 'Smith'

stringa = 'Hello, {name} {fam}'.format(name=firstname, fam=lastname)
print(stringa)

from math import sin, radians, factorial
x = radians(180)
eps = 0.00000000001
k = 0
print(round(sin(x), 5))
print()

summ = 0
next_part = 1

while abs(next_part) > eps:
    next_part = pow(-1, k) * pow(x, 2 * k + 1) / factorial(2 * k + 1)
    summ += next_part
    k += 1
    print(round(summ, 5))


arr = [11, 20, 31, 45, 50]

for item in arr:
    if item % 2 == 0:
        print(f"This item is chetnoe: {item}")
    else:
        print("Not chetnoe")


value = 0

print(f"{value} < 5")
while value < 5:
    value += 1
    if value == 3:
        continue
    print(f"{value} < 5")


# factorial

def fact(value):
    fct = 1
    for i in range(1, value+1):
        fct *= i

    return fct

for i in range(0, 5):
    print(i/fact(i))


value = 0
while value < 5:
    value += 1
    if value == 3:
        continue
    print(f"{value} < 5")


from math import factorial, e, log

x = float(input('*Тык*: '))
exp = 0.0001
rez = 0
n = 1
syl = 1
while abs(syl) > exp:
    syl = ((pow(-1, n+1)) * ((pow(x, n))) / n)
    n += 1
    rez += syl
print(rez)
print(log(1+x))'''




'''x = float(input("Set X: "))
m = float(input("Set m: "))
n = 1
eps = 0.001
summ = 1
proizv = 1
next_part = 1

while abs(next_part) > eps:
    for k in range(1, n + 1):
        proizv *= (m - k + 1) / k

    summ += proizv
    n += 1
    next_part = proizv
    proizv = 1

print(f"Result: {summ}")


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name: str, age: int, groupnumber: str):
        super().__init__(name, age)
        self.groupnumber = groupnumber

    def go_to_the_class(self):
        if self.groupnumber == "12345":
            print(f"I am here! {self.name=}")
        elif self.groupnumber == "54321":
            print(f"CANCEL")

    @classmethod
    def test_method(cls):
        print("Call test method")


student_1 = Student("Ivan", 20, "12345")
student_2 = Student("Masha", 25, "54321")

student_1.go_to_the_class()
student_2.go_to_the_class()

person_1 = Person("Kate", 24)
print(person_1.name)
print(student_1.name)
print(student_1.groupnumber)'''





import json


class Person:
    def __init__(self, *args):
        self.name, self.birthday, self.height, \
        self.weight, self.car, self.languages = args

    def get_dict(self):
        return {
            "name": self.name,
            "birthday": self.birthday,
            "height": self.height,
            "weight": self.weight,
            "car": self.car,
            "languages": self.languages
        }


with open("jsonfile.json", "r") as jfile:
    data_list = json.load(jfile)

obj_list = list()

for item in data_list:
    new_obj = Person(item["name"], item["birthday"], item["height"],
                     item["weight"], bool(item["car"]), list(item["languages"]))
    obj_list.append(new_obj)

new_person = Person("Kate", "02-02-2000", 165, 56, False, ['Python', 'Assembler'])
obj_list.append(new_person)

data_list.append(new_person.get_dict())

with open("jsonfile.json", "w") as jfile:
    json.dump(data_list, jfile, indent=4)













