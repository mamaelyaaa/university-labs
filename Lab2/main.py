# -*- coding: utf-8 -*-

import numpy as np


A: float = -0.4  # Left border
B: float = 0.8  # Right border
E: float = 0.0001

expectedIntegralRes: float = 0.117517


def method_right_rectangle() -> None:
    with open('output.txt', 'w') as outputFile:
        n: int = 20
        h: float = (B - A) / n
        sum1: float = 0
        sum2: float = 0

        for i in range(n):
            sum1 += h * f(A + (i + 1) * h)

        while abs(sum1 - sum2) >= E:
            sum1: float = 0
            n *= 2
            h = (B - A) / n

            for i in range(n):
                sum1 += h * f(A + (i + 1) * h)
            sum2 = sum1

        print(f'Method right rectangle:  res = {sum1: 2.6f}, {n = }, {h = :.2f}', file=outputFile)


def method_left_rectangle() -> None:
    with open('output.txt', 'a') as outputFile:
        n: int = 20
        h: float = (B - A) / n
        sum1: float = 0
        sum2: float = 0

        for i in range(n):
            sum1 += h * f(A + i * h)

        while abs(sum1 - sum2) >= E:
            sum1: float = 0
            n *= 2
            h = (B - A) / n

            for i in range(n):
                sum1 += h * f(A + i * h)
            sum2 = sum1

        print(f'Method left rectangle:   res = {sum1: .6f}, {n = }, {h = :.2f}', file=outputFile)


def method_middle_rectangle() -> None:
    with open('output.txt', 'a') as outputFile:
        n: int = 20
        h: float = (B - A) / n
        sum1: float = 0
        sum2: float = 0

        for i in range(n):
            sum1 += h * f(A + (2 * i + 1) / 2 * h)

        while abs(sum1 - sum2) >= E:
            sum1: float = 0
            n *= 2
            h = (B - A) / n

            for i in range(n):
                sum1 += h * f(A + (2 * i + 1) / 2 * h)
            sum2 = sum1
        print(f'Method middle rectangle: res = {sum1: .6f}, {n = }, {h = :.2f}', file=outputFile)


def method_trapeze() -> None:
    with open('output.txt', 'a') as outputFile:
        n: int = 20
        h: float = (B - A) / n
        sum1: float = 0
        sum2: float = 0

        for i in range(n):
            sum1 += h * ((f(A + i * h) + f(A + (i + 1) * h)) / 2)

        while abs(sum1 - sum2) >= E:
            sum1: float = 0
            n *= 2
            h = (B - A) / n

            for i in range(n):
                sum1 += h * ((f(A + i * h) + f(A + (i + 1) * h)) / 2)
            sum2 = sum1
        print(f'Method trapeze:          res = {sum1: .6f}, {n = }, {h = :.2f}', file=outputFile)


def method_simpson() -> None:
    with open('output.txt', 'a') as outputFile:
        n: int = 20
        h: float = (B - A) / (2 * n)
        sum1: float = 0
        sum2: float = 0

        for i in range(n):
            sum1 += h / 3 * (f(A + 2 * i * h) + 4 * f(A + (2 * i + 1) * h) + f(A + (2 * i + 2) * h))

        while abs(sum1 - sum2) >= E:
            sum1: float = 0
            n *= 2
            h = (B - A) / (2 * n)

            for i in range(n):
                sum1 += h / 3 * (f(A + 2 * i * h) + 4 * f(A + (2 * i + 1) * h) + f(A + (2 * i + 2) * h))
            sum2 = sum1

        print(f'Method simpson:          res = {sum1: .6f}, {n = }, {h = :.2f}',
              file=outputFile)


def method_gauss_quadrature() -> None:
    with open('output.txt', 'a') as outputFile:
        n = 20
        # Получение узлов и весов для полиномов Лежандра
        x, w = np.polynomial.legendre.leggauss(n)

        # Преобразование узлов на интервал [a, b]
        t = 0.5 * (x + 1) * (B - A) + A

        res_integral = 0.5 * (B - A) * sum(w * f(t))

        print(f'Method Gauss-Quadrature: res = {res_integral: .6f}, {n = }',
              file=outputFile)


def f(x: float) -> float:
    return x ** 2 / (4 * x ** 3 + 1)


def main() -> int:
    method_right_rectangle()
    method_left_rectangle()
    method_middle_rectangle()
    method_trapeze()
    method_simpson()
    method_gauss_quadrature()
    return 0


if __name__ == '__main__':
    main()
