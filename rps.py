# Rock Paper Scissors Game to practice Python

# Ask the user to make a choice (rock, paper, scissors)
import random

choice_dict = {'r': 'Rock!', 's': 'Scissors!', 'p': 'Paper!'}
choices = ('r', 'p', 's')

while True:
    user_choice = input('Rock, paper, or scissors? (r/p/s): ').lower()
    if user_choice not in choices:
        print("Invalid Choice!")  # If choice is not valid - print an error
        continue

    computer_choice = random.choice(choices)

    print(f'You chose {choice_dict[user_choice]}')
    print(f'Computer chose {choice_dict[computer_choice]}')

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == 'r' and computer_choice == 's') or
        (user_choice == 's' and computer_choice == 'p') or
            (user_choice == 'p' and computer_choice == 'r')):
        print("You win!")
    else:
        print("Computer Wins! Too bad")

# Ask the user if they want to play again - if no break the loop.
    keep_playing = input("Do you want to continue playing? (y/n): ").lower()
    if keep_playing == 'n':
        break
