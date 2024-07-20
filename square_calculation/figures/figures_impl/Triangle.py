import math
import numbers

from square_calculation.figures.Figure import Figure


class Triangle(Figure):
    def __init__(self, side_1: float, side_2: float, side_3: float) -> None:
        self.validate_arguments(side_1, side_2, side_3)
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3

        self.is_equaliteral = False
        if side_1 == side_2 and side_2 == side_3:
            self.is_equaliteral = True

    def validate_arguments(self, *args):
        """Check if triangle rule inequality holds"""
        super().validate_arguments(*args)
        if (args[0] >= sum([args[1], args[2]]) or
            args[1] >= sum([args[0], args[2]]) or
            args[2] >= sum([args[0], args[1]])):
            raise ValueError(f'Triange inequality doesnt hold')

    def get_square(self, ) -> float:
        p = sum([self.side_1, self.side_2, self.side_3]) / 2
        square = math.sqrt(p * (p - self.side_1) * (p - self.side_2) * (p - self.side_3))
        return square

    def __str__(self) -> str:
        return (f"\n{super().__str__()}"
                f"\nis_equaliteral={self.is_equaliteral}"
                f"\nside_1={self.side_1}"
                f"\nside_2={self.side_2}"
                f"\nside_3={self.side_3}")