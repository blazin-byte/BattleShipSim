# UGLY BOILERPLATE EWWW
import sys
from pathlib import Path  # if you haven't already done so
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

# Actual imports
from src.game_board import GameBoard, Ship, Tile
from src.game_server import GameServer
import pygame as pg


##################
# GAME CONSTANTS #
##################


WINDOW_SIZE = (1200, 600)
WATER_COLOR = (157, 223, 247)


############################
# STARTUP/CONFIG FUNCTIONS #
############################


def setup_window() -> pg.Surface:
    # Define the dimensions of
    # screen object(width,height)
    screen = pg.display.set_mode(WINDOW_SIZE)

    # Set the caption of the screen
    pg.display.set_caption('BATTLESHIP - TO THE DEATH')

    # Fill the background colour to the screen
    screen.fill(WATER_COLOR)

    # Update the display using flip
    pg.display.flip()

    return screen


##################
# MAIN GAME LOOP #
##################


def main():

    screen = setup_window()

    #

    dummy_tile = Tile(1, 2)
    dummy_tile.reset_before_game()
    screen.blit(dummy_tile.display_surface, (100, 100))

    #

    # Variable to keep our game loop running
    running = True

    # game loop
    while running:

        # for loop through the event queue
        for event in pg.event.get():

            # Check for QUIT event
            if event.type == pg.QUIT:
                running = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_j:
                    dummy_tile.on_hit()
                    screen.blit(dummy_tile.display_surface, (100, 100))
                elif event.key == pg.K_k:
                    dummy_tile.reset_before_game()
                    screen.blit(dummy_tile.display_surface, (100, 100))

        # Update the display
        pg.display.flip()


if __name__ == "__main__":
    main()
