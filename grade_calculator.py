# grade_calculator.py

def calculate_average(grades):
    return sum(grades) / len(grades)

def assign_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def student_report(name, *grades):
    average = calculate_average(grades)
    grade = assign_grade(average)
    print(f"Student Name: {name}")
    print(f"Grades: {grades}")
    print(f"Average Score: {average:.2f}")
    print(f"Final Grade: {grade}")
    print()

# Collect grades for students
student_report("Alice", 95, 90, 85)
student_report("Bob", 70, 75, 80)
student_report("Charlie", 60, 65, 70)

# Commit to Git:
# git add grade_calculator.py
# git commit -m "Day 20: Advanced functions – student grade calculator"
# git push
