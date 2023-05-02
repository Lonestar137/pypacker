from typing import Tuple, List
from .vector import Vector2D
from .dimensions import GridDimensions


class Grid:
    def __init__(self, gridDimensions: GridDimensions) -> None:
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

        # newMinX = minX
        # newMaxX = maxX
        # newMinY = minY
        # newMaxY = maxY

        validVectors: List[Tuple] = []
        for y in range(minY - 1, maxY + 2):
            for x in range(minX - 1, maxY + 2):
                try:
                    valueAtIndex = self.grid[y][x]
                    currentVector = (y, x)

                    isInArea: bool = minX <= x <= maxX and minY <= y <= maxY

                    if isInArea and valueAtIndex == 0:
                        validVectors.append(currentVector)
                    elif valueAtIndex > 0:
                        center_y = (minY + maxY) // 2
                        center_x = (minX + maxX) // 2
                        if y < center_y:
                            minY -= 1
                            maxY -= 1
                        elif y > center_y:
                            minY += 1
                            maxY += 1

                        if x < center_x:
                            minX -= 1
                            maxX -= 1
                        elif x > center_x:
                            minX += 1
                            maxX += 1

                except IndexError as e:
                    pass

        # Get actual dimensions of tile after collision check
        newMinX = min(v[1] for v in validVectors)
        newMaxX = max(v[1] for v in validVectors)
        newMinY = min(v[0] for v in validVectors)
        newMaxY = max(v[0] for v in validVectors)
        appliedTopLeftVector = Vector2D(newMinX, newMinY)
        appliedBottomRightVector = Vector2D(newMaxX, newMaxY)

        for y in range(newMaxY - newMinY + 1):
            for x in range(newMaxX - newMinX + 1):
                try:
                    valueAtIndex = self.grid[appliedTopLeftVector.y + y][
                        appliedTopLeftVector.x + x
                    ]
                    currentVector = (
                        (appliedTopLeftVector.y + y),
                        (appliedTopLeftVector.x + x),
                    )
                    if valueAtIndex == 0:
                        self.grid[appliedTopLeftVector.y + y][
                            appliedTopLeftVector.x + x
                        ] = zoneNumber
                except IndexError as e:
                    pass

        appliedVectors: Tuple[Vector2D, Vector2D] = (
            appliedTopLeftVector,
            appliedBottomRightVector,
        )

        return appliedVectors
