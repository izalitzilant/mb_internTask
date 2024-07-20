import numbers
from abc import ABC, abstractmethod

from square_calculation.figures.PlaneFigure import PlaneFigure


class Figure(ABC, PlaneFigure):
    @abstractmethod
    def validate_arguments(self, *args) -> None:
        """Figure accepts only postive numeric types"""
        for arg in args:
            if not isinstance(arg, numbers.Number):
                raise TypeError(f'Argument {arg} is not a number')
            if arg <= 0:
                raise ValueError("Argument must be greater than zero")

    @abstractmethod
    def __str__(self) -> str:
        """String representation of Figure"""
        f_type = self.__class__.__name__
        return (f"\n{f_type}"
                f"\nsquare={self.get_square()}")
