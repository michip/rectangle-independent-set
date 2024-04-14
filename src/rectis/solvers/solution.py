from dataclasses import dataclass
from typing import List

from rectis.geometry.rectangle import Rectangle


@dataclass
class IndependentSetSolution:
    indices: List[int]
    independent_set: List[Rectangle]
    objective_value: float
    best_bound: float
    optimal: bool
    elapsed_time: float = 0

    @classmethod
    def from_dict(cls, data):
        return cls(
            indices=data["indices"],
            independent_set=[Rectangle(**rect) for rect in data["independent_set"]],
            objective_value=data["objective_value"],
            best_bound=data["best_bound"],
            optimal=data["optimal"],
            elapsed_time=data["elapsed_time"]
        )

    def to_dict(self):
        return {
            "indices": self.indices,
            "objective_value": self.objective_value,
            "best_bound": self.best_bound,
            "optimal": self.optimal,
            "independent_set": [rect.to_dict() for rect in self.independent_set],
            "elapsed_time": self.elapsed_time
        }

    def plot(self, ax):
        for rect in self.independent_set:
            rect.plot(ax, facecolor='#0000ff44', edgecolor='black', add_points=False)
        ax.set_title(f"Obj= {round(self.objective_value, 2)}, "
                     f"Bound= {round(self.best_bound, 2)} "
                     f"({round(self.elapsed_time, 2)}s)")
