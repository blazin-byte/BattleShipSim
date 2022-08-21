from .src import game_board, game_server
import pygame as pg


def main():

    background_colour = (234, 212, 252)
    # Define the dimensions of
    # screen object(width,height)
    screen = pg.display.set_mode((1200, 600))

    # Set the caption of the screen
    pg.display.set_caption('Geeksforgeeks')

    # Fill the background colour to the screen
    screen.fill(background_colour)

    # Update the display using flip
    pg.display.flip()

    # Variable to keep our game loop running
    running = True

    # game loop
    while running:

        # for loop through the event queue
        for event in pg.event.get():

            # Check for QUIT event
            if event.type == pg.QUIT:
                running = False


if __name__ == "__main__":
    main()
