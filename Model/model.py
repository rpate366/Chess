import string
import chess

def makeMove(board: chess, move, promotion = None):
    if chess.Move.from_uci(move) in chess.LegalMoveGenerator(board):
        board.push(chess.Move.from_uci(move))
    return board

def mouseUp():
    print("Mouse Up")

def stalemateCheck():
    return False