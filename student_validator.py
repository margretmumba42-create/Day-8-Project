# student_validator.py

def get_student_name():
    while True:
        name = input("Enter student name: ")
        if name.strip():
            return name
        print("Name cannot be empty. Please try again.")

def get_student_age():
    while True:
        try:
            age = int(input("Enter student age: "))
            if age > 0:
                return age
            print("Age must be a positive integer. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid age.")

# Collect student details
students = []
for i in range(3):
    print(f"\nEnter details for Student {i+1}:")
    name = get_student_name()
    age = get_student_age()
    students.append({"name": name, "age": age})

# Display student records
print("\nStudent Records:")
for i, student in enumerate(students, start=1):
    print(f"Student {i}: Name = {student['name']}, Age = {student['age']}")
