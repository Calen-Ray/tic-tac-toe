# lets try to build tic-tac-toe using purely python code, no ui, nothing crazy, just trying to keep skills fresh

import string
import math
from sys import platform
from typing import Counter
import random


# ----------- a sea of functions to compartmentalize this game -----------#

def identify_move(board:list) -> dict:
    """ The purpose of this function is to attempt to identify the best move on a tic-tac-toe board """

    # These are the basics,
    o_score = sum([row.count('O') for row in board]) # score is the count of O's in the board
    x_score = sum([row.count("X") for row in board]) # score is the count of X's in the board
    ai_symbol = 'X' if x_score < o_score else "O" # determins the AI's symbol based on which symbols turn it is
    player_symbol = "X" if ai_symbol == "O" else "O" # determins the players symbol based on the AIs
    claimable = "-" 

    if o_score < 1 or x_score < 1:
        # randomize the first cpu move.
        return {"row": random.randint(0, 2), "index": random.randint(0, 2)}
    
    for i, row in enumerate(board):
        # this will check for the availablity of a victory horizontally 
        if row.count(ai_symbol) == 2 and row.count(claimable) == 1:
            # if the ai already owns two places on this row, and the third is unclaimed, claim the third
            return {"row": i, "index": row.index(claimable)}
    
    for i in range(3):
        # range three as the range function is non-inclusive of final number
        slice = [board[0][i], board[1][i], board[2][i]]
        # Checking each row, index 0, then 1, then 2 looking for a winnable series
        if slice.count(ai_symbol) == 2 and slice.count(claimable) == 1:
            return {"row": slice.index(claimable), "index": i}

    # Next we need to calculate potential victory by cross play
    cross_play_one = [board[0][0], board[1][1], board[2][2]]
    cross_play_two = [board[2][0], board[1][1], board[0][2]]
    
    if cross_play_one.count(ai_symbol) == 2 and cross_play_one.count(claimable) == 1:
        # if computer can win via top left to the bottom right, will return winning answer
            # ironically we can use the same calculation for each row and index in our dict due to the layout of the cross-play-one variable.
            return {"row": cross_play_one.index(claimable), "index": cross_play_one.index(claimable)}

    if cross_play_two.count(ai_symbol) == 2 and cross_play_two.count(claimable) == 1:
        # if computer can win via bottom left to the top right, will return winning answer
            # Neat work around, whatever the index of the cross-play-two, we just neet to return the absolution of that number minus two for the row in the board. 
            return {"row": abs(cross_play_two.index(claimable)-2), "index": cross_play_two.index(claimable)}

    # at this point we know we cannot win this turn, so lets calulate a good next move, looking for denial of the humans victory.
    # 

    for i, row in enumerate(board):
    # this will check for the availablity of a victory horizontally 
        if row.count(player_symbol) == 2 and row.count(claimable) == 1:
            # if the ai already owns two places on this row, and the third is unclaimed, claim the third
            return {"row": i, "index": row.index(claimable)}

    for i in range(3):
        # range three as the range function is non-inclusive of final number
        slice = [board[0][i], board[1][i], board[2][i]]
        # Checking each row, index 0, then 1, then 2 looking for a winnable series
        if slice.count(player_symbol) == 2 and slice.count(claimable) == 1:
            return {"row": slice.index(claimable), "index": i}

    # Next we need to calculate potential victory by cross play
    cross_play_one = [board[0][0], board[1][1], board[2][2]]
    cross_play_two = [board[2][0], board[1][1], board[0][2]]
    
    if cross_play_one.count(player_symbol) == 2 and cross_play_one.count(claimable) == 1:
        # if computer can win via top left to the bottom right, will return winning answer
            # ironically we can use the same calculation for each row and index in our dict due to the layout of the cross-play-one variable.
            return {"row": cross_play_one.index(claimable), "index": cross_play_one.index(claimable)}

    if cross_play_two.count(player_symbol) == 2 and cross_play_two.count(claimable) == 1:
        # if computer can win via bottom left to the top right, will return winning answer
            # Neat work around, whatever the index of the cross-play-two, we just neet to return the absolution of that number minus two for the row in the board. 
            return {"row": abs(cross_play_two.index(claimable)-2), "index": cross_play_two.index(claimable)}


    # Okay so now we've identified no one is winning this turn, 
    # lets proceed to make a logical next step,
    # we are going to look for a play with two open spaces with the third claimed by the ai.
        
    for i, row in enumerate(board):
        # this will check for the availablity of a play horizontally 
        if row.count(ai_symbol) == 1 and row.count(claimable) == 2:
            # if the ai already owns one place on this row, and the other two are unclaimed, claim the first 
            return {"row": i, "index": row.index(claimable)}
    
    for i in range(3):
        # range three as the range function is non-inclusive of final number
        slice = [board[0][i], board[1][i], board[2][i]]
        # Checking each row, index 0, then 1, then 2 looking for a play-able series
        if slice.count(ai_symbol) == 1 and slice.count(claimable) == 2:
            return {"row": slice.index(claimable), "index": i}

    # Next we need to calculate potential play by cross play
    cross_play_one = [board[0][0], board[1][1], board[2][2]]
    cross_play_two = [board[2][0], board[1][1], board[0][2]]
    
    if cross_play_one.count(ai_symbol) == 1 and cross_play_one.count(claimable) == 2:
        # if computer can win via top left to the bottom right, will return playable answer
            # ironically we can use the same calculation for each row and index in our dict due to the layout of the cross-play-one variable.
            return {"row": cross_play_one.index(claimable), "index": cross_play_one.index(claimable)}

    if cross_play_two.count(ai_symbol) == 1 and cross_play_two.count(claimable) == 2:
        # if computer can play  via bottom left to the top right, will return playable answer
            # Neat work around, whatever the index of the cross-play-two, we just neet to return the absolution of that number minus two for the row in the board. 
            return {"row": abs(cross_play_two.index(claimable)-2), "index": cross_play_two.index(claimable)}

    elif sum([row.count("-") for row in board]) == 1:
        # Identify if there is one remaining play, return the final move
        for i, row in enumerate(board):
            if row.count('-') == 1:
                return {"row": i, "index": row.index("-")}
    
    else:
        while True:
            row = random.randint(0,2)
            index = random.randint(0,2)
            if validate_move(row, index, board):
                return {"row": row, "index": index}


