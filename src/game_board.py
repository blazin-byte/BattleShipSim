import pygame as pg


class GameBoard():
    """ Positions will be a list of lists representing the coordinates of the the ships given by each bot"""

    def __init__(self, positions) -> None:
        self.matrix_of_tiles = []
        self.length = 8
        self.width = 8
        self.matrix = [
            [Tile(i, j) for i in len(self.width)] for j in len(self.length)
        ]

    def init_ships(positions):
        ships = []
        for coords in positions:
            ships.append(Ship(len(coords)))

# are all of your ships sunk
# Update ships positions
# pregame reset (reset ship coordinates, reset tiles states)

# Do I get the ship positions from the bot? Can I assume I'll just get my ship coordinates as a list from the bot?

    def all_sunk():
        for ship in self.ships:
            if ship.is_sunk == False:
                return False
        return True

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
        self.hit = False
        self.num_hits = 0

    def reset_before_game():
        pass
