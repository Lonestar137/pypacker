import curses

# from curses import wrapper
from curses.textpad import rectangle
from .grid import Grid, GridDimensions, Vector2D


class TileLayer:
    def __init__(self) -> None:
        self.stdscr = curses.initscr()
        self.gridDimensions: GridDimensions = GridDimensions(
            width=curses.COLS, height=curses.LINES
        )
        # self.layer = Grid(GridDimensions(20, 20))
        self.layer: Grid = Grid(self.gridDimensions)

        curses.noecho
        curses.curs_set(0)

    def addTile(
        self, topLeftVector: Vector2D, bottomRightVector: Vector2D, zoneNumber=1
    ):
        tileDimensions = self.layer.addTiledZone(
            topLeftVector, bottomRightVector, zoneNumber
        )

        rectangle(
            self.stdscr,
            tileDimensions[0].y,
            tileDimensions[0].x,
            tileDimensions[1].y,
            tileDimensions[1].x,
        )

    def eventloop(self):
        self.stdscr.getch()
        curses.nocbreak()
        curses.endwin()
        print(self.layer.gridDimensions)

        for i in self.layer.grid:
            print(i)
