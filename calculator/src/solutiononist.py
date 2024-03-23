from sympy import sympify, Derivative, Symbol, lambdify, diff


def iterate(x_k_1: float, point: tuple, eps, max_iter, func: callable, der: callable):
    code = 1

    x_k = point[0] - (point[1] / der(point[0]))
    i = 0
    try:
        while i < max_iter:
            alpha = -func(x_k) / der(x_k)

            if abs(alpha) < eps:
                code = 0
                break

            x_k = x_k + alpha

            i += 1
    except ZeroDivisionError:
        code = 2

    return f"[{x_k_1:g}, {point[0]:g}]", x_k, func(x_k), i, code


def get_derivative(function):
    x = Symbol("x")
    derivative = diff(sympify(function), x)
    return lambdify(x, derivative)


