import curses
from curses.textpad import rectangle
from .grid import Grid, GridDimensions, Vector2D


class TileLayer:
    def __init__(self) -> None:
        self.stdscr = curses.initscr()
        self.gridDimensions: GridDimensions = GridDimensions(
            width=curses.LINES, height=curses.COLS
        )
        self.layer: Grid = Grid(self.gridDimensions)

    def addTile(
        self, topLeftVector: Vector2D, bottomRightVector: Vector2D, zoneNumber=1
    ):
        tileDimensions = self.layer.addTiledZone(
            topLeftVector, bottomRightVector, zoneNumber
        )

        rectangle(
            self.stdscr,
            tileDimensions[0].x,
            tileDimensions[0].y,
            tileDimensions[1].x,
            tileDimensions[1].x,
        )

    def eventloop(self):
        self.stdscr.getch()
        self.stdscr.endwin()
        for i in self.layer.grid:
            print(i)
