from square_calculation.figures.FigureFactory import FigureFactory
from square_calculation.figures.figures_impl.Circle import Circle
from square_calculation.figures.figures_impl.Triangle import Triangle


class TestFigureFactory:
    def test_figurefactory_threearggiven_trianglereturned(self):
        assert isinstance(FigureFactory.calculate_square(4, 2, 3), Triangle)

    def test_figurefactory_onearggiven_circleereturned(self):
        assert isinstance(FigureFactory.calculate_square(5), Circle)
