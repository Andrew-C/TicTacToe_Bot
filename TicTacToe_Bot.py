import random

global board
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
global turn
turn = 1    #turn counter
MAX_PLAY =  3000

def print_board(board):
    displaystate = list(board)

    for i, val in enumerate(board):
        # a value of 10 in the board is an X for the computer
        if val == 10:
            displaystate[i] = "X"
        # a value of 11 in the board is an O fo the player
        elif val == 11:
            displaystate[i] = "O"
        else:
            displaystate[i] = str(board[i])

    line1 = ("| " + str(displaystate[0]) + "| " + str(displaystate[1]) + "| " + str(displaystate[2]) + "|")
    line2 = ("| " + str(displaystate[3]) + "| " + str(displaystate[4]) + "| " + str(displaystate[5]) + "|")
    line3 = ("| " + str(displaystate[6]) + "| " + str(displaystate[7]) + "| " + str(displaystate[8]) + "|")
 
    print(" __ __ __")
    print(line1)
    print(" __ __ __")
    print(line2)
    print(" __ __ __")
    print(line3)
    print(" __ __ __")

def find_next_move(state):
    # returns the index of the largest value
    score = random_playout(state)
    return score.index(max(score))

def random_playout(state):
    # copies the current board
    global turn
    tempTurn = turn
    curr_play = 0   # play counter for each move
    play_score = 0 # tracks the current score of the current move
    score_board = [] # tracks the scores of each move
    moveset = valid_moves(state)

    for i in moveset:
        # start of playouts beginning with move i
        while(curr_play < MAX_PLAY):
            compTurn = False
            playout_board = state.copy()       # resets the board for the new play
            playout_board[i - 1] = 10
            turn += 1

            #start of playout
            while(is_terminal(playout_board) == 3):     # 3 means an unfinished game
                # grabs a new set of moves
                moveset = valid_moves(playout_board)
                # chooses a random move from moveset
                move = random.choice(moveset)
                # makes the move
                if(compTurn == True):
                    playout_board[move - 1] = 10
                    compTurn = False
                    turn += 1
                else:
                    playout_board[move - 1] = 11
                    compTurn = True
                    turn += 1

            # end of current playout
            if(is_terminal(playout_board) == 0):
                # awards 1 point for draws
                play_score += 1
            elif(is_terminal(playout_board) == 1):
                # awards 3 points for wins
                # no points for losses
                play_score += 3
            turn = tempTurn                #reset turn counter
            curr_play += 1

        score_board.append(play_score)  # adds the final playscore to the list
        play_score = 0                  # resets playscore for new game beginning with i
        curr_play = 0                   #resets current play for new game beginning with i

    turn = tempTurn
    return score_board




def valid_moves(state):
    array = []
    for i, val in enumerate(state):
        if val != 10 and val != 11:
            array.append(state[i])

    return array

def is_terminal(state):
    global turn
    if(turn >= 10):
        # no more available moves 
        # returns 0 for a draw
        return 0

    # horizontal win conditions
    elif(state[0] == state[1] and state[1] == state[2]):
        if(state[0] == 10):
            # returns 1 if winning line was X for computer
            return 1
        else:
            # returns 2 if winning line was O for player
            return 2

    elif(state[3] == state[4] and state[4] == state[5]):
        if(state[3] == 10):
            return 1
        else:
            return 2

    elif(state[6] == state[7] and state[7] == state[8]):
        if(state[6] == 10):
            return 1
        else:
            return 2

    # vertical win conditions
    elif(state[0] == state[3] and state[3] == state[6]):
        if(state[0] == 10):
            # returns 1 if winning line was X for computer
            return 1
        else:
            # returns 2 if winning line was O for player
            return 2

    elif(state[1] == state[4] and state[4] == state[7]):
        if(state[1] == 10):
            return 1
        else:
            return 2

    elif(state[2] == state[5] and state[5] == state[8]):
        if(state[2] == 10):
            return 1
        else:
            return 2
    #  diagonal win conditions
    elif(state[0] == state[4] and state[4] == state[8]):
        if(state[0] == 10):
            return 1
        else:
            return 2

    elif(state[2] == state[4] and state[4] == state[6]):
        if(state[2] == 10):
            return 1
        else:
            return 2
    else:
        # returns 3 for unfinished game
        return 3




if __name__ == '__main__':
    finished = False
    myTurn = False
    compTurn = True
    compMoveSet = []
    moveToTake = 0
    
# start of the game
# computer goes first and uses the "X" mark
    while(finished == False):

        if(myTurn == True):
            # changes the turn the computer
            x = input("Enter a number to mark the corresponding square: ")
            # if input is invalid or outside the scope of the board
            if(board[int(x) - 1] == 10 or board[int(x) - 1] == 11 or int(x) > 9 or int(x) < 1):
                print("invalid move")
            else:
                board[int(x) - 1] = 11
                myTurn = False
                compTurn = True
                turn += 1
        elif(compTurn == True):
            if(turn == 1):
                board[random.randint(0,8)] = 10
            else:
                # makes a list of valid moves
                compMoveset = valid_moves(board)
                # determins which move is the best
                moveToTake = find_next_move(board)
                # makes the move
                board[compMoveset[moveToTake] - 1] = 10

            # changes the turn the player
            compTurn = False
            myTurn = True
            turn += 1
            print_board(board)

        if(is_terminal(board) == 0):
            finished = True
            print("DRAW")
        elif(is_terminal(board) == 1):
            finished = True
            print("YOU LOSE")
        elif(is_terminal(board) == 2):
            finished = True
            print("YOU WIN")

