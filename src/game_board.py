import pygame as pg
from . import constants


class GameBoard():
    def __init__(self) -> None:
        """ Positions will be a list of lists representing the coordinates of the the ships given by each bot"""
        self.ships = []
        self.matrix = [
            [Tile(row, col) for row in range(constants.GAME_BOARD_ROWS)]
            for col in range(constants.GAME_BOARD_COLUMNS)
        ]
        self.display_surface = pg.Surface(
            size=(constants.GAME_BOARD_ROWS * constants.TILE_WIDTH,
                  constants.GAME_BOARD_COLUMNS * constants.TILE_HEIGHT)
        )

    def init_ships(self, positions):
        self.ships = []
        for coords in positions:
            # Might have to divide the length by 2
            current_ship = Ship(len(coords))
            self.ships.append(current_ship)
            for coord in coords:
                current_ship.tiles.append(self.matrix(coord))


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

    def update_display_surface(self):
        # Clear the display surface
        self.display_surface.fill(constants.WATER_COLOR)

        # Plot each tile on the display surface
        for row in range(constants.GAME_BOARD_ROWS):
            for col in range(constants.GAME_BOARD_COLUMNS):
                current_tile_surface = self.matrix[row][col].display_surface
                x_coord_to_plot_at = row * constants.TILE_WIDTH
                y_coord_to_plot_at = col * constants.TILE_HEIGHT

                self.display_surface.blit(current_tile_surface, dest=(
                    x_coord_to_plot_at,
                    y_coord_to_plot_at
                ))


class Ship():
    def __init__(self, length, coords) -> None:
        self.length = length
        self.tiles = []
        self.is_sunk = False
        self.display_surface = pg.Surface()

    def reset_before_game():
        # TODO: Reset the display surface before a new game
        pass


class Tile():
    def __init__(self, row, column) -> None:
        self.row = row
        self.column = column
        self.hit = False
        self.num_hits = 0
        self.display_surface = pg.Surface(
            (constants.TILE_WIDTH, constants.TILE_HEIGHT),
            flags=pg.SRCALPHA)

        self.reset_before_game()

    def reset_before_game(self):
        self.display_surface.fill(constants.TRANSPARENT)
        pg.draw.rect(
            self.display_surface, constants.TILE_COLOR, pg.Rect(
                0, 0, constants.TILE_WIDTH, constants.TILE_HEIGHT))

    def on_hit(self):
        self.display_surface.fill(constants.TRANSPARENT)
        self.display_surface.fill((255, 255, 255))
