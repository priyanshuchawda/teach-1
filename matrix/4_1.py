import sympy as sp

# Define the matrix A
A = sp.Matrix([
    [4, -5, 1],
    [3, 1, -2],
    [1, 4, 1]
])

# Define the vector Y
Y = sp.Matrix([1, 2, -1])

# Solve for X
X = A.solve(Y)  #AX=Y , finds X

# Print the result
print("The solution (x1, x2, x3) is:", X)