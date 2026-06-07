import numpy as np
# Section 3
# Indexing and slicing

# Answer no.51
array1 = np.random.randint(1, 50, 6)
print(array1)
print(f"The first element of the array: {array1[0]}")
print("------------------------------------------------------------------")

# Answer no. 52
array2 = np.arange(1, 16, 2, dtype=int)
print(array2)
print(f"The last element of the array : {array2[-1]}")
print("------------------------------------------------------------------")

# Answer no. 53
array3 = np.array(["a", "b", "c", "d", "e", "f", "g"])
print(array3)
print(f"The first five element of the array: {array3[0:5]}")
print("------------------------------------------------------------------")

# Answer no. 54
array4 = np.arange(1, 11)
print(array4)
print(f"The last five elements of the array:{array4[-1:-6:-1]}")
print("------------------------------------------------------------------")

# Answer no. 55
array5 = np.random.randint(1, 50, 6)
print(array5)
print(f"The alternate elements of the array: {array5[::2]}")
print("------------------------------------------------------------------")

# Answer no. 56
array6 = np.array(["Lisa", "Sabrina", 6, False, 7.5])
print(array6)
print(f"The reversed array: {array6[::-1]}")
print("------------------------------------------------------------------")
print("------------------------------------------------------------------")

# Answer no. 57
array7 = np.random.randint(1, 60, (3, 4))
print(array7)
print(f"The second row in the matrix is:{array7[1, :]}")
print("------------------------------------------------------------------")

# Answer no. 58
array8 = np.random.randint(1, 60, (3, 4))
print(array8)
print(f"The second column in the matrix is:{array8[:, 1]}")
print("------------------------------------------------------------------")

# Answer no. 59
array9 = np.random.randint(1, 80, (5, 5))
print(array9)
print(f"The sub-matrix of a 5x5 : {array9[1:4, 1:4]}")
print("------------------------------------------------------------------")

# Answer no. 60
array10 = np.random.randint(1, 10, 4)
print(array10)
array10[2] = 100
print(f"The replaced third element of array :{array10}")
print("------------------------------------------------------------------")

# Answer no. 61
array11 = np.array([1, 2, 3, 4, 5])
print(array11)
replaced_array11 = np.where(array11 % 2 == 0, -1, array11)  # or
# replaced_array11 = np.array([
#     -1 if x % 2 == 0 else x
#     for x in array11
# ])
print(f"The replaced even numbers: {replaced_array11}")
print("------------------------------------------------------------------")

# Answer no. 62
array12 = np.random.randint(1, 100, 5)
print(array12)
# elm_msg = "No element greater than 50 in the array"
# greater_elm = np.array(
#     [i for i in array12 if i > 50])
# if greater_elm.size == 0:
#     print(elm_msg)
# else:
#     print(f"The elements greater than 50:{greater_elm}") #or
if np.any(array12 > 50):
    print("The elements greater than 50:", array12[array12 > 50])
else:
    print("No element greater than 50")

print("------------------------------------------------------------------")

# Answer no. 63
array13 = np.random.randint(1, 100, 5)
print(array13)
idx = np.where(array13 > 50)
print(f"The indices of the elements greater than 50: {idx}")

# Answer no. 64
array14 = np.array([6, 9, 5, 10])
print(array14)
result = array14[array14 % 3 == 0]

if result.size > 0:
    print("The elements divisible by 3 in the array:", result)
else:
    print("There are no elements divisible by 3 in the array")  # or
# if np.any(array14 % 3 == 0):
#     print(
#         f"The elements divisible by 3 in the array: {array14[array14 % 3 == 0]}")
# else:
#     print("There are no element divisible by 3 in the array")

# Answer no. 65
array15 = np.random.randint(1, 50, (4, 4))
print(array15)
diag_elm = np.diag(array15)
print(f"The diagonal elements from the matrix: {diag_elm}")
