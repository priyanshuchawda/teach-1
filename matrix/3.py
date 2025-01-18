import sympy as sp

# Define variables
x, y, z, lamb = sp.symbols('x y z lambda')

# Define the equations
eq1 = sp.Eq(3*x + 2*y + 4*z, 3)
eq2 = sp.Eq(x + y + z, lamb)
eq3 = sp.Eq(5*x + 4*y + 6*z, 15)

# Create a list of equations
equations = [eq1, eq2, eq3]

# Create a list of variables
variables = [x, y, z]

# Solve the system for the given lambda
solution = sp.solve(equations, variables, dict=True)

# Check if there are solutions for lambda
if solution:
    # Extract the condition for lambda
    lambda_condition = [sol[lamb] for sol in solution if lamb in sol]
    if lambda_condition:
        lambda_value = lambda_condition[0]
    else:
        # Solve for lambda that makes the system consistent
        # Find the augmented matrix and compute ranks
        A = sp.Matrix([
            [3, 2, 4],
            [1, 1, 1],
            [5, 4, 6]
        ])
        B = sp.Matrix([3, lamb, 15])
        augmented = A.row_join(B)
        
        # Compute ranks
        rank_A = A.rank()
        rank_aug = augmented.rank()
        
        # Find lambda where rank_A == rank_aug
        consistency_condition = sp.Eq(rank_A, rank_aug)
        lambda_value = sp.solve(consistency_condition, lamb)
        lambda_value = lambda_value[0]  # Extract the value
else:
    # Find lambda that makes the system consistent
    A = sp.Matrix([
        [3, 2, 4],
        [1, 1, 1],
        [5, 4, 6]
    ])
    B = sp.Matrix([3, sp.symbols('lambda'), 15])
    augmented = A.row_join(B)
    
    # Compute ranks
    rank_A = A.rank()
    rank_aug = augmented.rank()
    
    # Solve for lambda where rank_A == rank_aug
    lambda_value = sp.solve(sp.Eq(rank_A, rank_aug), sp.symbols('lambda'))
    lambda_value = lambda_value[0]  # Extract the value

# Substitute lambda back into the system and solve
equations_consistent = [
    sp.Eq(3*x + 2*y + 4*z, 3),
    sp.Eq(x + y + z, lambda_value),
    sp.Eq(5*x + 4*y + 6*z, 15)
]

# Solve the consistent system
solutions = sp.solve(equations_consistent, (x, y, z), dict=True)

# Express solutions in terms of a free parameter z
# Since z is a free variable, set z = t
t = sp.symbols('t')
general_solution = {
    x: solutions[0][x].subs(z, t),
    y: solutions[0][y].subs(z, t),
    z: t
}

# Display the results
print(f"Value of lambda for consistency: {lambda_value}")
print(f"General solution:")
print(f"x = {general_solution[x]}")
print(f"y = {general_solution[y]}")
print(f"z = {general_solution[z]}")