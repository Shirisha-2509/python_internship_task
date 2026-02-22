import numpy as np

print("Matrix Operations Tool")

rows = int(input("Rows: "))
cols = int(input("Columns: "))

A = np.array([[int(input()) for _ in range(cols)] for _ in range(rows)])
B = np.array([[int(input()) for _ in range(cols)] for _ in range(rows)])

print("Matrix A:\n", A)
print("Matrix B:\n", B)

print("Addition:\n", A + B)
print("Subtraction:\n", A - B)
print("Multiplication:\n", np.dot(A, B.T))
print("Transpose A:\n", A.T)

if rows == cols:
    print("Determinant:", np.linalg.det(A))
