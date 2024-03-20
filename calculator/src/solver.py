from math import sin, cos, tan, log2, log, e

EPS = 1e-8


class Arithmetics:
    def __init__(self, expression=None):
        self._stack = []
        self._expression = expression
        self._operations = {
            '+': self._sum,
            '-': self._subtract,
            '*': self._multiply,
            '/': self._divide,
            '^': self._expo,
            'sin': self._sin,
            'cos': self._cos,
            'tan': self._tan,
            'cot': self._cot,
            'log': self._log,
            'ln': self._ln,
            'exp': self._e,
            'UM': self._UM
        }

    def _reset(self):
        self._stack = []
        self._expression = []

    def _sum(self):
        self._stack[-2] = self._stack[-2] + self._stack[-1]
        del self._stack[-1]

    def _subtract(self):
        self._stack[-2] = self._stack[-2] - self._stack[-1]
        del self._stack[-1]

    def _multiply(self):
        self._stack[-2] = self._stack[-2] * self._stack[-1]
        del self._stack[-1]

    def _divide(self):
        self._stack[-2] = self._stack[-2] / self._stack[-1]
        del self._stack[-1]

    def _expo(self):
        if abs(self._stack[-1]) <= EPS:
            self._stack[-2] = 1
        elif abs(self._stack[-2]) <= EPS:
            self._stack[-2] = 0
        else:
            sign = int(abs(self._stack[-2]) / self._stack[-2])
            self._stack[-2] = abs(self._stack[-2]) ** self._stack[-1] * sign
        del self._stack[-1]

    def _sin(self):
        self._stack[-1] = sin(self._stack[-1])

    def _cos(self):
        self._stack[-1] = cos(self._stack[-1])

    def _tan(self):
        self._stack[-1] = tan(self._stack[-1])

    def _cot(self):
        self._stack[-1] = 1 / (tan(self._stack[-1]))

    def _log(self):
        self._stack[-1] = log2(self._stack[-1])

    def _ln(self):
        self._stack[-1] = log(self._stack[-1])

    def _e(self):
        self._stack[-1] = e ** self._stack[-1]

    def _UM(self):
        self._stack[-1] = -1 * self._stack[-1]

    def solve(self, equation=False):
        if equation:
            self._expression = equation

        for item in self._expression:
            if isinstance(item, float) or item == 0:
                self._stack.append(item)
            else:
                self._operations[item]()

        answer = self._stack[-1]

        self._reset()

        return answer


class Function(Arithmetics):
    def __init__(self):
        super().__init__()


class Equation:
    def __init__(self, equation):
        self._base_equation = equation

        self.solver = Arithmetics()
        self._substituted = None

        self._left_bound = None
        self._right_bound = None

        self._opposite_signs = None

    def set_equation(self, equation):
        self._base_equation = equation

    def _substitute(self, value):
        self._substituted = self._base_equation.copy()

        for elem_id, elem in enumerate(self._substituted):
            if elem == 'x':
                self._substituted[elem_id] = value

    def _find_value_of(self, value):
        self._substitute(value)
        return self.solver.solve(equation=self._substituted)

    def F(self, x):
        return self._find_value_of(x)

    def find_solution(self, left_bound, right_bound):
        ...  # to be done




