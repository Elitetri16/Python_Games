import random

while True:
    user_cases = input("Enter a choice (lady, hunter, tiger): ")
    possible_cases = ["lady", "hunter", "tiger"]
    computer_cases = random.choice(possible_cases)
    print(f"\nYou chose {user_cases}, computer chose {computer_cases}.\n")

    if user_cases == computer_cases:
        print(f"Both players selected {user_cases}. It's a tie!")
    elif user_cases == "lady":
        if computer_cases == "tiger":
            print("tiger eats lady! You lose.")
        else:
            print("lady dismisses hunter! You win!")
    elif user_cases == "hunter":
        if computer_cases == "lady":
            print("lady dismisses hunter! You lose.")
        else:
            print("Hunter hunts tiger! You win!")
    elif user_cases == "tiger":
        if computer_cases == "hunter":
            print("Hunter hunts tiger! You lose.")
        else:
            print("tiger eats lady! You win!")

    play_again = input("Play again? (yes/no): ")
    if play_again.lower() != "yes":
        break