# Question no.1:
print("Answer no.1:")


def greeting(name, message="Welcome"):
    print(f"Hello,{name}! {message}")


greeting("Lisa")

print("---------------------------------")


# Question no.2:
print("Answer no.2:")


def total(*args):
    print(f"The sum of the tuple is: {sum(args)}")


total(10, 20, 30)


print("---------------------------------")

# Question no.3:
print("Answer no.3:")


def display_info(**kwargs):
    for e in kwargs.items():
        print(e)


display_info(name="Lisa", age=25, city="kathmandu")

print("---------------------------------")

# Question no.4:
print("Answer no.4:")


def repeat_words(*args, times):
    repeated_word = args * times
    print(f"The repeated words are:{repeated_word}")


repeat_words("Hi", "Bye", times=3)


print("---------------------------------")

# Question no.5:
print("Answer no.5:")


def user_profile(name, age, *hobbies, **extra_info):
    print(f"Name: {name}, Age:{age}")
    print("No hobbies") if not hobbies else print(f"Hobbies:{hobbies}")
    print("No extra info") if not extra_info else print(extra_info)


user_profile("Lisa", 26, "Singing", "Dacning",
             "Playing Tennis", is_married=False, city="Seoul, Korea")
print("---------------------------------")
