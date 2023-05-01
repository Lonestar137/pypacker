from types import Tuple


class Tile:
    def __init__(
        self, grid, top_vector: Tuple[int, int], bottom_vector: Tuple[int, int]
    ) -> None:
        vectors: Tuple[Tuple[int, int], Tuple[int, int]] = (top_vector, bottom_vector)
        showOutline: bool = False
        allowSubTiles: bool = False
        subarray = [[]]

    def addTile(self):
        pass

    def getSubRectangle(self):
        minX = min(v[0] for v in self.vectors)
        maxX = max(v[0] for v in self.vectors)
        minY = min(v[1] for v in self.vectors)
        maxY = max(v[1] for v in self.vectors)

        # 2D list of zeros, same size as tile
        subarray = [[0 for j in range(maxY - minX + 1)] for i in range(maxY - minY + 1)]

        self.subarray = subarray


class ListTile(Tile):
    def __init__(self) -> None:
        super().__init__()
        pass


class MeterTile(Tile):
    # Meter tile, filled by percentage
    def __init__(self) -> None:
        # var style
        # var title
        super().__init__()
        pass


class ASCITile(Tile):
    def __init__(self) -> None:
        super().__init__()
