# Count Vowels and Consonants in a String
string = 'Hello World'
vowels = consonants = 0
for char in string:
    if char.isalpha():
        if char in 'aeiouAEIOU':
            vowels += 1
        else:
            consonants += 1
print('Vowels:', vowels, 'Consonants:', consonants)