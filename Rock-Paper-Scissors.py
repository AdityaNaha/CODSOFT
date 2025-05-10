# ADITYANAHA_CodSoft_Rock-Paper-Scissors Game

import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def decide_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

def print_scores(user_score, computer_score):
    print(f"\n Scores:")
    print(f"You: {user_score}")
    print(f"Computer: {computer_score}")

def play_game():
    user_score = 0
    computer_score = 0
    print("Welcome to Rock-Paper-Scissors!")
    print("Choose rock, paper, or scissors.\n")

    while True:
        user_choice = input("👉 Your choice: ").lower()
        if user_choice not in ["rock", "paper", "scissors"]:
            print("❌ Invalid choice. Please choose rock, paper, or scissors.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        result = decide_winner(user_choice, computer_choice)
        print(f"{result}")

        if "You win" in result:
            user_score += 1
        elif "Computer wins" in result:
            computer_score += 1

        print_scores(user_score, computer_score)
        play_again = input("\nPlay again? (y/n): ").lower()

        if play_again != 'y':
            print("\nThanks for playing! Final scores:")
            print_scores(user_score, computer_score)

            break

play_game()