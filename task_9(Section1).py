import numpy as np
# Section no.1 : Array Creation and Basic Operations
# Answer no.1
print(f"The numpy version is:{np.__version__}")
print("----------------------------------------------------------------------")

# Answer no.2
array1 = np.array(range(1, 11))
print(f"The array of numbers from 1 to 10: {array1}")
print("----------------------------------------------------------------------")

# Answer no.3
array2 = np.zeros(shape=10, dtype=int)
print(f"The array of zeros: {array2}")
print("----------------------------------------------------------------------")

# Answer no.4
array3 = np.ones(shape=(3, 3), dtype=int)
print(f"The array of ones with shape (3,3): {array3}")
print("----------------------------------------------------------------------")

# Answer no.5
array4 = np.eye(N=5, dtype=int)
print(f"The identity matrix of size 5x5: {array4}")
print("----------------------------------------------------------------------")

# Answer no.6
array5 = np.array([i for i in range(2, 51) if i % 2 == 0], dtype=int)  # or
# array5 = np.arange(2, 51, 2)
print(array5)
print(f"The array of even numbers from 2 to 50:{array5}")
print("----------------------------------------------------------------------")

# Answer no.7
array6 = np.array([i for i in range(1, 100) if i % 2 != 0], dtype=int)  # or
# array5 = np.arange(1, 100, 2)
print(f"The array of odd numbers from 1 to 99:{array6}")
print("----------------------------------------------------------------------")

# Answer no.8
array7 = np.arange(10, 101, 5)
print(f"The array from 10 to 100 with step size of 5:{array7}")
print("----------------------------------------------------------------------")

# Answer no.9
python_list = list(range(1, 21))
array9 = np.array(python_list)
print(f"The numpy array from a python list:{array9}")
print("----------------------------------------------------------------------")

# Answer no.10
my_tuple = tuple(range(1, 16))
print(my_tuple)
array10 = np.array(my_tuple)
print(array10)
print("----------------------------------------------------------------------")

# Answer no.11
array11 = np.array(range(1, 31))
print(f"The shape of an array is:{array11.shape}")
print("----------------------------------------------------------------------")

# Answer no. 12
array12 = np.arange(1, 11)
print(f"The number of dimension in the array: {array12.ndim}")
print("----------------------------------------------------------------------")

# Answer no. 13
array13 = np.array(["Lisa", "Sabrina", "Laufey"])
print(f"The datatype of the array is: {array13.dtype}")
print("----------------------------------------------------------------------")

# Answer. no. 14
array14 = np.random.rand(10)
print(f"The random array of size 10 : {array14}")
print("----------------------------------------------------------------------")

# Answer no. 15
array15 = np.random.randint(1, 100, size=10)
print(f"The random integers between 1 and 100:{array15}")
print("----------------------------------------------------------------------")

# Answer no.16
array16_ = np.random.randint(1, 100, size=12)
array16 = array16_.reshape(3, 4)
print(f"The reshaped array of size 12 to (3,4):{array16}")
print("----------------------------------------------------------------------")

# Answer no.17
array17_ = np.random.randint(1, 20, size=(3, 3))
# array17 = array17_.reshape(9)
array17 = array17_.flatten()
print(f"The flattened 3x3 matrix into 1D array:{array17}")
print("----------------------------------------------------------------------")

# Answer no.18
array18 = np.full(fill_value=7, shape=(4, 4))
print(f"The 4x4 matrix of value filled with 7: {array18}")
print("----------------------------------------------------------------------")

# Answer no.19
array19 = np.full((3, 3), 4)
print(f"The number of elements in the array : {array19.size}")
print("----------------------------------------------------------------------")

# Answer no. 20
array20 = np.diag([1, 2, 3, 4])
print(f"The diagonal matrix with values[1,2,3,4] : {array20}")
print("----------------------------------------------------------------------")

# Answer no. 21
array21_ = np.random.rand(7)
array21 = array21_.astype(int)
print(f"The converted int array from float :{array21}")
print("----------------------------------------------------------------------")

# Answer no. 22
array22 = np.linspace(0, 1, 5)
print(f"The values between 0 and 1 :{array22}")
print("----------------------------------------------------------------------")

# Answer no.23
array23 = np.random.randint(1, 20, 5)
print(array23)
print(f"The reversed array:{array23[::-1]}")
print("----------------------------------------------------------------------")

# Answer no.24
array24_ = np.random.randint(1, 30, 5)
print(array24_)
array24 = np.sort(array24_)
print(f"The array sorted in ascending order:{array24}")
print("----------------------------------------------------------------------")

# Answer no.25
array25 = np.random.randint(1, 50, 5)
print(array25)
max_number = array25.max()
min_number = array25.min()
print(f"The maximum number from the array :{max_number}")
print(f"The minimum number from the array :{min_number}")
print("----------------------------------------------------------------------")

# Answer no.26
array26 = np.random.randint(1, 60, 5)
index_max = np.argmax(array26)
print(array26)
print(f"The index of the maximum value is:{index_max}")
print("----------------------------------------------------------------------")

# Answer no.27
array27 = np.random.randint(1, 60, 5)
index_min = np.argmin(array27)
print(array27)
print(f"The index of the maximum value is:{index_min}")
print("----------------------------------------------------------------------")

# Answer no.28
array28 = np.random.randint(1, 60, (2, 3))
print(array28)
print(f"The transpose of the matrix is: {np.transpose(array28)}")
print("----------------------------------------------------------------------")

# Answer no.29
array29_1 = np.array(["Lisa", "Sabrina"])
array29_2 = np.array(["Laufey", "Beabadoobe"])
array29 = np.concatenate((array29_1, array29_2))
print(f"The concatenated array :{array29}")
print("----------------------------------------------------------------------")

# Answer no.30
array30_ = np.array(["Lisa", "Sabrina", "Adele", "Laufey",
                    "Beabadoobe", "Lana del ray"])
array30 = np.split(array30_, 3)
print(array30)
