from typing import Tuple, List
from .vector import Vector2D
from .dimensions import GridDimensions


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
    ) -> Tuple[Vector2D, Vector2D]:
        vectors = (topLeftVector, bottomRightVector)
        print(vectors)
        minX = min(v.x for v in vectors)
        maxX = max(v.x for v in vectors)
        minY = min(v.y for v in vectors)
        maxY = max(v.y for v in vectors)

        validVectors: List[Tuple] = []
        for y in range(maxY - minY + 1):
            for x in range(maxX - minX + 1):
                try:
                    valueAtIndex = self.grid[topLeftVector.y + y][topLeftVector.x + x]
                    currentVector = ((topLeftVector.y + y), (topLeftVector.x + x))
                    if valueAtIndex == 0:
                        self.grid[topLeftVector.y + y][topLeftVector.x + x] = zoneNumber

                        validVectors.append(currentVector)

                except IndexError as e:
                    pass

        # Get actual dimensions of tile after collision check
        newMinX = min(v[1] for v in validVectors)
        newMaxX = max(v[1] for v in validVectors)
        newMinY = min(v[0] for v in validVectors)
        newMaxY = max(v[0] for v in validVectors)
        appliedTopLeftVector = Vector2D(newMinX, newMinY)
        appliedBottomRightVector = Vector2D(newMaxX, newMaxY)

        appliedVectors: Tuple[Vector2D, Vector2D] = (
            appliedTopLeftVector,
            appliedBottomRightVector,
        )

        return appliedVectors
