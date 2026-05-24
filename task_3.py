# Question no.1
i1 = 4
f1 = 3.5


def add(a, b):
    result = print(f"The sum is: {a + b} and type is: {type(a + b)}")
    return result


def substract(a, b):
    result = print(f"The difference is: {a - b} and type is: {type(a - b)}")
    return result


def multiply(a, b):
    result = print(
        f"The multiplication is: {a * b} and type is: {type(a * b)}")
    return result


def divide(a, b):
    result = print(f"The division is: {a / b} and type is: {type(a / b)}")
    return result


add(i1, f1)
substract(i1, f1)
multiply(i1, f1)
divide(i1, f1)

# Question no.2
i2 = 100000000000000000000
print(i2)
print(type(i2))

# Question no.3
z = 3 + 4j
print(z.real)
print(z.imag)
print(type(z))

z1 = 5 + 6j
cplx_sum = z + z1
print(cplx_sum)

# Question no.4
m = 10
n = 15
status = m > n
print(status)
print(type(status))
status = m != n
print(status)


# Question no.5
text = "HelloLisa!"
# postive indexing
print(text[0])
# negative indexing
print(text[-1])
# total length of string
print(len(text))

# Question no.6
lang = "PythonProgramming"
sub_string_lang = lang[2:8]
print(sub_string_lang)
sub_string_lang1 = lang[:5]
print(sub_string_lang1)
reversed_str = lang[::-1]
print(reversed_str)

# Question no.7
phrase = "Hello, Python World!"
print(phrase)
phrase_strip = phrase.strip()
print(phrase_strip)
phrase_upper = phrase.upper()
print(phrase_upper)
phrase_replace = phrase.replace("Hello", "Hi")
print(phrase_replace)

# Question no.8
name = "Sabrina"
score = 95
result = f"{name} scored {score} points"
print(result)

# Question no.9
age = 30
is_married = False
# if age is greater than 20 and if marriage is true then pyton gives the result as True
output = (age >= 20) and (is_married == True)
print(output)

# Question no.10
l1 = [1, 2, 3, 4, 5]
first_item, middle_item, last_item = l1[0], l1[2], l1[4]
print(f"First item: {first_item}")
print(f"Middle item: {middle_item}")
print(f"Third item: {last_item}")

# Question no.11
nums = [10, 20, 30, 40]
nums.insert(2, 25)
print(nums)
nums.pop()
print(nums)

# Question no.12
letters = ["a", "b", "c", "d", "e"]
print(letters[1:4])

# Question no.13
l2 = [3, 5, 1, 0, 3]
l2.sort()
print(l2)
print(l2[::-1])

# Question no.14
list1 = [1, 2, 3]
list2 = [4, 5, 6]
# using + method
combined_list = list1 + list2
print(combined_list)

# using .extend
list1.extend(list2)
print(list1)

# Question no.15
f2 = [1.5, 2.5, 3.5, 4.5]
sum_f2 = sum(f2)
print(sum_f2)
print(min(f2))
print(max(f2))

# Question no.16
t = (10, 20, "Hello", True)
print(f"Tuple: {t} and type: {type(t)}")

# Question no.17
print(t[0:2])
print(t[-1])

# Question no.18
t2 = ("Tom", 25, "Engineer")
name, age, profession = t2[0], t2[1], t2[2]
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Profession: {profession}")

# Question no.19
# t[0] = 99. # It throws an error because tuple is immutable and cant be changed once assigned
# print(t)

# Question no.20
my_set = {1, 3, 5, 7}
if my_set.__contains__(5):
    print(True)
else:
    print(False)
if my_set.__contains__(2):
    print(True)
else:
    print(False)

# Question no.21
my_set.add(9)
print(my_set)
my_set.remove(3)
print(my_set)

# Question no.22
set_A = {1, 2, 3}
set_B = {3, 4, 5}
# we can do either .func or direct or, and and - for the result
union = set_A or set_B
intersection = set_A.intersection(set_B)
diff = set_A - set_B

print(union)
print(intersection)
print(diff)

# Question no.23
vals = [1, 2, 2, 3, 3, 3, 4]
vals_set = set(vals)
print(vals)
print(vals_set)

# Question no.24
l3 = [2, 4, 4, 6]
print(l3)
frozen_set_l3 = frozenset(l3)
print(frozen_set_l3)

# Question no.25
a, b, c = 4, 2, 5
result1 = a + b * c
result2 = (a+b) * c
# the result differs because python uses BODMAS rule
print(result1)
print(result2)

