from pathlib import Path

from rectis.solvers.solvers import execute_cp_sat, execute_gurobi
from rectis.geometry.sweep_line import intersection_sweep_line
from rectis.utils.parser import read_instance

import numpy as np


def test_same_solution():
    for instance in [
        Path(__file__).parent / "instances" / "medium.csv",
        Path(__file__).parent / "instances" / "medium2.csv"
    ]:
        rectangles = read_instance(instance)
        intersections = intersection_sweep_line(rectangles)

        cp_sat_solution = execute_cp_sat(rectangles, intersections, timeout=60)
        gurobi_solution = execute_gurobi(rectangles, intersections, timeout=60)

        assert gurobi_solution.optimal
        assert cp_sat_solution.optimal
        assert gurobi_solution.objective_value == cp_sat_solution.objective_value
        assert gurobi_solution.best_bound == cp_sat_solution.best_bound
        assert len(gurobi_solution.indices) == gurobi_solution.objective_value
        assert len(cp_sat_solution.indices) == cp_sat_solution.objective_value


def test_timeout():
    path = Path(__file__).parent / "instances" / "large.csv"
    rectangles = read_instance(path)
    intersections = intersection_sweep_line(rectangles)

    timeout = 1

    cp_sat_solution = execute_cp_sat(rectangles, intersections, timeout=timeout)
    gurobi_solution = execute_gurobi(rectangles, intersections, timeout=timeout)

    assert np.isclose(gurobi_solution.elapsed_time, timeout, atol=1), gurobi_solution.elapsed_time
    assert np.isclose(cp_sat_solution.elapsed_time, timeout, atol=1), cp_sat_solution.elapsed_time
