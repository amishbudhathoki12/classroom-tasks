# Question.1

t1 = (1, 1.5, "Lisa", True, 1+2j)
print("Answer no.1:")
for e in t1:
    print(f"The element is: {e} and its data type is: {type(e)}")
print("------------------------------------------------------")

# Question no.2
l1 = ["Kathmandu", "Lalitpur", "Bhaktapur", "Pokhara"]
print("Answer no.2:")
for e in l1:
    print(f"{e} is a great place")
print("------------------------------------------------------")

# Question no.3
print("Answer no.3:")
s1 = input("Enter a word:")

for e in enumerate(s1):
    print(f"The word and index are: {e}")
print("------------------------------------------------------")

# Question no.4
print("Answer no.4:")
l2 = [1, 2, 3, 4, 5, 6]
sum = 0
for e in l2:
    sum += e
print(f"The sum of all numbers in list is: {sum}")
print("------------------------------------------------------")

# Question no.5
print("answer no.5:")
t2 = ("Lisa", True, 26, False, "Sabrina", 2+3j, True)
count_bool = 0
for e in t2:
    if e is True:
        count_bool += 1
print(f"There are {count_bool} True values in the tuple")
print("------------------------------------------------------")

# Question no. 6
print("Answer no.6:")
l3 = [1, 2.5, "Sabrina", True, 3+2j, [1, 2]]
for e in l3:
    print(f"The data type of {e} is {type(e)}")
print("------------------------------------------------------")

# Question no.7
print("Answer no.7:")
s2 = input("Enter a word:")

for char in s2:

    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        print(f"{char} is a vowel")

    else:
        print(f"{char} is not a vowel")
print("------------------------------------------------------")

# Question no.8
print("Answer no.8:")
t3 = (1, 2, 3, 4, 5)

for i in t3:
    print(f"The square of {i} is: {i ** 2}")
print("------------------------------------------------------")

# Question no.9
print("Answer no.9:")
l4 = ["lisa", "sabrina", "adele"]

for words in l4:
    words = words.upper()
    print(f"The uppercase of {words.lower()} is {words}")

print("------------------------------------------------------")

# question no. 10
print("Answer no.10:")
l5 = [1, 2, 10, 20, 5, 50, 100]
greater_nums = 0

for i in l5:
    if i > 10:
        greater_nums += 1

print(greater_nums)
