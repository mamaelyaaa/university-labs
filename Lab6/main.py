from random import uniform


def monte_carlo(n: int) -> float:
    """Находим число pi, через площадь круга с радиусом 1"""

    m: int = 0  # Счетчик точек которые попали в фигуру
    r: int = 1  # Радиус окружности

    # Обозначим границы
    x_left, x_right = -r, r
    y_left, y_right = -r, r

    a: float = abs(x_left - x_right)  # Сторона описанного квадрата

    for i in range(n):
        rand_x: float = uniform(x_left, x_right)
        rand_y: float = uniform(y_left, y_right)

        m += f(rand_x, rand_y)

    s: float = a ** 2 * (m / n)

    return s


def f(x: float, y: float) -> bool:
    return x ** 2 + y ** 2 <= 1


def main() -> int:
    with open('data.txt', 'w') as data_file:
        n: list[int] = [5000, 1000, 25000, 50000, 100_000, 200_000, 500_000, 1_000_000]

        for i in n:
            print(f'{i} {monte_carlo(i)}', file=data_file)

    return 0


if __name__ == '__main__':
    main()
