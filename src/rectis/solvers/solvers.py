from typing import List, Tuple

from ortools.sat.python import cp_model
import gurobipy as gp
from gurobipy import GRB

from rectis.geometry.rectangle import Rectangle
from rectis.geometry.sweep_line import intersection_sweep_line
from rectis.solvers.solution import IndependentSetSolution


def execute_cp_sat(rectangles: List[Rectangle],
                   intersections: List[Tuple[int, int]],
                   timeout):
    model = cp_model.CpModel()
    x = [model.NewBoolVar(name=f"x{i}") for i in range(len(rectangles))]

    for i, j in intersections:
        model.AddBoolOr(x[i].Not(), x[j].Not())

    model.Maximize(sum(x))

    solver = cp_model.CpSolver()
    solver.parameters.log_search_progress = True
    solver.parameters.max_time_in_seconds = timeout

    status = solver.Solve(model)
    values = [solver.Value(x[i]) for i in range(len(rectangles))]

    return IndependentSetSolution(
        indices=[i for i, v in enumerate(values) if v],
        independent_set=[rectangles[i] for i, v in enumerate(values) if v],
        objective_value=solver.ObjectiveValue(),
        best_bound=solver.BestObjectiveBound(),
        optimal=status == cp_model.OPTIMAL,
        elapsed_time=solver.WallTime()
    )


def execute_gurobi(rectangles: List[Rectangle],
                   intersections: List[Tuple[int, int]],
                   timeout: int):
    model = gp.Model("rectangle_independent_set")
    rect_vars = model.addVars(len(rectangles), vtype=GRB.BINARY, name="x")

    model.addConstrs((rect_vars[i] + rect_vars[j] <= 1 for i, j in intersections), name=f"no_intersect")

    model.setObjective(rect_vars.sum(), GRB.MAXIMIZE)
    model.Params.TimeLimit = timeout

    model.optimize()

    return IndependentSetSolution(
        indices=[i for i in rect_vars if rect_vars[i].x > 0.5],
        independent_set=[rectangles[i] for i in rect_vars if rect_vars[i].x > 0.5],
        objective_value=model.objVal,
        best_bound=model.objBound,
        optimal=model.status == GRB.OPTIMAL,
        elapsed_time=model.Runtime
    )


def run_solver(solver: str, rectangles: List[Rectangle], timeout: int = 900):
    intersections = list(intersection_sweep_line(rectangles))

    if solver == "cp-sat":
        return execute_cp_sat(rectangles, intersections, timeout)
    elif solver == "ip":
        return execute_gurobi(rectangles, intersections, timeout)
    else:
        raise ValueError(f"Unknown solver {solver}")
