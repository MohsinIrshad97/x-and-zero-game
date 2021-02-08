#from IPython.display import clear_output
def display_board(board):
    #clear_output()  # Remember, this only works in jupyter!
    
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

    
def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

import random

def choose_first():
    if random.randint(0, 1) == 0:
        return 'player2'
    else:
        return 'player1'

def space_check(board, position):
    
    return board[position] == ' ' 
    
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False 
    return True
    
def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position

def replay():
    
    choice=input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')
    return choice =="Yes"
print('Welcome to Tic Tac Toe!')
while True: 

    #play game

    # set everything up(board, who is first,choose marker)
    test_board1=[' ']*10
    display_board(test_board1)
    (p1marker, p2marker)=player_input()
    turn=choose_first()
    print("{} goes first".format(turn))
    playgame = input("ready ? enter y or n:")
    if playgame == "y":
        game_on = True
    else:
        game_on= False

    #game play
    while game_on:

        if turn == 'player1':
            display_board(test_board1)
            position = player_choice(test_board1)
            place_marker(test_board1, p1marker, position)
            if win_check(test_board1,p1marker):
                display_board(test_board1)
                print("player1 has won")
                game_on = False 
            else:
                if full_board_check(test_board1):
                    display_board(test_board1)
                    print("its a tie")
                    break   
                else:
                    turn="player2"
                  ##player 1
        else:
            display_board(test_board1)
            position = player_choice(test_board1)
            place_marker(test_board1, p2marker, position)
            if win_check(test_board1, p2marker):
                display_board(test_board1)
                print("player2 has won")
                game_on = False 
            else:
                if full_board_check(test_board1):
                    display_board(test_board1)
                    print("its a tie")
                    break
                else:
                    turn='player1'
                      

        ##player2
 

    if not replay():
        break




       

    