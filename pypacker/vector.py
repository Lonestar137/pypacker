from typing import Tuple


class Vector2D:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def updateFromTuple(self, index: Tuple[int, int]):
        self.x = index[0]
        self.y = index[1]

    def __str__(self) -> str:
        return f"X: {self.x}, Y: {self.y}"
