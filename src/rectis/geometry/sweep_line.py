from typing import List

from tqdm import tqdm

from rectis.geometry.rectangle import Rectangle


def _intersection_sweep(rectangles: List[Rectangle], method):
    # sort the rectangles by x coordinate
    # we don't care about the order of start and end as intersections along an edge are not considered
    events = list(sorted(
        [(rect.x, i, "start") for i, rect in enumerate(rectangles)] +
        [(rect.x2, i, "end") for i, rect in enumerate(rectangles)], key=lambda t: t[0]))

    active_rectangles = set()
    for _, i, action in tqdm(events):
        if action == "end":
            active_rectangles.remove(i)
            continue

        # action == "start", new rectangle was added to the active set
        for j in active_rectangles:
            if method == "fast" and rectangles[i].intersects(rectangles[j]):
                yield (i, j) if i < j else (j, i)
            elif method == "shapely" and rectangles[i].shapely_polygon.intersection(rectangles[j].shapely_polygon).area > 0:
                yield (i, j) if i < j else (j, i)

        active_rectangles.add(i)


def intersection_sweep_line(rectangles: List[Rectangle], method="fast"):
    """
    Runs a sweep line algorithm to find all intersections between rectangles.
    :param rectangles:
    :return:
    """
    return list(_intersection_sweep(rectangles, method=method))
