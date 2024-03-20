class Converter:
    def __init__(self):
        self._weights = {
            '(': 1,
            '+': 2,
            '-': 2,
            '*': 3,
            '/': 3,
            '^': 4,
            'sin': 4,
            'cos': 4,
            'tan': 4,
            'cot': 4,
            'log': 4,
            'ln': 4,
            'exp': 4,
            'UM': 4
        }

        self.operations = ['+', '-', '*', '/', '^']

        self.functions = ['sin', 'cos', 'tan', 'cot', 'log', 'ln', 'UM', 'exp']

    def convert(self, expression):
        stack = []
        output = []
        for token in expression:
            if isinstance(token, float) or token == 'x':
                output.append(token)
            else:
                if not stack:
                    stack.append(token)
                    continue

                if token in self.functions:
                    stack.append(token)

                elif token == '(':
                    stack.append(token)

                elif token == ')':
                    while stack[-1] != "(":
                        output.append(stack.pop())
                    stack.pop()

                elif token in self.operations:

                    if self._weights[stack[-1]] >= self._weights[token]:
                        while stack and self._weights[stack[-1]] >= self._weights[token]:
                            output.append(stack.pop())

                    stack.append(token)

        while stack:
            output.append(stack.pop())

        return output






