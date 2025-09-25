# grade_calculator.py

def calculate_grade(mark):
    """
    Calculates the letter grade based on a given mark.

    Args:
        mark (int or float): The numerical mark.

    Returns:
        str: The corresponding letter grade (A, B, C, D, E, or F).
    """
    if 90 <= mark <= 100:
        return "A"
    elif 80 <= mark < 90:
        return "B"
    elif 70 <= mark < 80:
        return "C"
    elif 60 <= mark < 70:
        return "D"
    elif 50 <= mark < 60:
        return "E"
    else:
        return "F"

# Store student names and marks in parallel lists
students = ["Alice", "Bob", "Charlie", "David", "Eve"]
marks = [95, 82, 67, 74, 89]

# Use a for loop to iterate through the students and print their grades
for i in range(len(students)):
    student_name = students[i]
    student_mark = marks[i]
    grade = calculate_grade(student_mark)
    print(f"{student_name}: {student_mark} - Grade {grade}")
