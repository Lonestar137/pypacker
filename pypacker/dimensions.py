class GridDimensions:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    def __str__(self) -> str:
        return f"Grid Dimensions X: {self.width}, Y: {self.height}"
