# Check if a Year is a Leap Year
year = 2024
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, 'is a leap year.')
else:
    print(year, 'is not a leap year.')