# Question no.26
x = 17
y = 4
print(x % y)  # it prints the remainder while performing x/y
print(x//y)  # it prints the quotient as an integer, it ignores the decimal

# Question no.27
p1 = 2**3
p2 = 3**4
result = print(p1 + p2)

# Question no.28
s1 = "Apple"
s2 = "Banana"

print(s1 > s2)
print(s1 < s2)
print(s1 == s2)

# Question no.29
i3 = 5
f3 = 5.0
# it checks if the value of the variables are same
print(f"using == operator: {i3 == f3}")
print(f"using is : {i3 is f3}")  # it checks if the varibles are the same


# Question no.30
# it is checking if 2 is less than 3 and 3 is less than5 , if both returns true it prints true or else it prints false
print(2 < 3 < 5),

# Question no.31
p = True
q = False
print(p)
print(q)

age1 = 18
has_ID = True
result = print(age1 > 18 and has_ID)

# Question no.32
print(f"Print p or q: {p or q}")

# Question no.33
r = 10 > 5
print(r)
print(not r)

# Question no.34
l4 = ["Lisa", 25, "Sabrina", 26, "Laufey", 28, True]
print(len(l4))

# Question no.35

# This function prints the type of the variable


def check_type(value):
    return print(type(value))


check_type(10)
check_type(10.5)
check_type("Ten")
check_type(True)
check_type(3+2j)

# Question no.36
# abs() gives the result in postivite even if its compiled in negative
print(abs(10))
print(abs(-10))
print(abs(-3.5))

# Question no.37
print(round(3.1234345, 2))
print(round(2.5))

# Question no.38
l5 = [1, 2, 3, 4, 5]
print(sum(l5))
print(min(l5))
print(max(l5))

# Question no.39
vals_t = (3, 1, 4, 2)
print(vals_t)

# using sorted(), it sorts the oerder of the tuple and set and gives the result in list
print(sorted(vals_t)),

# Question no.40
b1 = [True, False, True]
print(any(b1))  # if any values in the list is true, it prints True
print(all(b1))  # if any of the values in the list not true, it prints False, i.e all values in the list needs to be true


# Question no.41
a1 = 10 > 3
b1 = 5 == 5

print(a1 or b1)
print(a1 and b1)

# Question no.42
hobby = """
        Coding Everyday
        Writing Songs
        Making Music
        """


def calc_count(letter):
    if letter in hobby.lower() or letter in hobby.upper():
        return print(hobby.count(letter))
    else:
        return print(f"There are no {letter}")


calc_count("a")

# Question no.43
s3 = "ABCDEFGHIJ"
sliced_s3 = s3[::2]
print(sliced_s3)
print(sliced_s3[::-1])

# Question no.44
s4, s5 = "Case", "Case"
print(s4 == s5)
new_s4 = s4.casefold()
print(new_s4)
new_s5 = s5.casefold()
print(new_s5)
print(new_s4 == new_s5)

# Question no.45
name_ = "Ramesh"
product = "Notebook"
quantity = 2
price = 12.50

print(f"{name_} purchased {quantity} {product} for a total of ${price}")


# Question no.
s6 = "0"
print(s6)
s6 = float(s6)
print(s6)
s6 = bool(s6)
print(s6)

# Question no.47
fruits = ["apple", "banana", "cherry"]
print(fruits)
# fruits.sort(reverse=True) # this is to change the original list
# print(fruits)

# this way the orignal list is not changed
sorted_list = sorted(fruits, reverse=True)
print(sorted_list)


sorted_list.reverse()
print(sorted_list)

# Question no.48
l6 = [2, 5, 7, 1, 9]
new_l6 = l6.copy()
new_l6[1:1] = [4]
print(new_l6)
print(l6)

# Question no.49
info = ["John", 28, True, 4500.75]
new_info = [info[0], info[3]]
print(new_info)

# Question no.50
t3 = (1, 2)
t4 = (3, 4)
t5 = t3 + t4
print(t5)
t6 = t3 * 3
print(t6)

# Question no.51
t7 = (42,)
print(type(t7))

i5 = (42)
print(type(i5))

# Question no.52
set_c = {1, 2, 3, 4}
set_d = {1, 2}

print(set_c and set_d)
print(set_c | set_d)

# Question no.53
print(set_d.issubset(set_c))
print(set_c.issuperset(set_c))
