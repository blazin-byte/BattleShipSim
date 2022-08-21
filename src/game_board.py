import pygame as pg


class GameBoard():
    def __init__(self) -> None:
        """ Positions will be a list of lists representing the coordinates of the the ships given by each bot"""
        self.length = 8
        self.width = 8
        self.matrix = [
            [Tile(i, j) for i in range(self.width)] for j in range(self.length)
        ]
        self.display_surface = pg.Surface()

    def init_ships(self, positions):
        ships = []
        for coords in positions:
            # Might have to divide the length by 2
            curShip = Ship(len(coords))
            ships.append(curShip)
            for coord in coords:
                curShip.tiles.append(self.matrix(coord))


# are all of your ships sunk
# Update ships positions
# pregame reset (reset ship coordinates, reset tiles states)

# Do I get the ship positions from the bot? Can I assume I'll just get my ship coordinates as a list from the bot?


    def all_sunk(self):
        for ship in self.ships:
            if ship.is_sunk == False:
                return False
        return True

    def update_board(self, coord):
        self.matrix(coord).hit = True
        self.matrix(coord).num_hits += 1
        self.hit_ship(coord)

    def hit_ship(self, coord):
        for ship in self.ships:
            for tile in ship.tiles:
                if coord[0] == tile.row and coord[1] == tile.column:
                    self.sunk_ship(ship)

    def sunk_ship(self, ship):
        hit_check = True
        for tile in ship.tiles:
            if tile != self.matrix.tile:
                hit_check = False
        if hit_check:
            ship.is_sunk = True

    def reset_before_game():
        # You'll have to request the bots for new inputs
        pass

    def update_display_surface():
        pass


class Ship():
    def __init__(self, length, coords) -> None:
        self.length = length
        self.tiles = []
        self.is_sunk = False
        self.display_surface = pg.Surface()

    def reset_before_game():
        # TODO: Reset the display surface before a new game
        pass


TILE_SIZE = (25, 25)


class Tile():
    def __init__(self, row, column) -> None:
        self.row = row
        self.column = column
        self.hit = False
        self.num_hits = 0
        self.display_surface = pg.Surface(TILE_SIZE)

    def reset_before_game(self):
        # TODO: Reset the display surface before a new game
        self.display_surface.fill((0, 0, 0))
        pass

    def on_hit(self):
        self.display_surface.fill((255, 255, 255))

    # TODO: Update the display surface when a hit is detected
