import random as rd
from itertools import combinations
from pathlib import Path

from rectis.geometry.rectangle import Rectangle
from rectis.geometry.sweep_line import intersection_sweep_line
from rectis.utils.parser import read_instance


def test_interior_intersection():
    rectangle1 = Rectangle(0, 0, 4, 4)
    rectangle2 = Rectangle(1, 1, 2, 2)

    assert rectangle1.intersects(rectangle2)
    assert rectangle2.intersects(rectangle1)


def test_same_intersection():
    rectangle1 = Rectangle(0, 0, 4, 4)
    rectangle2 = Rectangle(0, 0, 4, 4)

    assert rectangle1.intersects(rectangle2)
    assert rectangle2.intersects(rectangle1)


def test_no_intersection():
    rectangle1 = Rectangle(0, 0, 2, 3)
    rectangle2 = Rectangle(3, 3, 2, 3)

    assert not rectangle1.intersects(rectangle2)
    assert not rectangle2.intersects(rectangle1)


def test_intersection():
    rectangle1 = Rectangle(0, 0, 2, 3)
    rectangle2 = Rectangle(1, 1, 2, 3)

    assert rectangle1.intersects(rectangle2)
    assert rectangle2.intersects(rectangle1)


def test_intersection_same_x():
    rectangle1 = Rectangle(0, 0, 2, 3)
    rectangle2 = Rectangle(2, 1, 2, 1)

    assert rectangle1.shapely_polygon.intersection(rectangle2.shapely_polygon).area <= 0

    assert not rectangle1.intersects(rectangle2)
    assert not rectangle2.intersects(rectangle1)


def test_intersection_edge():
    rectangle1 = Rectangle(0, 0, 2, 3)
    rectangle2 = Rectangle(2, 3, 2, 1)

    assert rectangle1.shapely_polygon.intersection(rectangle2.shapely_polygon).area <= 0

    assert not rectangle1.intersects(rectangle2)
    assert not rectangle2.intersects(rectangle1)


def test_sweep_line_intersections():
    rd.seed(42)
    rectangles = [
        Rectangle(rd.randint(0, 10), rd.randint(0, 10), rd.random() * 4, rd.random() * 5)
        for _ in range(100)
    ]

    all_intersections = [(i, j) for i in range(len(rectangles)) for j in range(i + 1, len(rectangles)) if
                         rectangles[i].intersects(rectangles[j])]
    sweep_line_intersections = list(intersection_sweep_line(rectangles))

    assert set(all_intersections) == set(sweep_line_intersections)


def test_intersections_with_shapely():
    rd.seed(4242)
    rectangles = [
        Rectangle(rd.randint(0, 10), rd.randint(0, 10), rd.random() * 4, rd.random() * 5)
        for _ in range(100)
    ]

    for i, j in combinations(range(len(rectangles)), 2):
        assert (rectangles[i].intersects(rectangles[j]) ==
                (rectangles[i].to_shapely().intersection(rectangles[j].to_shapely()).area > 0))


"""
def test_sweep_line_intersections_large():
    rd.seed(42)
    rectangles = read_instance(Path(__file__).parent / "instances" / "giant.csv")

    all_intersections = list(intersection_sweep_line(rectangles, method="shapely"))
    sweep_line_intersections = list(intersection_sweep_line(rectangles))

    assert set(all_intersections) == set(sweep_line_intersections)
"""
