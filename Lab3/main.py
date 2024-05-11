x_approximate_val: float = 5.5


def method_euler(h: float) -> None:
    with open('output.txt', "a", encoding='UTF-8') as output_file:
        print(f'h = {h}', file=output_file)

        x: list[float] = [1.0]  # x0
        y: list[float] = [1.0]  # y0

        for i in range(int(x_approximate_val // h) + 1):
            y.append(round(y[i] + h * f(x[i], y[i]), 3))
            x.append(round(x[i] + h, 2))

        zip_values: dict = {x: y for x, y in zip(x, y)}

        print(f'x =     {x_approximate_val}', file=output_file)
        print(f'y_e =  {zip_values[x_approximate_val]}', file=output_file)


def method_euler_mod(h: float) -> None:
    with open('output.txt', "a", encoding='UTF-8') as output_file:
        x: list[float] = [1.0]
        y: list[float] = [1.0]

        for i in range(int(x_approximate_val // h) + 1):
            x_mod: float = x[i] + h / 2
            y_mod: float = y[i] + h / 2 * f1(x[i], y[i])

            y.append(round(y[i] + h * f(x_mod, y_mod), 3))
            x.append(round(x[i] + h, 2))

        zip_values: dict = {x: y for x, y in zip(x, y)}

        print(f'y_em = {zip_values[x_approximate_val]}', file=output_file)


def method_euler_improve(h: float) -> None:
    with open('output.txt', "a", encoding='UTF-8') as output_file:
        x: list[float] = [1.0]
        y: list[float] = [1.0]

        for i in range(int(x_approximate_val // h) + 1):
            y_mod: float = y[i] + h / 2 * f1(x[i], y[i])

            y.append(round(y[i] + h * f(x[i], y_mod), 3))
            x.append(round(x[i] + h, 2))

        zip_values: dict = {x: y for x, y in zip(x, y)}

        print(f'y_ei = {zip_values[x_approximate_val]}', file=output_file)


def method_runge_kutt(h: float) -> None:
    with open('output.txt', "a", encoding='UTF-8') as output_file:
        x: list[float] = [1.0]
        y: list[float] = [1.0]

        for i in range(int(x_approximate_val // h) + 1):
            k1: float = f(x[i], y[i])
            k2: float = f(x[i] + 0.25 * h, y[i] + 0.25 * h * k1)
            k3: float = f(x[i] + 0.25 * h, y[i] + 0.125 * h * k1 + 0.125 * h * k2)
            k4: float = f(x[i] + 0.5 * h, y[i] - 0.5 * h * k2 + h * k3)
            k5: float = f(x[i] + 0.75 * h, y[i] + 0.1875 * h * k1 + 0.5625 * h * k4)
            k6: float = f(x[i] + h, y[i] - 3 / 20 * h * k1 + 3 / 4 * h * k4 + 3 / 5 * h * k5)

            y.append(round(y[i] + h * (7 / 90 * k1 + 32 / 90 * k3 + 12 / 90 * k4 + 32 / 90 * k5 + 7 / 90 * k6), 3))
            x.append(round(x[i] + h, 2))

        zip_values: dict = {x: y for x, y in zip(x, y)}

        print(f'y_rk = {zip_values[x_approximate_val]}\n', file=output_file)


def f(x: float, y: float) -> float:  # Variant 24
    return y / x - (2 * x) / x ** 2


def f1(x: float, y: float) -> float:
    return (f(x, y) * x - (y - 2)) / x ** 2


def main() -> int:
    with open('output.txt', 'w') as file:
        file.truncate()

    step: list[float] = [0.5, 0.1, 0.01]

    for h in step:
        method_euler(h)
        method_euler_mod(h)
        method_euler_improve(h)
        method_runge_kutt(h)
    return 0


if __name__ == '__main__':
    main()
