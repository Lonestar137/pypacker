from vector import Vector2D
from dimensions import GridDimensions


class Grid:
    def __init__(
        self,
        gridDimensions: GridDimensions,
    ) -> None:
        self.gridDimensions = gridDimensions
        self.grid = self.createBlankGridFromDimensions()

    # Creates 2D grid of 0's from class or provided dimensions.
    def createBlankGridFromDimensions(self, customDimensions: GridDimensions = None):
        array = []
        if customDimensions == None:
            array = [
                [0 for y in range(self.gridDimensions.height)]
                for x in range(self.gridDimensions.width)
            ]
        else:
            array = [
                [0 for y in range(customDimensions.height)]
                for x in range(customDimensions.width)
            ]

        return array

    # Marks an area as being filled on class/provided grid.
    def addTiledZone(
        self,
        topLeftVector: Vector2D,
        bottomRightVector: Vector2D,
        zoneNumber: int = 1,
        customGrid=None,
    ):
        vectors = (topLeftVector, bottomRightVector)
        print(vectors)
        minX = min(v.x for v in vectors)
        maxX = max(v.x for v in vectors)
        minY = min(v.y for v in vectors)
        maxY = max(v.y for v in vectors)

        for y in range(maxY - minY + 1):
            for x in range(maxX - minX + 1):
                try:
                    self.grid[topLeftVector.y + y][topLeftVector.x + x] = zoneNumber
                except IndexError as e:
                    pass
