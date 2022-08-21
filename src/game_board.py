import pygame as pg


class GameBoard():
    def __init__(self) -> None:
        self.display_surface = None

    def reset_before_game():
        pass

    def update_display_surface():
        pass


class Ship():
    def __init__(self, length) -> None:
        self.length = length
        self.tiles = []
        self.is_sunk = False
        self.display_surface = pg.Surface()

    def reset_before_game():
        pass


class Tile():
    def __init__(self, row, column) -> None:
        self.row = row
        self.column = column
        self.num_hits = 0
        self.display_surface = pg.Surface()

    def reset_before_game():
        pass
