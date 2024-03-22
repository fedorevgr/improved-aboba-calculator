import string
from calculator.exceptions import *


class Lexer:
    _OPERATIONS = '+-*/^'

    def define_unary_minus(self):
        for elem_id in range(len(self._result) - 1):
            elem = self._result[elem_id]
            if elem == '-':
                if elem_id == 0:
                    self._result[elem_id] = 'UM'
                else:
                    previous_elem = self._result[elem_id - 1]
                    if previous_elem in list('()^+-*/'):
                        self._result[elem_id] = 'UM'

    def convert_numbers_from(self):
        for item_id in range(len(self._result)):
            item = self._result[item_id]
            try:
                item = float(item)
            except ValueError:
                continue
            self._result[item_id] = item

    def __init__(self):
        self._state = 'S'
        self._buffer = ''
        self._index = 0
        self._current_char = ''
        self._brackets_count = 0
        self.is_function = False
        self._result = []

        self._machine = {
            'S': self._state_s,  # default state
            'I': self._state_i,  # integer state
            'R': self._state_r,  # real number state
            'B': self._state_b,  # closing brackets state
            'F': self._state_f,  # function state
            'X': self._state_x   # variable state
        }

        self._expectations = {
            'S': 'number, letter, unary minus or opening bracket',
            'I': 'number, operator, comma or closing bracket',
            'R': 'number, operator or closing bracket',
            'B': 'operator or closing bracket',
            'F': 'letter or opening bracket',
            'X': 'closing bracket or operator',
            'B_ERR': 'right brackets count'
        }

    def _reset(self):
        self._state = 'S'
        self._buffer = ''
        self._index = 0
        self._current_char = ''
        self._brackets_count = 0
        self.is_function = False
        self._result = []

    def _flush_buffer(self):
        if self._buffer:
            self._result.append(self._buffer)
            self._buffer = ''

    def _add_char_to_buffer(self):
        self._buffer += self._current_char

    def _flush_current_char(self):
        self._result.append(self._current_char)

    def _state_s(self):  # from default to default, I, F or X
        if self._current_char.isdigit():
            self._add_char_to_buffer()
            return 'I'
        if self._current_char == '(':
            self._brackets_count += 1
            self._flush_current_char()
            return 'S'
        if self._current_char == '-':
            # self._add_char_to_buffer()
            self._flush_current_char()
            return 'S'

        if self._current_char in string.ascii_lowercase and self._current_char != 'x':
            self._add_char_to_buffer()
            return 'F'

        if self._current_char == 'x':
            self.is_function = True
            self._add_char_to_buffer()
            self._flush_buffer()
            return 'X'

    def _state_i(self):  # from integer to integer, real or brackets
        if self._current_char == '.':
            self._add_char_to_buffer()
            return 'R'

        if self._current_char.isdigit():
            self._add_char_to_buffer()
            return 'I'

        if self._current_char == ')':
            self._brackets_count -= 1
            self._flush_buffer()
            self._flush_current_char()
            return 'B'

        if self._current_char in self._OPERATIONS:
            self._flush_buffer()
            self._flush_current_char()
            return 'S'

    def _state_r(self):  # from real to continue real or end number input
        if self._current_char.isdigit():
            self._add_char_to_buffer()
            return 'I'

        if self._current_char == ')':
            self._brackets_count -= 1
            self._flush_buffer()
            self._flush_current_char()
            return 'B'

        if self._current_char in self._OPERATIONS:
            self._flush_buffer()
            self._flush_current_char()
            return 'S'

    def _state_b(self):
        if self._current_char == ')':
            self._brackets_count -= 1
            self._flush_current_char()
            return 'B'

        if self._current_char in self._OPERATIONS:
            self._flush_buffer()
            self._flush_current_char()
            return 'S'

    def _state_f(self):
        if self._current_char in string.ascii_lowercase:
            self._add_char_to_buffer()
            return 'F'

        if self._current_char == '(':
            self._brackets_count += 1
            self._flush_buffer()
            self._flush_current_char()
            return 'S'

    def _state_x(self):
        self.is_function = True

        if self._current_char == ')':
            self._flush_current_char()
            self._brackets_count -= 1
            return 'B'

        if self._current_char in self._OPERATIONS:
            self._flush_buffer()
            self._flush_current_char()
            return 'S'

    def parse(self, expression: str):
        if not expression:
            raise EmptyExpression

        for index, char in enumerate(expression):
            self._index = index
            self._current_char = char

            if self._state is None:
                self._reset()
                raise ParseError(expression, where=index)

            self._state = self._machine[self._state]()

        if self._state not in 'IBX':
            raise NoArgsException(expression)

        if self._brackets_count != 0:
            brackets = []
            if self._brackets_count > 0:
                for elem_id in range(len(expression)):
                    if expression[elem_id] == '(':
                        brackets.append(elem_id)
                    elif expression[elem_id] == ')':
                        brackets.pop()
            elif self._brackets_count < 0:
                for elem_id in range(len(expression), 0, -1):
                    if expression[elem_id] == ')':
                        brackets.append(elem_id)
                    elif expression[elem_id] == '(':
                        brackets.pop()

            error = brackets[-1]

            raise NoClosureBracket(expression, error)

        self._flush_buffer()

        self.convert_numbers_from()

        self.define_unary_minus()

        out = self._result.copy()

        self._reset()

        return out
