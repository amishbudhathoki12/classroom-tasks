# Question no.1
# initializing an integer variable
n1 = 5

# this condition checks if the number is divisible by 2 and returns the if print statement else it prints else print statement
if n1 % 2 == 0:
    print(f"{n1} is an even number.")
else:
    print(f"{n1} is an odd number.")

# Question no.2

# this condition checks if n1 is equal ot 0 , less than 0 or greater than 0 and gives the respective priont result
if n1 == 0:
    print(f"{n1} is zero.")
elif n1 > 0:
    print(f"{n1} is positive number")
else:
    print(f"{n1} is a negative number")

# Question no.3

# this function gives the grade for a certain amount of marks that is entered


def calc_grade(marks):
    if marks >= 90:
        return print(f"You have obtained grade A")
    elif marks >= 80:
        return print(f"You have obtained grade B")
    elif marks >= 70:
        return print(f"You have obtained grade C")
    else:
        return print("You have been failed.")


# calling the func calc_grade we created to get the result
calc_grade(90)

# Question no. 4
list_num = list(range(1, 101))

# this is for loop used to get the result for respective conditions
for i in list_num:
    if i % 3 == 0 and i % 5 == 0:
        print(f"The number divisible by both 3 and 5 are: {i}")

print("--------------------------------------------")
for i in list_num:
    if i % 3 == 0 and i % 5:
        print(f"The number divisible by 3 but not 5 are: {i}")

print("--------------------------------------------")

for i in list_num:
    if i % 5 == 0 and i % 3:
        print(f"The number divisible by 5 but not 3 are: {i}")

print("--------------------------------------------")

# Question no. 5

password = "secret"

if password == "secret":
    print(f"Access granted")
else:
    print(f"Access denied")

# Question no. 6

letters = "abcdefghijklmnopqrstuvwxyz"

for e in letters:
    if e in "aeiou":
        print(
            f"The vowels in the given string are: {e} and the count is: {letters.count(e)} ")
print("--------------------------------------------")
# bonus:
for e in letters:
    if e != "a" and e != "e" and e != "i" and e != "o" and e != "u":
        print(
            f"The vowels in the given string are: {e} and the count is: {letters.count(e)} ")

# Quesiton no.7
num1 = 1
num2 = 2
num3 = 3

if num1 < num2 and num3:
    print(f"Num1: {num1} is smallest")
elif num2 < num1 and num3:
    print(f"Num2: {num2} is smallest")
else:
    print(f"Num3: {num3} is smallest")


# Question no. 8

enter_number = input("Enter either 1, 2 or 3: ")

if enter_number == "1":
    print("Game starting...")
elif enter_number == "2":
    print("Opening settings...")
elif enter_number == "3":
    print("Exiting...")
else:
    print("DO NOT ENTER NUMBER HIGHER THAN 3")
