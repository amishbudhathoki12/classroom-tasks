# Question no. 1
print("Answer no.1:")
num = 10
while num <= 30:
    print(num)
    num += 1
print("---------------------------------")

# Question no.2
print("Answer no.2:")
odd_count = 1
while odd_count <= 20:
    print(odd_count)
    odd_count += 2
print("---------------------------------")

# Question no.3
print("Answer no.3:")
word_count = 0
while word_count < 5:
    print("Hello")
    word_count += 1
print("---------------------------------")

# Question no. 4
print("Answer no.4:")
n4 = 12345
reverse_num = 0

while n4 > 0:
    digit = n4 % 10
    reverse_num = reverse_num * 10 + digit
    n4 = n4 // 10

print(reverse_num)

print("---------------------------------")

# Question no. 5
print("Answer no.5")
n5 = 3
while n5 <= 30:
    print(n5)
    n5 += 3
print("---------------------------------")

# Question no.6
print("Answer no.6")
s1 = int(input("Enter a number: "))

while s1 <= 0:
    s1 = int(input("Please enter a positive number: "))

print("The number you entered is positive.")
print("---------------------------------")

# Question no.7
print("Answer no.7")
n7 = 10
while n7 <= 20:
    print(n7)
    n7 += 2
print("---------------------------------")

# Question no.8
print("Answer no.8")
s2 = int(input("Enter a number from 1 to 20: "))
secret_number = 7
while s2 != secret_number:
    s2 = int(input("Try a number again from 1 to 20: "))
print("CONGRATULATION! YOU FOUND THE SECRET NUMBER 7")
print("---------------------------------")

# Question no.9
print("Answer no.9")
def add(a, b): print(f"The sum is: {a + b}")


add(a=3, b=5)
print("---------------------------------")

# Question no.10
print("Answer no.10")


def add(x, y): print(f"The product is: {x * y}")


add(x=3, y=5)
print("---------------------------------")

# Question no.11
print("Answer no.11")


def check_even_odd(
    num): print(f"{num} is even") if num % 2 == 0 else print(f"{num} is odd")


check_even_odd(6)
print("---------------------------------")
