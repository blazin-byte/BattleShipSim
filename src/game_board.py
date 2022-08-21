import pygame as pg


class GameBoard():
    def __init__(self) -> None:
        pass

    def reset_before_game():
        pass


class Ship():
    def __init__(self, length) -> None:
        self.length = length
        self.tiles = []
        self.is_sunk = False

    def reset_before_game():
        pass


class Tile():
    def __init__(self, row, column) -> None:
        self.row = row
        self.column = column
        self.num_hits = 0

    def reset_before_game():
        pass
