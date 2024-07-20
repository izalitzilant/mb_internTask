from figures.FigureFactory import FigureFactory


if __name__ == '__main__':
    print(FigureFactory.get_impl(2, 3, 4))
    print(FigureFactory.get_impl(5))
