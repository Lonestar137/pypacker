from typing import Tuple


class Tile:
    def __init__(
        self, grid, top_vector: Tuple[int, int], bottom_vector: Tuple[int, int]
    ) -> None:
        showOutline: bool = False
        allowSubTiles: bool = False


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
