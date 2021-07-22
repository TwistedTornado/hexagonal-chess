class PixelCoord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return PixelCoord(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return PixelCoord(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return PixelCoord(self.x * other, self.y * other)

    def __truediv__(self, other):
        return PixelCoord(self.x / other, self.y / other)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
