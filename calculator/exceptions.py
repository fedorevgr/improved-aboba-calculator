class NoArgsException(Exception):
    def __init__(self, expression):
        super().__init__(f'Can not end with operator or function without arguments\n'
                         f'{expression}\n{"^":~>{len(expression)}}')


class NoClosureBracket(Exception):
    def __init__(self, expression, error):
        super().__init__(f'Bracket not closed, expected ")"\n{expression}\n'
                         f'{"^":~>{error}}{"":~{len(expression) - error}}')


class OperatorEnding(Exception):
    def __init__(self, expression):
        super().__init__(f'Can not end with operator or function without arguments\n'
                         f'{expression}\n{"^":~>{len(expression)}}')


class ParseError(Exception):
    def __init__(self, expression, where):
        super().__init__(f"Unknown token: {expression}\n{'^':~>{where}}")


class ExpectedError(Exception):
    def __init__(self, expression, expectation, where):
        super().__init__(f"Expected {expectation}, \n{expression}\n{'^':~>{where}}{'':~^{len(expression) - where}}")


class EmptyExpression(Exception):
    def __init__(self):
        super().__init__("Empty expression")


ParseExceptions = (ParseError, OperatorEnding, ExpectedError, EmptyExpression, NoArgsException, NoClosureBracket)


