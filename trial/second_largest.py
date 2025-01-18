# Find the Second Largest Number in a List
numbers = [1, 2, 3, 4, 5]
unique_numbers = list(set(numbers))
unique_numbers.sort()
second_largest = unique_numbers[-2]
print('Second largest number is:', second_largest)