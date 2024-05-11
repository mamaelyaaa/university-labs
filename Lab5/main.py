def finding_dependence(x: float, b1: float, b2: float) -> float:
    return b1 + b2 * x


def method_mnk(x: list, y: list) -> None:
    n: int = len(x)

    # Промежуточные вычисления
    sum_x: float = sum(x)
    sum_y: float = sum(y)
    sum_xx: float = sum(i ** 2 for i in x)
    sum_xy: float = sum(x[i] * y[i] for i in range(n))

    # Нахождение искомой зависимости (через линейную функцию)
    b2: float = (sum_xy * n - sum_x * sum_y) / (sum_xx * n - sum_x ** 2)
    b1: float = (sum_y - b2 * sum_x) / n

    # Создаем систему уравнений и заполняем массив для метода Гаусса
    slay: list[list] = []
    factor: list = [n] + [sum_x ** i for i in range(2)]
    idx: int = 0

    for i in range(2):
        slay.append([b1 * factor[idx], b2 * factor[idx + 1], sum_y * x[idx] ** i])
        idx += 1

    # Находим R**2
    numerator = sum((y[i] - finding_dependence(x[i], *method_gauss(slay))) ** 2 for i in range(n))
    denominator = sum((y[i] - sum_y * n) ** 2 for i in range(n))

    print(f'Method MNK: y = {method_gauss(slay)[0]:.4f} {method_gauss(slay)[1]:.4f}x')
    print(f'R = {pow(numerator / denominator, 0.5):.5f}')


def method_gauss(slay_arr: list) -> list[int]:
    n: int = len(slay_arr)

    for i in range(n):
        pivot: float = slay_arr[i][i]

        for j in range(i, n + 1):
            slay_arr[i][j] /= pivot

        for k in range(i + 1, n):
            factor = slay_arr[k][i]

            for j in range(i, n + 1):
                slay_arr[k][j] -= factor * slay_arr[i][j]

    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = slay_arr[i][-1]
        for j in range(i + 1, n):
            x[i] -= slay_arr[i][j] * x[j]

    return x


def main() -> str | int:
    try:
        with open('input_data.txt', 'r') as inputFile:
            x_exp: list = [float(i) for i in inputFile.readline().split()]
            y_exp: list = [float(i) for i in inputFile.readline().split()]

    except FileNotFoundError:
        return 'Не удалось открыть файл'

    method_mnk(x_exp, y_exp)
    return 0


if __name__ == '__main__':
    main()
