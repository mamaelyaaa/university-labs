from math import atan

# Границы интервала
A: float = 0
B: float = 2

# Погрешность
E: float = 0.005


def f(x: float) -> float:
    return x ** 2 + 1 / atan(x)


def f1(x: float) -> float:
    return 2 * x - 1 / ((x ** 2 + 1) * atan(x) ** 2)


def f2(x: float) -> float:
    return 2 + 2 * x * atan(x) + 2 / ((x ** 4 + 2 * x ** 2 + 1) * atan(x) ** 3)


def method_golden_section() -> None:
    with open('output.txt', 'w', encoding='utf-8') as output_file:
        golden_ratio = (1 + 5 ** 0.5) / 2
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

        print(f'Метод золотого сечения: {(a + b) / 2:.5f}', file=output_file)


def method_polyline() -> None:
    pass


def method_tangents() -> None:
    with open('output.txt', 'a', encoding='utf-8') as output_file:
        x0: float = (A + B) / 2

        while abs(f(x0)) >= E:
            x1 = x0 - f(x0) / f1(x0)
            x0 = x1

        print(f'Метод касательных: {x0}', file=output_file)


def method_Newton() -> None:
    pass


def main() -> None:
    method_golden_section()
    method_polyline()
    method_tangents()
    method_Newton()
    pass


if __name__ == '__main__':
    main()
