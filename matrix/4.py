import numpy as np

# Define the matrix A
A = np.array([
    [4, -5, 1],
    [3,  1, -2],
    [1,  4,  1]
])

# Define the vector Y
Y = np.array([1, 2, -1])

# Solve for X
X = np.linalg.solve(A, Y)

# Print the result
print("The solution (x1, x2, x3) is:", X)
