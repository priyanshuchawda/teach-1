# Compound Interest Calculation
principal = 1000  # Principal amount
rate = 5  # Interest rate

time = 2  # Time in years
amount = principal * (1 + rate / 100) ** time
compound_interest = amount - principal
print('Compound Interest:', compound_interest)
