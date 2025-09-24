# Ask the user for their name and score
name = input("Enter the student's name: ")
score = int(input("Enter the student's score (0-100): "))

# Use if-elif-else to assign a grade based on the score
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

# Print the final result
print("---")
print(f"Student: {name}")
print(f"Score: {score}")
print(f"Grade: {grade}")
