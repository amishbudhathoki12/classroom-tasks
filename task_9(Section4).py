import numpy as np
# Section no.4
# Matrix Operations

# Answer no. 66
matrix1 = np.random.randint(1, 50, (3, 4))
print(f"Matrix1:{matrix1}")
matrix2 = np.random.randint(1, 50, (3, 4))
print(f"Matrix2: {matrix2}")
# sum_matrix = np.add(matrix1, matrix2) or
sum_matrix = matrix1 + matrix2
print(f"The sum of two matrices : {sum_matrix} ")
print("-----------------------------------------------------------------------")

# Answer no. 67
matrix3 = np.random.randint(1, 50, (3, 4))
print(f"Matrix1:{matrix3}")
matrix4 = np.random.randint(1, 50, (3, 4))
print(f"Matrix2: {matrix4}")
# diff_matrix = np.diff(matrix1, matrix2) or
diff_matrix = matrix1 - matrix2
print(f"The difference of two matrices : {diff_matrix} ")
print("-----------------------------------------------------------------------")

# Answer no. 68
matrix5 = np.random.randint(1, 50, (3, 4))
print(f"Matrix1:{matrix5}")
matrix6 = np.random.randint(1, 50, (3, 4))
print(f"Matrix2: {matrix6}")
# prod_matrix = np.multiply(matrix1, matrix2) or
prod_matrix = matrix1 * matrix2
print(f"The multiplication of two matrices : {prod_matrix} ")
print("-----------------------------------------------------------------------")


# Answer no. 69
matrix7 = np.random.randint(1, 50, (3, 3))
print(f"Matrix1: {matrix7}")
matrix8 = np.random.randint(1, 50, (3, 3))
print(f"Matrix2: {matrix8}")
prd_matrix = np.dot(matrix7, matrix8)
print(f"Matrix multiplication using dot: {prd_matrix}")
print("-----------------------------------------------------------------------")

# Answer no. 70
matrix9 = np.random.randint(1, 60, (4, 4))
print(matrix9)
transpose_matrix9 = np.transpose(matrix9)
print(f"The transpose of the matrix : {transpose_matrix9}")
print("-----------------------------------------------------------------------")

# Answer no.71
matrix10 = np.random.randint(1, 60, (2, 2))
matrix11 = np.random.randint(1, 60, (3, 3))
print(matrix10)
print(matrix11)
dtr_matrix10 = np.linalg.det(matrix10)
dtr_matrix11 = np.linalg.det(matrix11)
print(f"The determinant of 2x2 matrix:{int(dtr_matrix10)}")
print(f"The determinant of 3x3 matrix:{int(dtr_matrix11)}")
print("-----------------------------------------------------------------------")

# Answer no.72
matrix12 = np.random.randint(1, 50, (2, 2))
print(matrix12)
inv_matrix12 = np.linalg.inv(matrix12)
print(f"The inverse of the matrix: {inv_matrix12}")
print("-----------------------------------------------------------------------")

# Answer no.73
matrix13 = np.random.randint(1, 50, (3, 3))
print(matrix13)
eigvl_matrix13 = np.linalg.eigvals(matrix13)
print(f"The eigenvalues of a matrix: {eigvl_matrix13}")
print("-----------------------------------------------------------------------")

# Answer no.74
matrix14 = np.random.randint(1, 50, (3, 3))
print(matrix14)
eigenvalues, eigenvectors = np.linalg.eig(matrix14)
print(f"The eigenvectors of a matrix: {eigenvectors}")
print("-----------------------------------------------------------------------")

# Answer no.75
matrix15 = np.array([[1, 2, 3], [2, 4, 6], [1, 1, 1]])
print(matrix15)
mat_rank = np.linalg.matrix_rank(matrix15)
print(f"The matrix rank is: {mat_rank}")
print("-----------------------------------------------------------------------")

# Answer no.76
matrix16 = np.random.randint(1, 50, (4, 4))
print(matrix16)
row_sum = np.sum(matrix16, axis=1)
print(f"The row sum:{row_sum}")
print("-----------------------------------------------------------------------")

# Answer no.77
matrix17 = np.random.randint(1, 50, (4, 4))
print(matrix17)
column_sum = np.sum(matrix17, axis=0)
print(f"The column sum:{column_sum}")
print("-----------------------------------------------------------------------")

# Answer no.78
matrix18 = np.random.randint(1, 60, (3, 3))
print(matrix18)
row_wise_max_val = np.max(matrix18, axis=1)
print(f"The row-wise maximum values: {row_wise_max_val} ")
print("-----------------------------------------------------------------------")

# Answer no.79
matrix20 = np.random.randint(1, 60, (3, 3))
print(matrix20)
col_min_val = np.min(matrix20, axis=0)
print(f"The column-wise minimum values: {col_min_val} ")
print("-----------------------------------------------------------------------")

# Answer no.80
n = 5
matrix19 = np.arange(1, n+1) * np.arange(1, n+1).reshape(n, 1)  # or
# matrix19 = np.array([
#     [i * j for j in range(1, 6)]
#     for i in range(1, 6)
# ])

# print(matrix19)
print(f"The 5x5 multiplication tabele: {matrix19}")
