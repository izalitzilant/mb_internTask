from figures.FigureFactory import FigureFactory


if __name__ == '__main__':
    figure_1 = FigureFactory.get_impl(2, 3, 4)
    figure_2 = FigureFactory.get_impl(5)
    print(figure_1.get_square(), figure_2.get_square())
