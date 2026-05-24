# Question no.1
# initializing , three variables that consists integer, float and complex values
my_int = 23
my_float = 22.33
my_complex_num = 4 + 6j

# printing each data types
print(type(my_int))
print(type(my_float))
print(type(my_complex_num))

# Question no. 2
# creation of two variables that consists int value
a = 10
b = 5


# defining functions that returns the calculation of two numbers

def sum(a, b):
    return a + b


def diff(a, b):
    return a - b


def multiply(a, b):
    return a * b


def quotient(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by 0 is not allowed!"


# defing the function that prints the result and its type
def calculation(expression):
    if expression == "+":
        return print(f"The sum is : {sum(a, b)} and data type is: {type(sum(a, b))}")
    elif expression == "-":
        return print(f"The difference is : {diff(a, b)} and data type is: {type(diff(a, b))}")
    elif expression == "*":
        return print(f"The multiplication is : {multiply(a, b)} and data type is: {type(multiply(a, b))}")
    elif expression == "/":
        return print(f"The quotient is : {quotient(a, b)} and data type is: {type(quotient(a, b))}")
    else:
        return "Invalid operator. Please use +, -, *, or /."


# calling the method for the result
calculation("+")
calculation("-")
calculation("*")
calculation("/")

# Question no.3
x = 10
y = 7

# priting if greater result: if x is greater than y, it prints True , if not it prints False
greater = x > y
if greater == True:
    print(greater)
else:
    print(False)

# priting if less than result: if x is less than y ,  it prints True , if not it prints False

less_than = x < y
if less_than == True:
    print(less_than)
else:
    print(False)

# printing equals to result : if x equals to y  it prints True , if not it prints False
equals_to = x == y
if equals_to == True:
    print(equals_to)
else:
    print(False)

#  printing not equals to : if x is not equal to y it prints True , if  it is , it prints False
not_equal_to = x != y
if not_equal_to == True:
    print(not_equal_to)
else:
    print(False)

# Quesstion no.4:

# initializing a variable that consist bool value
status = True
print(status)
# printing the type of the variable status
print(type(status))

# reassigning the status to false
status = False
print(status)

# Question no. 5

#  Initializing a variable that consists string value
text = "Hello Lisa"
print(text)

# printing the length of the variable
print(len(text))

# printing the type of the variable
print(type(text))

# Question no.6

# initializing a string varaible
text = "Stay Motivated and Keep Coding"
print(text)

# Using str indexing to print each character
new_text = text[:]
print(new_text)

# printing first and last characters using negative indexing
neg_ind_text = text[-1:: -28]
print(neg_ind_text)

# Question no. 7

# initializing a str variable
lang = "Programming"
print(lang)

# printing sub str from index  0 to 4
new_lang1 = lang[0:4]
print(new_lang1)

# printing sub str from index 3 to end
new_lang2 = lang[3:]
print(new_lang2)

# printing sub str that omits first 2 and last 2 characters
new_lang3 = lang[2:9]
print(new_lang3)

# Question no.8:
#
# checking the length of lang and lang_sliced to see the difference
print(len(lang))
lang_sliced = lang[:7]
print(lang_sliced)
print(len(lang_sliced))

# Question no. 9

# initializing a str varaible
phrase = "Hello, Sabrina"

# using .upper() method : Changes to Upper case letters
phrase_one = phrase.upper()
print(phrase_one)

#  using . lowe()method: Changes to lower case letters
phrase_two = phrase.lower()
print(phrase_two)

# printing phrase to show it remains unchanged because string are immutable:
print(phrase)

# Question no. 10

#  initializting two str variables
str_1 = "Data"
str_2 = "Science"
print(str_1)
print(str_2)

# combining two strings in single string with a space
combined_str = str_1 + " " + str_2

# printing the combined string and its length
print(combined_str)
print(len(combined_str))

# Question no. 11

# initializing a str variable
word = "example"
word.upper()
# it doesnt do anything because the string is immutable once assigned a value
print(word)

# when we do this with = sign  we are telling python to overwrite the orginal string
word = word.upper()
print(word)

# Question no.12

# initializinf three int variables

a, b, c = 5, 3, 2

# definig function that returns expression


def calculate_expression(a, b, c):
    # here it first does (a+b) then it multiplies this result with c, using BODMAS rule
    return (a + b) * c


#  calling the method of the function we created to get the resut
print(calculate_expression(a, b, c))

# Question no. 13:

# initializing a str variable

range_text = "Hello"
# This gives an error because , there is no index no.5 in text "Hello", its [0],[1],[2],[3],[4], ie H,e,l,l,o
# print(range_text[5])

# Question no. 14:

# intiatializing two variables
s1, s2 = "test", "test"

# Both checks if s1 quals to s2 and returns a bool value.
print(s1 == s2)
print(s1 is s2)

# Question no. 15:

# initializing a complex number:

z = 3 + 4j

# printing the real (.real) part and imaginary part (.imag) and confirming the type
print(z.real)
print(z.imag)
print(type(z))

# Question n0.16:

# initialzing two float variables
f1, f2 = 0.1 + 0.2, 0.3

# cheching if f1 equals to f2
print(f1 == f2)

# printing f1 and f2

print(f1)
print(f2)  # since both values are differnt, f1 != f2
