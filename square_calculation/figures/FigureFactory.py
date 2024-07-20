from square_calculation.figures.Figures import Figures


class FigureFactory:
    @staticmethod
    def calculate_square(*args) -> float:
        arg_len = len(args)
        for f_type in Figures:
            if f_type.value.__init__.__code__.co_argcount - 1 == arg_len:
                return f_type.value(*args)
        raise ValueError(f"No shape found for {arg_len} arguments.")