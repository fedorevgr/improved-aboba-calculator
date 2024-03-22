from calculator.src.lexer import Lexer
from calculator.src.polish_notation_converter import Converter
from calculator.src.solver import Equation


class Interface:
    def __init__(self):
        self.lexer = Lexer()
        self.converter = Converter()
        self.solver = Equation(None)

        self._parsed_expression = ""
        self._function = []

    def set_expression(self, expression: str):
        self._parsed_expression = self.lexer.parse(expression)

        self._function = self.converter.convert(self._parsed_expression)

        self.solver.set_equation(self._function)

    def solve(self, x: float) -> float:
        return self.solver.F(x)

