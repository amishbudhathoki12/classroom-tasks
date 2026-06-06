import numpy as np
# Section 2:
# Basic operations

# Answer no.31
array1 = np.random.randint(1, 50, 5)
print(array1)
array2 = np.random.randint(1, 50, 5)
print(array2)
sum_arr = np.add(array1, array2)
print(f"The sum of two arrays:{sum_arr}")
print("-----------------------------------------------------")

# Answer no.32
array3 = np.random.randint(1, 50, 5)
print(array3)
array4 = np.random.randint(1, 50, 5)
print(array4)
diff_arr = np.diff(array3 - array4)
print(f"The difference of two arrays:{diff_arr}")
print("-----------------------------------------------------")

# Answer no.33
array9 = np.random.randint(1, 50, 5)
print(array9)
array10 = np.random.randint(1, 50, 5)
print(array10)
multiplication_arr = np.multiply(array9, array10)
print(f"The multiplication of two arrays:{multiplication_arr}")
print("-----------------------------------------------------")

# Answer no.34
array5 = np.random.randint(1, 50, 5)
print(array5)
array6 = np.random.randint(1, 50, 5)
print(array6)
division_arr = np.divide(array5, array6)
print(f"The division of two arrays:{division_arr}")
print("-----------------------------------------------------")

# Answer no.35
array7 = np.random.randint(1, 50, 5)
print(array7)
square_arr = np.square(array7)
print(f"The square of each element:{square_arr}")
print("-----------------------------------------------------")

# Answer no.36
array8 = np.random.randint(1, 50, 5)
print(array8)
cube_arr = np.power(array8, 3)
# # or
# cube_arr = np.array([i ** 3 for i in array8])
print(f"The cube of each element:{cube_arr}")
print("-----------------------------------------------------")

# Answer no. 37
array11 = np.random.randint(1, 50, 5)
print(array11)
sqrt_arr = np.sqrt(array11)
print(f"The square root values in the array: {sqrt_arr}")
print("-----------------------------------------------------")

# Answer no. 38
array12 = np.random.randint(1, 50, 5)
print(array12)
exp_arr = np.exp(array12)
print(f"The exponential values in the array: {exp_arr}")
print("-----------------------------------------------------")

# Answer no. 39
array13 = np.random.randint(1, 50, 5)
print(array13)
log_arr = np.log(array13)
print(f"The logarithm values in the array: {log_arr}")
print("-----------------------------------------------------")

# Answer no. 40
array12 = np.random.randint(1, 50, 5)
print(array12)
sum_arr = np.sum(array12)
print(f"The sum of all values in the array: {sum_arr}")
print("-----------------------------------------------------")

# Answer no. 41
array13 = np.random.randint(1, 50, 5)
print(array13)
mean_arr = np.mean(array13)
print(f"The mean of the array: {mean_arr}")
print("-----------------------------------------------------")

# Answer no.42
array14 = np.array([1, 2, 3, 4, 5])
print(array14)
median_arr = np.median(array14)
print(f"The median of the array: {median_arr}")
print("-----------------------------------------------------")

# Answer no.43
array15 = np.random.randint(1, 50, 5)
print(array15)
std_deviation_arr = np.std(array15)
print(f"The standard deviation of the array: {std_deviation_arr}")
print("-----------------------------------------------------")

# Answer no. 44
array16 = np.random.randint(1, 50, 5)
print(array16)
variance_arr = np.var(array16)
print(f"The variance of the array: {variance_arr}")
print("-----------------------------------------------------")

# Answer no. 45
array17 = np.random.randint(1, 50, 5)
print(array17)
cum_sum_arr = np.cumsum(array17)
print(f"The cumulative sum in the array: {cum_sum_arr}")
print("-----------------------------------------------------")

# Answer no. 46
array18 = np.random.randint(1, 50, 5)
print(array18)
cum_prod_arr = np.cumprod(array18)
print(f"The cumulative product in the array: {cum_prod_arr}")
print("-----------------------------------------------------")

# Answer no. 47
array19 = np.random.randint(1, 50, 5)
print(array19)
prod_arr = np.prod(array19)
print(f"The product of the array: {prod_arr}")
print("-----------------------------------------------------")

# Answer no. 48
array20 = np.random.rand(5)
print(array20)
rounded_arr = np.round(array20, 2)
print(f"The rounded value to 2 decimals: {rounded_arr}")
print("-----------------------------------------------------")

# Answer no. 49
array21 = np.array([-1, -2, -3, -4, -5])
print(array21)
absolute_neg_val = np.abs(array21)
print(f"The absolute values of negative numbers: {absolute_neg_val}")
print("-----------------------------------------------------")

# Answer no.50
array22 = np.array([-1, 2, -3, 4, -5])
print(array22)
# array22[array22 < 0] = 0
# print(array22)
# or
replaced_arr = np.where(array22 < 0, 0, array22)
print(f"The replaced negative values with zero: {replaced_arr}")
