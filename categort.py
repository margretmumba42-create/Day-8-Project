# age_category.py

def age_category():
    # Ask user for name and age
    name = input("Enter your name: ")
    while True:
        try:
            age = int(input("Enter your age: "))
            if age >= 0:
                break
            else:
                print("Please enter a non-negative age.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Assign age category
    if age <= 12:
        category = "Child"
    elif age <= 19:
        category = "Teen"
    elif age <= 59:
        category = "Adult"
    else:
        category = "Senior"

    # Print the result
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Category: {category}")

if __name__ == "__main__":
    age_category()
