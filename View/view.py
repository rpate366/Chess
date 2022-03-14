import pygame

# Unicode index for pieces, lower case is black
unicode_index = {
    "r" : "♜", "n" : "♞", "b" : "♝", "q" : "♛", "k" : "♚", "p" : "♟",
    "R" : "♖", "N" : "♘", "B" : "♗", "Q" : "♕", "K" : "♔", "P" : "♙",
    "." : ""
}


def updateView(view, data, size) :
    # Remove spaces, easier to work with later
    data = data.replace(" ", "")

    # Board length, must be even
    boardLength = 8
    view.fill((255, 255, 255))

    for i in range(0, boardLength):
        for z in range(0, boardLength):
            # Check if current loop value is even, even == white squares
            if (i + z) % 2 == 0:
                pygame.draw.rect(view, (242, 225, 195), [size * z, size * i, size, size])
            else:
                pygame.draw.rect(view, (195, 160, 130), [size * z, size * i, size, size])
            
            # Use index to find correct pieces, search string depending on what square is being loaded
            piece_to_insert = unicode_index[data[i * 9 + z]]

            # Render and add with this super hard font to find for whatever reason
            f = pygame.font.SysFont("segoeuisymbol", 64)
            view.blit(f.render(piece_to_insert, True, (0, 0, 0)), (size * z + (size * .07), size * i - (size * .115)))

    # Add a nice border
    pygame.draw.rect(view, (155, 155, 155), [0, 0, boardLength * size, boardLength * size], 3)

    return view