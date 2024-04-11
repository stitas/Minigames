import os

player_x = 'X'
player_o = 'O'
run = True
turn = 'X'
valid_squares = [1,2,3,4,5,6,7,8,9]
square_values = {1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',}
board = f'{square_values[1]}|{square_values[2]}|{square_values[3]}\n-----\n{square_values[4]}|{square_values[5]}|{square_values[6]}\n-----\n{square_values[7]}|{square_values[8]}|{square_values[9]}'

def clear_board():
    for square in square_values:
        if square_values[square] == str(square):
            square_values[square] = ' '

def check_winner(player):
    if square_values[1] == player and square_values[2] == player and square_values[3] == player:
        return True
    elif square_values[4] == player and square_values[5] == player and square_values[6] == player:
        return True
    elif square_values[7] == player and square_values[8] == player and square_values[9] == player:
        return True
    elif square_values[1] == player and square_values[4] == player and square_values[7] == player:
        return True
    elif square_values[2] == player and square_values[5] == player and square_values[8] == player:
        return True
    elif square_values[3] == player and square_values[6] == player and square_values[9] == player:
        return True
    elif square_values[1] == player and square_values[5] == player and square_values[9] == player:
        return True
    elif square_values[3] == player and square_values[5] == player and square_values[7] == player:
        return True
    else:
        return False

def get_input(player):
    square = input(f'Enter Square {player}: ')
    if int(square) in valid_squares:
        square_values[int(square)] = player
        valid_squares.remove(int(square))
        if check_winner(player):
            os.system('cls')
            clear_board()
            board = f'\n {square_values[1]} | {square_values[2]} | {square_values[3]}\n ----------\n {square_values[4]} | {square_values[5]} | {square_values[6]}\n ----------\n {square_values[7]} | {square_values[8]} | {square_values[9]}\n'
            print(board)
            print(player + ' Wins!')
            return False
        elif len(valid_squares) == 0:
            os.system('cls')
            clear_board()
            board = f'\n {square_values[1]} | {square_values[2]} | {square_values[3]}\n ----------\n {square_values[4]} | {square_values[5]} | {square_values[6]}\n ----------\n {square_values[7]} | {square_values[8]} | {square_values[9]}\n'
            print(board)
            print('Tie!')
            return False
        else:
            os.system('cls')
            return True
    else:
        print('Wrong input')
        return 'error'

os.system('cls')
while run:
    board = f'\n {square_values[1]} | {square_values[2]} | {square_values[3]}\n ----------\n {square_values[4]} | {square_values[5]} | {square_values[6]}\n ----------\n {square_values[7]} | {square_values[8]} | {square_values[9]}\n'
    print(board)
    if turn == player_x:
        run = get_input(player_x)
        if run != 'error':
            turn = player_o
            continue
        run = True
    else:
        run = get_input(player_o)
        if run != 'error':
            turn = player_x
            continue
        run = True
    