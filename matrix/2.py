import sympy as sp

# Define lambda as a symbol
lambda_ = sp.symbols('lambda')

# Define coefficient matrix A and constants vector B
A = sp.Matrix([[3, 2, 4],
               [1, 1, 1],
               [5, 4, 6]])

B = sp.Matrix([3, lambda_, 15])

# Create augmented matrix
augmented = A.row_join(B)

# Perform row reduction
rref, pivot_columns = augmented.rref()

# Display the reduced row-echelon form
print("RREF of augmented matrix:")
print(rref)

# Find the condition for consistency
# The last row should be all zeros in the coefficient part and zero in the augmented part
# If not, it's inconsistent
# So, set the augmented part of the last row to zero and solve for lambda

# Extract the last row
last_row = rref[-1, :]

# The condition is that the augmented part (last element) is zero
condition = sp.Eq(last_row[-1], 0)

# Solve for lambda
lambda_solution = sp.solve(condition, lambda_)

print("Value of lambda for consistency:", lambda_solution)

# import numpy as np

# # Function to solve the system for a given lambda
# def solve_system(lambda_val):
#     # Coefficient matrix (A) and augmented column vector (B)
#     A = np.array([[3, 2, 4],
#                   [1, 1, 1],
#                   [5, 4, 6]])
#     B = np.array([3, lambda_val, 15])
    
#     # Augmented matrix for consistency check
#     augmented_matrix = np.column_stack((A, B))
    
#     # Rank of coefficient matrix and augmented matrix
#     rank_A = np.linalg.matrix_rank(A)
#     rank_augmented = np.linalg.matrix_rank(augmented_matrix)
    
#     # Check for consistency
#     if rank_A == rank_augmented:
#         print(f"For λ = {lambda_val}, the system is consistent.")
        
#         # Since rank_A < len(A), there are infinitely many solutions
#         print("The system has infinitely many solutions.")
#         print("General solution in terms of a free parameter t:")
#         print("x = -9 - 2t")
#         print("y = 15 + t")
#         print("z = t")
#     else:
#         print(f"For λ = {lambda_val}, the system is inconsistent.")

# # Value of lambda that makes the system consistent
# lambda_value = 6
# solve_system(lambda_value)