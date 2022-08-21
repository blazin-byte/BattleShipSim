# UGLY BOILERPLATE EWWW
import sys
from pathlib import Path  # if you haven't already done so
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

# Actual imports
from src.game_board import GameBoard, Ship, Tile
from src.game_server import GameServer
import src.constants as constants
import pygame as pg


############################
# STARTUP/CONFIG FUNCTIONS #
############################


def setup_window() -> pg.Surface:
    # Define the dimensions of
    # screen object(width,height)
    screen = pg.display.set_mode(constants.WINDOW_SIZE)

    # Set the caption of the screen
    pg.display.set_caption('BATTLESHIP - TO THE DEATH')

    # Fill the background colour to the screen
    screen.fill(constants.WATER_COLOR)

    # Update the display using flip
    pg.display.flip()

    return screen


##################
# MAIN GAME LOOP #
##################


def main():

    screen = setup_window()

    #

    # dummy_tile = Tile(1, 2)
    # dummy_tile.reset_before_game()
    # screen.blit(dummy_tile.display_surface, (100, 100))

    dummy_game_board = GameBoard()
    for rc in range(constants.GAME_BOARD_COLUMNS):
        dummy_game_board.matrix[rc][rc].on_hit()

    dummy_game_board.update_display_surface()

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

            # if event.type == pg.KEYDOWN:
            #     if event.key == pg.K_j:
            #         dummy_tile.on_hit()
            #         screen.blit(dummy_tile.display_surface, (100, 100))
            #     elif event.key == pg.K_k:
            #         dummy_tile.reset_before_game()
            #         screen.blit(dummy_tile.display_surface, (100, 100))

        screen.blit(dummy_game_board.display_surface,
                    (constants.HORIZONTAL_BORDER_SIZE, 80))
        screen.blit(
            dummy_game_board.display_surface,
            (constants.HORIZONTAL_BORDER_SIZE * 2 + constants.GAME_BOARD_COLUMNS *
             constants.TILE_WIDTH, 80))

        # Update the display
        pg.display.flip()


if __name__ == "__main__":
    main()
