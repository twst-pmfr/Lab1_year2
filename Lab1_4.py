import numpy as np

A = np.random.randint(1, 11, size=(5, 5))
B = np.random.randint(1, 11, size=(5, 5))

elementwise_product = A * B

matrix_product = np.dot(A, B)

det_A = np.linalg.det(A)

transposed_B = B.T

if abs(det_A) > 1e-10:
    inverse_A = np.linalg.inv(A)
else:
    print("Матрица A вырожденная, обратная матрица не существует.")

C = np.sum(A, axis=1)[:, None]
if abs(det_A) > 1e-10:
    solution_x = np.linalg.solve(A, C)
else:
    print("Система уравнений не решается, поскольку матрица A вырожденная.")

print("Матрица A:\n", A)
print("Матрица B:\n", B)
print("Поэлементное произведение матриц A и B:\n", elementwise_product)
print("Матричное произведение матриц A и B:\n", matrix_product)
print("Определитель матрицы A:", det_A)
print("Транспонированная матрица B:\n", transposed_B)

if abs(det_A) > 1e-10:
    print("Обратная матрица для A:\n", inverse_A)
    print("Решение системы уравнений Ax = C:\n", solution_x)
else:
    print("Матрица A вырожденная, система уравнений неразрешима.")