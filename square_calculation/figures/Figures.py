from enum import Enum

from square_calculation.figures.figures_impl.Circle import Circle
from square_calculation.figures.figures_impl.Triangle import Triangle


class Figures(Enum):
    TRIANGLE = Triangle
    CIRCLE = Circle
