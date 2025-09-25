import random

# Generate a random number between 1 and 50
secret_number = random.randint(1, 50)
attempts = 0

print("Welcome to the Guess the Number game!")
print("I'm thinking of a number between 1 and 50.")

# Start the game loop
while True:
    try:
        # Get the user's guess
        user_guess = int(input("Enter your guess: "))
        attempts += 1

        # Check the guess and provide hints
        if user_guess < secret_number:
            print("Too low! Try again.")
        elif user_guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} correctly.")
            print(f"It took you {attempts} attempts.")
            break # Exit the loop when the guess is correct
    except ValueError:
        print("Invalid input. Please enter a valid number.")
