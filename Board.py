import numpy
import copy
from Square import Square
from Checker import Checker
import Minmax
import globalVariables

def addChecker(x, y):
    if y == 3 or y == 4:
        return
    checker = Checker()
    checker.id = (x, y)
    if y < 4:
        checker.black = True
    checker.x = x
    checker.y = y
    board[x, y].checker = checker
    checkers.append(checker)

# Completely copies board for minimax
def copyBoard(origin):
    new_board = copy.deepcopy(origin)
    for square in board.flat:
        new_board[int(square.x/81.25),int(square.y/81.25)] = copy.deepcopy(square)
        new_board[int(square.x / 81.25), int(square.y / 81.25)].checker = copy.deepcopy(square.checker)
    return new_board

def King(board):
    for piece in board.flat:
        if piece.checker is None or piece.checker.king:
            continue
        if (piece.y/81.25 == 7 and piece.checker.black) or (piece.y/81.25 == 0 and not piece.checker.black):
            piece.checker.king = True


def getFullMove(partial_move):
    moves = Minmax.findJumps(board, False) + Minmax.findMoves(board, False)
    for move in moves:
        if move.checker.id == partial_move.checker.id and move.piece.x == partial_move.piece.x \
                and move.piece.y == partial_move.piece.y:
            return move
    return None

def countWhite(board):
    counter=0
    for piece in board.flat:
        if piece.checker is None:
            continue
        if (not piece.checker.black):
            counter=counter+1
    return counter

def countBlack(board):
    counter=0
    for piece in board.flat:
        if piece.checker is None:
            continue
        if (piece.checker.black):
            counter=counter+1
    return counter

def hasWon(board):
    white_actions = Minmax.findJumps(board, False) + Minmax.findMoves(board, False)
    black_actions = Minmax.findJumps(board, True) + Minmax.findMoves(board, True)
    # print("black actss",len(black_actions))
    # print("white actss",len(white_actions))
    if(globalVariables.whites>countWhite(board)):
        globalVariables.moves_without_attack=0
        globalVariables.attacks=globalVariables.attacks+(globalVariables.whites-countWhite(board))
        globalVariables.whites=countWhite(board)
    if(globalVariables.blacks>countBlack(board)):
        globalVariables.moves_without_attack=0
        globalVariables.attacks=globalVariables.attacks+(globalVariables.blacks-countBlack(board))
        globalVariables.blacks=countBlack(board)
    if len(white_actions) == 0 or countWhite(board)==0:
        return -1
    elif len(black_actions) == 0 or countBlack(board)==0:
        return 1
    if globalVariables.moves_without_attack==30:
        if(countWhite(board)<countBlack(board)):
            return -1
        elif(countWhite(board)>countBlack(board)):
            return 1
        else:
            return 2
    else:
        return 0


# The board of the game
board = numpy.empty((8, 8), dtype=Square)
checkers = []
square_offset = False

# Initializes the board
for x in range(0, 8):
    if x % 2 == 1:
        square_offset = True
    else:
        square_offset = False
    for y in range(0, 8):
        square = Square(x * 81.25, y * 81.25)  # 500/8
        board[x, y] = square
        if (x % 2 == 0 or y % 2 == 0) and (square_offset == True):
            addChecker(x, y)
        elif (x % 2 == 1 or y % 2 == 1) and (square_offset == False):
            addChecker(x, y)
