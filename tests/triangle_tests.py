from typing import List

import pytest

from square_calculation.figures.figures_impl.Triangle import Triangle


class TestTriangle:
    @pytest.mark.parametrize("test_input, expected", [([5, 4, 3], 6), ([10, 8, 6], 24)])
    def test_triangle_getsquare(self, test_input: List[float], expected: float) -> None:
        side1, side2, side3 = test_input
        triangle = Triangle(side1, side2, side3)
        assert triangle.get_square() == expected

    def test_triangle_nonnumeric_raises(self) -> None:
        with pytest.raises(TypeError):
            Triangle("str1", "str2", "str3")

    def test_triangle_negative_raises(self) -> None:
        with pytest.raises(ValueError):
            Triangle(-1, -1, -1)

    def test_triangle_inequality_raises(self) -> None:
        with pytest.raises(ValueError):
            Triangle(100, 1, 2)
