from sympy import Matrix

aug_matrix = Matrix([[2, -3, 5, 1],
                     [3,  1, -1, 2],
                     [1,  4, -6, 1]])


rref_matrix, pivots = aug_matrix.rref()
print(rref_matrix)
