# Section 1

# Question no.1

# initializing a list and prinitng it
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(my_list)

# Question no.2

# initializing a list of strings called fav_fruits and printing it
fav_fruits = ["Mango", "Kiwi", "Cranberry", "Dragonfruit"]
print(fav_fruits)

# Question no.3

# initializing a list of numbers
list_num = [10, 20, 30, 40, 50]
print(list_num)

# printing the first and last number with positive indexing
pos_ind_first_num = list_num[0]
print(pos_ind_first_num)
pos_ind_last_num = list_num[4]
print(pos_ind_last_num)

# Question no. 4

# initializing a list of female singer/songwriter
female_singer_list = ["Lisa", "Sabrina", "Adele", "Laufey", "Beabadoobe"]
print(female_singer_list)

# print the length of the list
singer_list_length = len(female_singer_list)
print(singer_list_length)

# Question no.5

# initializng an empty list
empty_list = []
print(empty_list)
# appending number 1 2 and 3 to the list
empty_list.append(1)
empty_list.append(2)
empty_list.append(3)
print(empty_list)

# Question no.6

# initializing a list of number
num_list = [1, 3, 4]
print(num_list)

# inserting num 2 at index 1
num_list.insert(1, 2)
print(num_list)

# Question no. 7

# initializing a list of numbers
nums_list = [1, 2, 3, 4, 5]
print(nums_list)

# removing num 3 from the list
nums_list.remove(3)
print(nums_list)

# Question no.8

#  initializing a list of number
list_nums = [10, 20, 30, 40]
print(list_nums)

# popping an element from the list
list_nums.pop()
print(list_nums)

# Question no.9

# initializing a list of number
lists_num = [0, 1, 2, 3, 4, 5]
print(lists_num)

# printing sliced list that contains elements  from index 2 - 4
sliced_list = lists_num[2:5]
print(sliced_list)

# Question no. 10

# initializing two lists

list_1, list_2 = [1, 2, 3], [4, 5, 6]
print(list_1)
print(list_2)

# concatenating list_1 and list_2
list_1.extend(list_2)  # or we can do list1 + list2 , list1 += list2
print(list_1)

# Question no.11

# initializing a list

l = [1, 2]
print(l)

# repating the list 3 times

repeated_list = l * 3
print(repeated_list)


# Question no.12

# initializing a list of num
l1 = [7, 5, 6]
print(f"Original list: {l1}")

# copying the list l1
copied_list = l1.copy()
print(f"Copied list: {copied_list}")
print(f"Original list: {l1}")

# Question no. 13

# initializing a list of num
l2 = [1, 2, 3, 4, 5]
print(l2)

# clearing the list
l2.clear()
print(l2)

# Section 2

# Question no. 1

# initializing a tuple of num and printing it
my_tuple = (1, 2, 3)
print(my_tuple)

# Question no.2

# initializing a tuple of 3 different colors and printing it
color_tuple = ("Red", "Orange", "Navy")
print(color_tuple)

# Question no.3

# initialiing a tuple of nums
t1 = (10, 20, 30, 40)
print(t1)

# printing the second element in tuple
ind_tuple = t1[1]
print(ind_tuple)

# Question no.4

# initializing a tuple of nums
t2 = (0, 1, 2, 3, 4)
print(t2)

# printing the sliced tuple from index 2 to 4
sliced_t2 = t2[2:5]
print(sliced_t2)

# Question no.5

# initializing two tuples
t5 = (1, 2, 3)
t6 = (4, 5, 6)

# concateneted two tuples
t5 += t6
print(f"Extended tuple: {t5}")

# Question no.6

# initializing a tuple of strs
t3 = ("Lisa", 25, "New York")
print(t3)

# putting them in a variable each and printing them
name = t3[0]
age = t3[1]
address = t3[2]

print(name)
print(age)
print(address)

# Question no.7

# initializing a list of nums
l4 = [1, 2, 3, 4]
print(l4)

# converting the list into tuple
list_to_tuple = tuple(l4)
print(f"The converted list: {list_to_tuple}")

# Question no.8

# initializing a tuple of nums
t4 = (1, 2, 2, 3, 2)
print(t4)

# counting the repeated number of 2
count_num_tuples = t4.count(2)
print(count_num_tuples)

# Question no.9

# initializing a tuple of nums
t7 = (10, 20, 30, 40)

# finding the index of element 30
print_index = t7.index(30)
print(print_index)
