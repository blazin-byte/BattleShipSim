import pygame as pg
from . import constants, game_board


class GameServer():
    def __init__(self) -> None:
        self.display_surface = pg.Surface(
            (2 * constants.GAME_BOARD_COLUMNS * constants.TILE_WIDTH + constants.
             HORIZONTAL_BORDER_SIZE + 4 * constants.GAME_BOARD_OUTER_BORDER,
             constants.GAME_BOARD_ROWS * constants.TILE_HEIGHT + 2 * constants.GAME_BOARD_OUTER_BORDER),
            flags=pg.SRCALPHA)

        self.game_boards = [
            game_board.GameBoard(),
            game_board.GameBoard()
        ]

    def update_display_surface(self):
        # Clear the display surface
        self.display_surface.fill(constants.WATER_COLOR)

        # Update the display surfaces of both game boards
        for game_board in self.game_boards:
            game_board.update_display_surface()

        # Plot both game boards on the display surface

        # - Left
        self.display_surface.blit(
            self.game_boards[0].display_surface,
            (constants.GAME_BOARD_OUTER_BORDER, constants.GAME_BOARD_OUTER_BORDER))
        pg.draw.rect(self.display_surface, constants.TILE_COLOR, pg.Rect(
            0, 0, constants.GAME_BOARD_COLUMNS * constants.TILE_WIDTH + 2 *
            constants.GAME_BOARD_OUTER_BORDER, constants.GAME_BOARD_ROWS *
            constants.TILE_HEIGHT + 2 * constants.GAME_BOARD_OUTER_BORDER),
            constants.GAME_BOARD_OUTER_BORDER)

        # - Right
        self.display_surface.blit(self.game_boards[1].display_surface,
                                  (constants.HORIZONTAL_BORDER_SIZE + constants.GAME_BOARD_COLUMNS *
                                   constants.TILE_WIDTH + 3 * constants.GAME_BOARD_OUTER_BORDER, constants.GAME_BOARD_OUTER_BORDER))
        pg.draw.rect(self.display_surface, constants.TILE_COLOR, pg.Rect(
            constants.GAME_BOARD_COLUMNS * constants.TILE_WIDTH + 2 *
            constants.GAME_BOARD_OUTER_BORDER + constants.HORIZONTAL_BORDER_SIZE, 0, constants.GAME_BOARD_COLUMNS * constants.TILE_WIDTH + 2 *
            constants.GAME_BOARD_OUTER_BORDER, constants.GAME_BOARD_ROWS *
            constants.TILE_HEIGHT + 2 * constants.GAME_BOARD_OUTER_BORDER),
            constants.GAME_BOARD_OUTER_BORDER)
