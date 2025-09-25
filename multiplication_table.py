# multiplication_table.py

# Get input from the user for a single number's multiplication table
try:
    number = int(input("Enter a number to see its multiplication table: "))

    print(f"\n--- Multiplication Table for {number} ---")

    # Use a for loop to print the multiplication table from 1 to 10
    for i in range(1, 11):
        product = number * i
        print(f"{number} x {i} = {product}")

except ValueError:
    print("Invalid input. Please enter a valid integer.")

# --- Bonus: Nested loops for tables 1-5 ---

print("\n--- Multiplication Tables for numbers 1 to 5 ---")

# Outer loop for numbers 1 to 5
for num in range(1, 6):
    print(f"\nMultiplication Table for {num}:")

    # Inner loop for the multiplication from 1 to 10
    for i in range(1, 11):
        product = num * i
        print(f"{num} x {i} = {product}")
