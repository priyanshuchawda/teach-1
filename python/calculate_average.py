try:
    with open('students.txt', 'r') as infile:
        lines = infile.readlines()

    total_marks = 0
    student_count = 0
    for line in lines:
        try:
            parts = line.strip().split(',')
            if len(parts) == 3:
                name = parts[0].strip('" ')  
                age = int(parts[1].strip())
                marks = float(parts[2].strip())
                total_marks += marks
                student_count += 1
        except (ValueError, IndexError) as e:
            print(f"Skipping invalid line: {line.strip()}")

    # Calculate and write average
    average_marks = total_marks / student_count if student_count > 0 else 0
    
    with open('average_marks.txt', 'w') as outfile:
        outfile.write(f'Average Marks: {average_marks:.2f}\n')

    print(f"Average marks ({average_marks:.2f}) have been written to average_marks.txt")

except FileNotFoundError:
    print("Error: students.txt file not found")
except Exception as e:
    print(f"An error occurred: {str(e)}") 