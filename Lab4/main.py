EXP_ANS: dict = {'a': -43.24231639,
                 'b': -3.197390354,
                 'c': -43.80095293,
                 'd': -37.24317186,
                 'e': 1.523063199}


def read_file() -> tuple | str:
    try:
        with open('input_data.txt', 'r') as inputFile:
            slay_arr: list = [list(map(float, row.split())) for row in inputFile.readlines()]
            n: int = len(slay_arr)  # Rows

            return slay_arr, n

    except FileNotFoundError:
        raise 'Не удалось открыть файл'


def method_gauss() -> None:
    matrix: list = read_file()[0]  # A,B matrix
    n: int = read_file()[1]

    with open('answer_data.txt', 'w') as output_file:
        error: float = 0  # Погрешность в сравнении с калькулятором

        for i in range(n):
            pivot: float = matrix[i][i]

            for j in range(i, n + 1):
                matrix[i][j] /= pivot

            for k in range(i + 1, n):
                factor = matrix[k][i]

                for j in range(i, n + 1):
                    matrix[k][j] -= factor * matrix[i][j]

        x = [0] * n
        for i in range(n - 1, -1, -1):
            x[i] = matrix[i][-1]
            for j in range(i + 1, n):
                x[i] -= matrix[i][j] * x[j]

        print('Method Gauss:        ', file=output_file, end=' ')

        for key, value in zip('abcde', x):
            print(f'{key} = {value: .4f}', file=output_file, end=' ')
            error = max(error, abs(value - EXP_ANS[key]))

        print(f'\nmax {error = : .10f}', file=output_file)


def method_gauss_zeidel() -> None:
    matrix: list = read_file()[0]  # A,B matrix
    n: int = read_file()[1]

    x = [0] * n  # Начальное приближение
    tol = 0.0001

    with open('answer_data.txt', 'a') as output_file:
        flag = 0
        error: float = 0

        for _ in range(1000):
            if flag:
                break
            x_new = x.copy()

            for i in range(n):
                sum_aix = sum(matrix[i][j] * x_new[j] for j in range(n) if j != i)
                x_new[i] = (matrix[i][-1] - sum_aix) / matrix[i][i]

            if all(abs(x_new[i] - x[i]) < tol for i in range(n)):
                flag = 1
            x = x_new

        print('\nMethod Gauss-Zeidel: ', file=output_file, end=' ')

        for key, value in zip('abcde', x):
            print(f'{key} = {value: .4f}', file=output_file, end=' ')
            error = max(error, abs(value - EXP_ANS[key]))

        print(f'\nmax {error = : .10f}', file=output_file)


def main() -> int:
    method_gauss()
    method_gauss_zeidel()
    return 0


if __name__ == '__main__':
    main()
