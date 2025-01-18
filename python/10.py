with open('students.txt', 'r') as infile:
    lines = infile.readlines()

total_marks = 0
student_count = 0

for line in lines:
    parts = line.strip().split(',')
    if len(parts) == 3:
        name = parts[0].strip()
        age = int(parts[1].strip())
        marks = float(parts[2].strip())
        total_marks += marks
        student_count += 1

if student_count > 0:
    average_marks = total_marks / student_count
else:
    average_marks = 0

with open('average_marks.txt', 'w') as outfile:
    outfile.write(f'Average Marks: {average_marks:.2f}\n')

print("Average marks have been written to average_marks.txt")