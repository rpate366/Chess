import sys
sys.path.append("../")

from View.view import *
from Model.model import *
import chess
import pygame

def getMove():
    move = input("Enter move: ")
    return move

if __name__ == "__main__":
    pygame.init()
    board = chess.Board()

    # Set window and individual cell size
    cellSize = 75
    screen = pygame.display.set_mode((cellSize * 8, cellSize * 8))

    # Prep and show board
    screen = updateView(screen, str(board), cellSize)
    pygame.display.update()

    while True:
        for e in pygame.event.get():
            global d_square
            global u_square

            if e.type == pygame.QUIT:
                print("Closing Game Without Saving")
                pygame.quit()
                sys.exit()
            
            elif e.type == pygame.MOUSEBUTTONDOWN:
                # Get location
                pos = pygame.mouse.get_pos()
                x = pos[0] // cellSize
                y = pos[1] // cellSize

                # d_square set to the chess coordinate clicked
                d_square = chr(97 + x) + str(8 - y)

            elif e.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                x = pos[0] // cellSize
                y = pos[1] // cellSize
                u_square = chr(97 + x) + str(8 - y)
                
                if d_square == u_square:
                    move = "0000"
                else:
                    move = d_square + u_square
                    
                board = makeMove(board, move)
                
                screen = updateView(screen, str(board), cellSize)
                pygame.display.update()