# student_bio.py

# List of students
students = [
    {'name': 'Alice', 'age': 20, 'major': 'Computer Science'},
    {'name': 'Bob', 'age': 21, 'major': 'Mechanical Engineering'},
    {'name': 'Charlie', 'age': 19, 'major': 'Electrical Engineering'},
    {'name': 'David', 'age': 22, 'major': 'Business Administration'},
    {'name': 'Eve', 'age': 20, 'major': 'Mathematics'}
]

# Print student bios
for student in students:
    print(f"Student Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Major: {student['major']}")
    print()  # Empty line for better formatting

# Commit to Git:
# git add student_bio.py
# git commit -m "Day 17: Python strings & student bio formatter"
# git push
