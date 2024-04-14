from pathlib import Path
from rectis.utils.parser import read_instance


def test_parse_json():
    rectangles = read_instance(Path(__file__).parent / "instances" / "tiny.json")

    assert len(rectangles) == 2
    assert rectangles[0].x == 0
    assert rectangles[0].y == 0
    assert rectangles[0].w == 100
    assert rectangles[0].h == 100
    assert rectangles[1].x == 100
    assert rectangles[1].y == 100
    assert rectangles[1].w == 100
    assert rectangles[1].h == 100


def test_parse_csv():
    rectangles = read_instance(Path(__file__).parent / "instances" / "tiny.csv")

    assert len(rectangles) == 2
    assert rectangles[0].x == 0
    assert rectangles[0].y == 0
    assert rectangles[0].w == 100
    assert rectangles[0].h == 100
    assert rectangles[1].x == 100
    assert rectangles[1].y == 100
    assert rectangles[1].w == 100
    assert rectangles[1].h == 100
