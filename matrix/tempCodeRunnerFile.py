import numpy as np

# Coefficient matrix (A) and right-hand side vector (B)
def solve_equations(lambda_val):
    A = np.array([[3, 2, 4],
                  [1, 1, 1],
                  [5, 4, 6]])
    
    B = np.array([3, lambda_val, 15])
    
    try:
        # Check determinant of the coefficient matrix
        rank_A = np.linalg.matrix_rank(A)
        augmented_matrix = np.column_stack((A, B))
        rank_augmented = np.linalg.matrix_rank(augmented_matrix)
    except ValueError:
        print("Error: The matrix is not invertible.")
        return None
    
    if rank_A == rank_augmented:
        x = np.linalg.solve(augmented_matrix, B)
        return x
    else:
        print("Error: The matrix is not invertible.")
