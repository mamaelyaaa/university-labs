def method_mnk(x_exp: list[float], y_exp: list[float]) -> None:
    def quadratic_func(x: float, a: float, b: float, c: float) -> float:
        return a * x ** 2 + b * x + c

    def method_gauss(slay_arr: list) -> list[int]:
        N: int = len(slay_arr)

        for i in range(N):
            pivot: float = slay_arr[i][i]

            for j in range(i, N + 1):
                slay_arr[i][j] /= pivot

            for k in range(i + 1, N):
                factor = slay_arr[k][i]

                for j in range(i, N + 1):
                    slay_arr[k][j] -= factor * slay_arr[i][j]

        x = [0] * N

        for i in range(N - 1, -1, -1):
            x[i] = slay_arr[i][-1]

            for j in range(i + 1, N):
                x[i] -= slay_arr[i][j] * x[j]

        return x

    with open('output.txt', 'w') as out_file:
        n: int = len(x_exp)

        # Промежуточные вычисления
        sum_x: float = sum(x_exp)
        sum_x2: float = sum(i ** 2 for i in x_exp)
        sum_x3: float = sum(i ** 3 for i in x_exp)
        sum_x4: float = sum(i ** 4 for i in x_exp)

        sum_y: float = sum(y_exp)
        sum_xy: float = sum(x_exp[i] * y_exp[i] for i in range(n))
        sum_x2y: float = sum(x_exp[i] ** 2 * y_exp[i] for i in range(n))

        # Создаем систему линейных уравнений для метода Гаусса
        slay: list[list] = [[], [], []]

        slay[0] = [sum_x2, sum_x, n, sum_y]
        slay[1] = [sum_x3, sum_x2, sum_x, sum_xy]
        slay[2] = [sum_x4, sum_x3, sum_x2, sum_x2y]

        # Нахождение коэффицента детерминации R
        sum_e = sum((y_exp[i] - quadratic_func(x_exp[i], *method_gauss(slay))) ** 2 for i in range(n))
        sum_y_bar = sum((y_exp[i] - 1 / n * sum_y) ** 2 for i in range(n))
        r = pow(1 - sum_e / sum_y_bar, 2)

        # Нахождение средней ошибки аппроксимации
        a = 1 / n * sum(abs((y_exp[i] - quadratic_func(x_exp[i], *method_gauss(slay))) / y_exp[i]) for i in range(n))

        print(f'Method MNK (quadratic): y = {method_gauss(slay)[0]:.4f}x^2 + {method_gauss(slay)[1]:.4f}x '
              f'{method_gauss(slay)[2]:.4f}', file=out_file)
        print(f'R = {r ** 2:.5f}', file=out_file)
        print(f'Approximate error: {a:.2%}\n', file=out_file)


def method_linear_regression(x_exp: list[float], y_exp: list[float]) -> None:

    def linear_func(x: float, b: float, k: float) -> float:
        return b + k * x

    with open('output.txt', 'a') as out_file:
        n: int = len(x_exp)

        # Промежуточные вычисления
        sum_x: float = sum(x_exp)
        sum_y: float = sum(y_exp)
        sum_x2: float = sum(i ** 2 for i in x_exp)
        sum_y2: float = sum(i ** 2 for i in y_exp)
        sum_xy: float = sum(x_exp[i] * y_exp[i] for i in range(n))

        # Нахождение искомой зависимости
        b2: float = (sum_xy * n - sum_x * sum_y) / (sum_x2 * n - sum_x ** 2)
        b1: float = (sum_y - b2 * sum_x) / n

        # Нахождение коэффицента детерминации R
        r = (n * sum_xy - sum_x * sum_y) / pow((n * sum_x2 - pow(sum_x, 2)) * (n * sum_y2 - pow(sum_y, 2)), 0.5)

        # Нахождение средней ошибки аппроксимации
        a = 1 / n * sum(abs((y_exp[i] - linear_func(x_exp[i], b1, b2)) / y_exp[i]) for i in range(n))

        print(f'Method MNK (linear):    y = {b2:.3f}x + {b1:.3f}', file=out_file)
        print(f'R = {r ** 2:.5f}', file=out_file)
        print(f'Approximate error: {a:.2%}', file=out_file)


def main() -> str | int:
    try:
        with open('input_data.txt', 'r') as inputFile:
            x: list = [float(i) for i in inputFile.readline().split()]
            y: list = [float(i) for i in inputFile.readline().split()]

    except FileNotFoundError:
        return 'Не удалось открыть файл'

    method_mnk(x, y)
    method_linear_regression(x, y)

    return 0


if __name__ == '__main__':
    main()
