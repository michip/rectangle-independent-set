from shapely import Polygon
from shapely.plotting import plot_polygon


class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.shapely_polygon = self.to_shapely()

        assert self.w > 0
        assert self.h > 0

    def to_dict(self):
        return {
            "x": self.x,
            "y": self.y,
            "w": self.w,
            "h": self.h
        }

    @property
    def x2(self):
        return self.x + self.w

    @property
    def y2(self):
        return self.y + self.h

    def intersects(self, other):

        if self.x > other.x + other.w or self.x + self.w < other.x:
            return False

        if self.y > other.y + other.h or self.y + self.h < other.y:
            return False

        return True

    def to_shapely(self):
        return Polygon([
            (self.x, self.y),
            (self.x + self.w, self.y),
            (self.x + self.w, self.y + self.h),
            (self.x, self.y + self.h)])

    def plot(self, ax, **kwargs):
        plot_polygon(self.shapely_polygon, ax=ax, **kwargs)