def game_status(board: list) -> tuple:
    """ Function checks if there is a valid victory in the passed board.  """

    for row in board:
        # check for horizontal win
        x='X'
        o="O"
        if row.count(x) == 3:
            return (True, x)
        elif row.count(o) == 3:
            return (True, o)
    
    for i in range(3):
        #checks for veritcal win
        # range three as the range function is non-inclusive of final number
        slice = [board[0][i], board[1][i], board[2][i]]
        # Checking each row, index 0, then 1, then 2 looking for a winnable series
        if slice.count(x) == 3:
            return (True, x)
        elif slice.count(o) == 3:
            return (True, o)
    
    #check for cross-play win
    cross_play_one = [board[0][0], board[1][1], board[2][2]]
    cross_play_two = [board[2][0], board[1][1], board[0][2]]

    if cross_play_two.count(x) == 3 or cross_play_one.count(x) == 3:
        return (True, x)
    elif cross_play_two.count(o) == 3 or cross_play_one.count(o) == 3:
        return (True, o)

    elif sum([row.count("-") for row in board]) == 0:
        # Identify if there are no remaining plays, return a game over
        return (True, "error")

    else:
        # We all know the else is not needed, dont @ me, it makes this shit more readable.
        return (False, "TIE")


def validate_move(row:int, index:int, board:list) -> bool:
    """ Use this function to determin if the move from the human is valid """
    return True if board[row][index] == "-" else False


def create_move(player:str) -> tuple:
    """ This function should allow us to create a move and validate its authenticity """


    player = player.lower()
    valid_play = [0,1,2] # need three so we can prove valid option prior adjustment for zero index. 
    if player != 'human' and player != 'ai':
        print(f'Error, there was an issue in the create_move function, passed player type is neither AI or Player.')
        return None



    if player == 'human':
    # if passed player type is human, perform a sequence that takes in user input for desired row and index.

        while True:
            # utilize a while loop to repose the question in the event that the move is invalid
            row = int(''.join([x for x in input('Player one please input your desired row number') if x in string.digits]))
            # utilizing this bazar list comprehension method will allow us to be able to skip the need for a validation of using int() 
            # becuase inherintly anything remaining from the comprehensive filter is a int-able number
            index = int(''.join([x for x in input(f"Please input your desired index 1-3") if x in string.digits]))
            row -=1
            index -= 1

            if validate_move(row, index, board) == False:
                # this will check to see if the move is invalid, if so, it will provide an error message and rerun the selection options for making a play
                print(f'It would appear row: {row+1} and index: {index+1} already contain a {board[row][index]}, please try again.')

            elif row in valid_play and index in valid_play:
                # this says, if row and index are between 0-2 each,
                break

            else: 
                # if row and index are not between 0-2, submit this error and recollect the data.
                print(f'There was an error trying to use your selection of \nRow: {row} or \nIndex: {index}\nPlease use only rows 1-3 and index 1-3 where the top left is row 1, index 1. ')



    elif player == 'ai':
        # this will allow us to formulate a AI move.
        while True:
            # this will allow us to loop if needed.
            ai_move = identify_move(board) # use function to return a tupil of data containing the ai's play
            row = ai_move['row']
            index = ai_move['index']
            if validate_move(row, index, board):
                break
            # if the validation is not successful it will loop and allow the computer another try at making a move. 
        

    # Finally, regardless of the player type we need to submit the raw and index for later evaluation.
    return {'row': row, 'index': index}


