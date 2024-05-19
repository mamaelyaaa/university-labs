from math import atan

# Границы интервала
A: float = 0
B: float = 2

# Погрешность
E: float = 0.005

# Просчитанный результат
answer: float = 0.757


def f(x: float) -> float:
    return x ** 2 + 1 / atan(x)


def df(x: float) -> float:
    return 2 * x - 1 / ((x ** 2 + 1) * atan(x) ** 2)


def d2f(x: float) -> float:
    return 2 + 2 * x * atan(x) + 2 / ((x ** 4 + 2 * x ** 2 + 1) * atan(x) ** 3)


def method_golden_section() -> None:
    with open('output.txt', 'w', encoding='utf-8') as output_file:
        golden_ratio: float = (1 + 5 ** 0.5) / 2
        a, b = A, B

        # Выбор начальных точек
        x1 = b - (b - a) / golden_ratio
        x2 = a + (b - a) / golden_ratio

        while abs(b - a) > E:
            if f(x1) < f(x2):
                b = x2
            else:
                a = x1

            x1 = b - (b - a) / golden_ratio
            x2 = a + (b - a) / golden_ratio

        print(f'Метод золотого сечения: {(a + b) / 2:.5f}, погрешность: {abs(answer - (a + b) / 2):.5f}',
              file=output_file)


def method_polyline() -> None:

    def delta(l: float, x: float, p: float) -> float:
        return 1 / (2 * l) * (f(x) - p)

    with open('output.txt', 'a', encoding='utf-8') as output_file:
        L = 0
        h = 0.0001

        for x in range(int(B), int(A), -1):
            L = max(abs((f(x + h) - f(x)) / h), L)

        x: float = 1 / (2 * L) * (f(B) + L * (A + B))
        p: float = (f(B) + L * (A - B)) / 2

        x1: list = [x - delta(L, x, p), x - delta(L, x, p)]
        p1: float = (f(x1[0]) + p) / 2

        x_min: float = x1[0] if f(x1[0]) < f(x1[1]) else x1[1]

        while abs(f(x) - f(x_min)) >= E:
            x1 = [x - delta(x, p, L), x + delta(x, p, L)]
            p1 = (f(x1[0]) - p) / 2

            x_min = x1[0] if f(x1[0]) < f(x1[1]) else x1[1]

            x = x_min
            p = p1

        print(f'Метод ломанных:         {x_min:.5f}, погрешность: {abs(answer - x_min):.5f}', file=output_file)


def method_tangents() -> None:
    with open('output.txt', 'a', encoding='utf-8') as output_file:
        x0 = A
        if x0 == 0:
            x0 = B

        x1 = x0 - f(x0) / df(x0)

        while abs(x1 - x0) < E:
            x1 = x0 - f(x0) / df(x0)
            x0 = x1

        print(f'Метод касательных:      {x1:.5f}, погрешность: {abs(answer - x1):.5f}', file=output_file)


def method_Newton() -> None:
    with open('output.txt', 'a', encoding='utf-8') as output_file:
        x0 = A
        if x0 == 0:
            x0 = B

        while abs(df(x0)) > E:
            x1 = x0 - (df(x0) / d2f(x0))
            x0 = x1

        print(f'Метод Ньютона:          {x0:.5f}, погрешность: {abs(answer - x0):.5f}', file=output_file)


def main() -> None:
    method_golden_section()
    method_polyline()
    method_tangents()
    method_Newton()
    pass


if __name__ == '__main__':
    main()
