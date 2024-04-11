import random

choices = ['rock', 'paper', 'scissors']

while True:
    choice = input('Choose 1: Rock, 2: Paper, 3: Scissors (enter the number): ')
    computer_choice = random.choice(choices)
    if choice == '1':
        if computer_choice == 'rock':
            print(f'The computer chose {computer_choice}')
            print('Tie')
        elif computer_choice == 'paper':
            print(f'The computer chose {computer_choice}')
            print('Lose')
        else:
            print(f'The computer chose {computer_choice}')
            print('Win')
    elif choice == '2':
        if computer_choice == 'rock':
            print(f'The computer chose {computer_choice}')
            print('Win')
        elif computer_choice == 'paper':
            print(f'The computer chose {computer_choice}')
            print('Tie')
        else:
            print(f'The computer chose {computer_choice}')
            print('Lose')
    elif choice == '3':
        if computer_choice == 'rock':
            print(f'The computer chose {computer_choice}')
            print('Lose')
        elif computer_choice == 'paper':
            print(f'The computer chose {computer_choice}')
            print('Win')
        else:
            print(f'The computer chose {computer_choice}')
            print('Tie')
    else:
        print('Wrong input')
    again = input('Do you want to play again ? (y/n): ')
    if again == 'n':
        print('Bye !')
        break