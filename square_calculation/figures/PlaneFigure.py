from typing import Protocol


class PlaneFigure(Protocol):
    def get_square(self) -> float: ...
