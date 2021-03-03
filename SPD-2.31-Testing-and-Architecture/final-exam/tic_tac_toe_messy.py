# Tic Tac Toe
# Reference: With modification from http://inventwithpython.com/chapter10.html.

import random

board_size = 10

def draw_board(board):
    """ This function prints out the board that it was passed."""

    # "board" is a list of 10 strings representing the board (ignore index 0)
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def input_player_letter():
    """Lets the player type which letter they want to be"""
    # Returns a list with the player’s letter as the first item, and the computer's letter as the second.
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    # the first element in the list is the player’s letter, the second is the computer's letter.
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def who_goes_first():
    """Randomly choose the player who goes first."""
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def play_again():
    """ This function returns True if the player wants to play again, otherwise it returns False."""
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def make_move(board, letter, move):
    board[move] = letter

def is_winner(bo, le):
    """ Given a board and a player’s letter, this function returns True if that player has won."""
    # We use bo instead of board and le instead of letter so we don’t have to type as much.
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
            (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
            (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
            (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
            (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
            (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
            (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
            (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

def get_board_copy(board):
    """ Make a duplicate of the board list and return it the duplicate."""
    dupe_board = []

    for i in range(len(board)):
        dupe_board.append(board[i])

    return dupe_board

def is_space_free(board, move):
    """ Return true if the passed move is free on the passed board."""
    return board[move] == ' '

def get_player_move(board):
    """ Let the player type in their move."""
    next_move = ' '
    while next_move not in '1 2 3 4 5 6 7 8 9'.split() or not is_space_free(board, int(next_move)):
        print('What is your next next_move? (1-9)')
        next_move = input()
    return int(next_move)

def choose_random_move_from_list(board, move_list):
    """ Returns a valid move from the passed list on the passed board."""
    # Returns None if there is no valid move.
    possible_moves = []
    for i in move_list:
        if is_space_free(board, i):
            possible_moves.append(i)

    if len(possible_moves):
        return random.choice(possible_moves)
    return None

def get_computer_move(board, computer_move):
    """ Given a board and the computer's move, determine where to move and return that move."""
    if computer_move == 'X':
        player_move = 'O'
    else:
        player_move = 'X'

    # Here is our algorithm for our Tic Tac Toe AI:
    # First, check if we can win in the next move
    for i in range(1, board_size):
        copy = get_board_copy(board)
        if is_space_free(copy, i):
            make_move(copy, computer_move, i)
            if is_winner(copy, computer_move):
                return i

    # Check if the player could win on their next move, and block them.
    for i in range(1, board_size):
        copy = get_board_copy(board)
        if is_space_free(copy, i):
            make_move(copy, player_move, i)
            if is_winner(copy, player_move):
                return i

    # Try to take one of the corners, if they are free.
    move = choose_random_move_from_list(board, [1, 3, 7, 9])
    if move is not None:
        return move

    # Try to take the center, if it is free.
    if is_space_free(board, 5):
        return 5

    # Move on one of the sides.
    return choose_random_move_from_list(board, [2, 4, 6, 8])

def is_board_full(board):
    # Return True if every space on the board has been taken. Otherwise return False.
    for i in range(1, board_size):
        if is_space_free(board, i):
            return False
    return True

def is_game_playing(new_turn, this_board, player_letter, computer_letter):
    """Checks current game if its still playing, a winner, or tied game"""
    player_won = is_winner(this_board, player_letter)
    computer_won = is_winner(this_board, computer_letter)
    tied = is_board_full(this_board)

    if player_won or computer_won:
        draw_board(this_board)
        if new_turn == 'player':
            print('Nice! You won the game!')
        else:
            print('The computer won! You lost')
        return False
    if tie_game:
        draw_board(this_board)
        print('The game is a tie!')
        return False
    return True

def player_turn(play_board, play_letter, comp_letter):
    """Get the player's move and make the changes to the board"""
    draw_board(play_board)
    play_move = get_player_move(play_board)
    make_move(play_board, play_letter, play_move)

def computer_turn(comp_board, play_letter, comp_letter):
    """Get the computer's move and make the changes to the board"""
    comp_move = get_computer_move(comp_board, comp_letter)
    make_move(comp_board, comp_letter, comp_move)

print('Welcome to Tic Tac Toe!')

while True:
    board_size = 10
    the_board = [' '] * board_size
    player_letter, computer_letter = input_player_letter()
    turn = who_goes_first()
    print('The ' + turn + ' will go first.')
    while True:
        if turn == 'player':
            player_turn(the_board, player_letter, computer_letter)
            if is_game_playing(turn, the_board, player_letter, computer_letter):
                turn = 'computer'
            else:
                break
        else:
            computer_turn(the_board, player_letter, computer_letter)
            if is_game_playing(turn, the_board, player_letter, computer_letter):
                turn = 'player'
            else:
                break
    if not play_again():
        break