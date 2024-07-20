import math

import pytest

from square_calculation.figures.figures_impl.Circle import Circle


class TestCircle:
    @pytest.mark.parametrize("test_input, expected", [(5, math.pi*25)])
    def test_circle_getsquare(self, test_input: float, expected: float) -> None:
        circle = Circle(test_input)
        assert circle.get_square() == expected

    def test_triangle_nonnumeric_raises(self) -> None:
        with pytest.raises(TypeError):
            Circle("1")

    def test_circle_negative_raises(self):
        with pytest.raises(ValueError):
            circle = Circle(-5)
            circle.get_square()
