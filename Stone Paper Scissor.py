import random

while True:
    user_cases = input("Enter a choice (stone, paper, scissors): ")
    possible_cases = ["stone", "paper", "scissors"]
    computer_cases = random.choice(possible_cases)
    print(f"\nYou chose {user_cases}, computer chose {computer_cases}.\n")

    if user_cases == computer_cases:
        print(f"Both players selected {user_cases}. It's a tie!")
    elif user_cases == "stone":
        if computer_cases == "scissors":
            print("stone breaks scissors! You win!")
        else:
            print("Paper wraps stone! You lose.")
    elif user_cases == "paper":
        if computer_cases == "stone":
            print("Paper wraps stone! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_cases == "scissors":
        if computer_cases == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("stone breaks scissors! You lose.")

    play_again = input("Play again? (yes/no): ")
    if play_again.lower() != "yes":
        break