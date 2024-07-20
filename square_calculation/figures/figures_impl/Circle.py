import math
import numbers

from square_calculation.figures.Figure import Figure


class Circle(Figure):
    def __init__(self, radius: float):
        self.validate_arguments(radius)
        self.radius = radius
        self.Square = math.pi * self.radius**2

    def validate_arguments(self, *args) -> None:
        super().validate_arguments(*args)

    def get_square(self) -> float:
        return self.Square

    def __str__(self) -> str:
        return (f"\n{super().__str__()}"
                f"\nradius={self.radius}")
