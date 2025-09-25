# student_marks.py

# Store student names and their marks in two lists
students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
marks = [85, 92, 78, 88, 95]

# Calculate the average marks
total_marks = sum(marks)
average_marks = total_marks / len(marks)

# Assign grades and print the summary table
print("Student Marks Analyzer\n")

for i in range(len(students)):
    student_name = students[i]
    student_mark = marks[i]
    
    # Assign grades using if-elif-else
    if student_mark >= 90:
        grade = 'A'
    elif student_mark >= 80:
        grade = 'B'
    elif student_mark >= 70:
        grade = 'C'
    elif student_mark >= 60:
        grade = 'D'
    else:
        grade = 'F'
        
    print(f"{student_name}: {student_mark} - Grade {grade}")

print(f"\nAverage marks: {average_marks:.1f}")
