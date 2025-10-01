# student_record.py

def add_student(name, age, major):
    with open("records.txt", "a") as file:
        file.write(f"{name},{age},{major}\n")

def view_students():
    try:
        with open("records.txt", "r") as file:
            students = file.readlines()
            for student in students:
                name, age, major = student.strip().split(",")
                print(f"Name: {name}, Age: {age}, Major: {major}")
    except FileNotFoundError:
        print("No student records found.")

# Add students
add_student("Alice", 20, "Computer Science")
add_student("Bob", 21, "Mechanical Engineering")
add_student("Charlie", 19, "Electrical Engineering")
add_student("David", 22, "Business Administration")
add_student("Eve", 20, "Mathematics")

# View students
print("Student Records:")
view_students()