def pretty_board(board:list) -> str:
    ''' This function will take in a list of lists and convert it to a tic-tac-toe board for user interface '''

    if len(board[0]+board[1]+board[2]) != 9:
        # if you are not passing me a list of lists with the total length of nine items than error 
        print(f'There was an error in trying to display the board, this error is caused by a malfunction of the board data itself.')
        return None

    current_board = f"{'|'.join(board[0])}\n-----\n{'|'.join(board[1])}\n-----\n{'|'.join(board[2])}"
    # Generate a 2D board for viewing.

    print(current_board)
    return None


def player_settings(player_number:str, choose_symbol=False) -> dict:
    ''' Input your player title (1/2/ect), user will be prompted to select ai or human, and symbols if desired. '''

    while True: # looping through until player makes valid selection of player/human, x/o, etc.
        player_type = input(f'Who would you like to play as {player_number}, a human player or computer? ( computer/human) ').lower()

        if player_type in ['human', 'person', 'me']: # checks to see if the player selected to have a human play.

            player_type = 'human' # lets cut the edge cases and convert the player_type to human with absolute certainty as its relied on for other functions

            if not choose_symbol:
                # if choose symbol is deactived (it is by default) we will return just the player type.
                return {'player_type': player_type}


            while True: # allows us to loop until a valid selection of X/O is made
                symbol_choice = input(f'For your Human {player_number} what symbol choice would you like? X/O').upper()

                if symbol_choice in ['X','O']:
                    return {'player_type': player_type, 'symbol_choice': symbol_choice}

                else:
                    print(f'There was an issue with your choice of {symbol_choice}, please make a valid selection.')

        elif player_type in ['ai', 'cpu', 'computer']: # checks to see if the player selected to have a computer assist with playing.

            player_type = 'ai' # lets establish with absolution that player_type is equal to ai, not cpu or computer, for consistancy throughout.

            if not choose_symbol:
                # if choose symbol is deactived (it is by default) we will return just the player type.
                return {'player_type': player_type}
            

            while True: # allows us to loop until a valid selection of X/O is made
                symbol_choice = input(f'For your computer, {player_number} what symbol choice would you like? X/O').upper()

                if symbol_choice in ['X','O']:
                    return {'player_type': player_type, 'symbol_choice': symbol_choice}

                else:
                    print(f'There was an issue with your choice of {symbol_choice}, please make a valid selection.')
            
            

        else:
            print(f'\nThere was an error with your input of {player_type}, please try again with a valid option')



# ----------- two while loops to allow for the outer loop to control each new game and the inner loop to control turn repetition -----------#
while True:

    player_one_symbol = False # sets our player one symbol to false, a trigger used to identify the need for first time setup
    board = [['-','-','-'],['-','-','-'], ['-','-','-']] # obviously our board that uses three lists within a list as our game-board where the master index is board[row][position/index]


    while True:

        # ----------- First time setup only ran if player_one_symbol is not set I.E. New game -----------#
        if not player_one_symbol:

            # this will obviously run a player creation function that return a disct as such: {'player_type': player_type, 'symbol_choice': symbol_choice}
            player_one = player_settings('Player one', True)
            player_one_type = player_one['player_type']
            player_one_symbol = player_one['symbol_choice']


            # now we can create a second player for use
            player_two = player_settings('Player two') # note we did not pass a second arg to the function, no need as we already know the symbol used for p2. 
            player_two_type = player_two['player_type']
            player_two_symbol = 'X' if player_one_symbol == 'O' else 'O' # we can determin the second players symbol with deductive reasoning, we dont need anything fancy or to ask the user.



        # ---- before any player is able to play, we should display the board for them. ----#
        pretty_board(board)



        # ----------- player one's turn -----------#
        player_one_move = create_move(player_one_type)
        board[ player_one_move['row'] ] [ player_one_move['index'] ] = player_one_symbol # puts the player_one_move choice into the board
        game_won, winner = game_status(board)
        # returns a tupil of (True/False, X/O/tie/None) where the bool is if the game is over, and the string is the winning results
        if game_won:
            # final step of any turn is to determin if the game has been won. 
            break
        


        # ---- before any player is able to play, we should display the board for them. ----#
        pretty_board(board)



        # ----------- player two's turn -----------#
        ai_move = create_move(player_two_type)
        board[ ai_move['row'] ] [ ai_move['index'] ] = player_two_symbol # puts the ai choice into the list
        game_won, winner = game_status(board)
        # returns a tupil of (True/False, X/O/tie/None) where the bool is if the game is over, and the string is the winning results
        if game_won:
            # final step of any turn is to determin if the game has been won. 
            break




    # this is all post-game loop, this will run after the computer has determined if there was a victor. 
    if winner == 'TIE':
        pretty_board(board)
        print(f'Looks like a Tie! Maybe you can beat the bot next time.')

    else:
        pretty_board(board)
        print(f"Congrats to {winner}, You played well. ")

    again = input("Would you like to play again? yes/no: ")
    if again in ['no', 'n']:
        break


