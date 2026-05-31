from functools import reduce

# Question no.1:
print("Answer no.1:")


class Person:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

   
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    # Setter methods
    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age



person1 = Person("Lisa", 26)


print(f"Name from get method: {person1.get_name()}")
print(f"Age from get method: {person1.get_age()}")


person1.set_name("Sabrina")
person1.set_age(28)



print(f"Name after modification: {person1.get_name()}")
print(f"Age after modification: {person1.get_age()}")

print("----------------------------------")

# Question no.2
print("Answer no.2:")


class Person:
    def details(self):
        print("These are the details of person.")


class Laptop():
    def details(self):
        print("These are the details of Laptop.")


class Camera():
    def details(self):
        print("These are the details of Camera")


def show_details(obj):
    obj.details()


person2 = Person()
laptop1 = Laptop()
camera1 = Camera()

show_details(person2)
show_details(laptop1)
show_details(camera1)

print("----------------------------------")

# Question no.3
print("Answer no.3:")


class Vechile:
    def start(self):
        print("The vechile is starting")


class Bike(Vechile):
    def wheel(self):
        print("Two wheeler")


b1 = Bike()
b1.start()
b1.wheel()

print("----------------------------------")

# Question no.4
print("Answer no.4:")


class Singer:
    def sing(self):
        print("Has a excellent voice")


class Dancer:
    def dance(self):
        print("Have excellent moves")


class Performer(Singer, Dancer):
    pass


p1 = Performer()
p1.sing()
p1.dance()
print("----------------------------------")

# Question no.5

print("Answer no.6:")

class Appliance:
    def power_on(self):
        print("Appliance is powered on")


class WashingMachine(Appliance):
    def wash(self):
        print("Washes clothes")


class Microwave(Appliance):
    def heat(self):
        print("Heats food")


wash_machine = WashingMachine()
microwave = Microwave()

print("Inheritance for Washing Machine:")
wash_machine.power_on()
wash_machine.wash()

print("Inheritance for Microwave:")
microwave.power_on()
microwave.heat()
print("----------------------------------")

# Question no.6

print("Answer no.6:")


class Pencil:
    def write(self):
        print("Writes with a pencil")


class Pen:
    def write(self):
        print("Writes with a pen")


def show_writing_tool(obj):
    obj.write()


objects = [
    Pencil(),
    Pencil(),
    Pencil(),
    Pen(),
    Pen(),
    Pen()
]

for obj in objects:
    show_writing_tool(obj)
print("----------------------------------")

# Question no.7
print("Answer no.7:")


class Person_1:
    def __init__(self, age):
        self.__age = 0
        if age > 0:
            self.__age = age
        else:
            print("Invalid age, Age cant be negative.")

    def get_age(self):
        print(f"The age is: {self.__age}")

    def set_age(self, value):
        if value > 0:
            self.__age = value
        else:
            print("Invalid age, Age cant be negative.")


p2 = Person_1(16)
p2.get_age()
p2.set_age(value=23)
p2.get_age()

print("----------------------------------")

# Question no.8

print("Answer No.8:")


class Company:
    def company_name(self):
        print("This prints the company name")


class Department(Company):
    def department_name(self):
        print("This prints the department name")


class Employee(Department):
    def employee_name(self):
        print("This prints the employee name")


employee1 = Employee()
employee1.employee_name()
employee1.company_name()
employee1.department_name()

print("----------------------------------")

# Question no. 9
print("Answer no.9:")
num = lambda n : True if n>0 else False
print(num(1))
print("----------------------------------")

# Question no. 10
print("Answer no.10:")
char = lambda word : word[0]
print(char("Sabrina"))
print("----------------------------------")

#Question no.11
print("Answer no. 11:")
l = [1,2,3,4,5]
result = map(lambda x: x+10, l)
print(list(result))
print("----------------------------------")

# Question no.12
print("Answer no.12:")
l2 = ["apple", "banana", "kiwi"]
outupt = map(lambda l: len(l), l2)
print(list(outupt))
print("----------------------------------")

# Question no.12
print("Answer no.13:")
l3 = [10,55,60,23,90]
result = filter(lambda n: n>50, l3)
print(list(result))
print("----------------------------------")

# Question no.14
print("Answer no.14:")
l4 = ["P","Y","T","H","O","N"]

join = reduce(lambda l,y : l + y, l4 )
print(join)

