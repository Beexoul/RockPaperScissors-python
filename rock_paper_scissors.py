import random

def play_game():
    print("Welcome to Rock-Paper-Scissors!")

    choices = ['rock', 'paper', 'scissors']

    while True:
        player_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

        if player_choice not in choices:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = random.choice(choices)

        print("You chose:", player_choice)
        print("Computer chose:", computer_choice)

        if player_choice == computer_choice:
            print("It's a tie!")
        elif (
            (player_choice == 'rock' and computer_choice == 'scissors') or
            (player_choice == 'paper' and computer_choice == 'rock') or
            (player_choice == 'scissors' and computer_choice == 'paper')
        ):
            print("You win!")
        else:
            print("Computer wins!")

        play_again = input("Do you want to play again? (yes/no): ").lower()

        if play_again != 'yes':
            break

    print("Thank you for playing!")

play_game()
