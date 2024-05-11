from random import randint
from time import time

N = 10000


def generation() -> None:
    with open("input.txt", 'w') as file:
        for _ in range(N):
            print(randint(-25000, 25000), file=file, end=' ')


with open('input.txt', 'r') as file_input:
    arr: list[int] = list(map(int, file_input.readline().split()))


def method_simple_sort() -> None:
    start_time = time()
    swaps_count: int = 0

    global arr
    a: list[int] = arr.copy()

    for i in range(len(a) - 1):
        min_el = a.index(min(a[i:]))
        if a[i] > min_el:
            a[i], a[min_el] = a[min_el], a[i]
            swaps_count += 1

    end_time = time()
    with open("time.txt", 'w') as time_file:
        print(f'Simple time: {end_time - start_time: .2f} sec', file=time_file)
    with open("swaps.txt", 'w') as swaps_file:
        print(f'Simple swaps_count: {swaps_count}', file=swaps_file)


def method_bubble() -> None:
    start_time = time()
    swaps_count: int = 0

    global arr
    a: list[int] = arr.copy()

    count: int = 1

    while count > 0:
        count = 0
        for i in range(len(a) - 1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                count += 1
                swaps_count += 1

    end_time = time()
    with open("time.txt", 'a') as time_file:
        print(f'Bubble time: {end_time - start_time: .2f} sec', file=time_file)
    with open("swaps.txt", 'a') as swaps_file:
        print(f'Bubble swaps_count: {swaps_count}', file=swaps_file)


def method_comb_sort() -> None:
    start_time = time()
    swaps_count: int = 0

    global arr
    a: list[int] = arr.copy()

    fact: float = 1.247
    step: float = len(arr) - 1

    while step >= 1:
        for i in range(int(len(a) - step)):
            if a[i] > a[int(i + step)]:
                a[i], a[int(i + step)] = a[int(i + step)], a[i]
                swaps_count += 1
        step /= fact

    end_time = time()

    with open("time.txt", 'a') as time_file:
        print(f'Comb time: {end_time - start_time: .2f} sec', file=time_file)
    with open("swaps.txt", 'a') as swaps_file:
        print(f'Comb swaps_count: {swaps_count}', file=swaps_file)


def method_shaker_sort() -> None:
    start_time = time()
    swaps_count: int = 0

    global arr
    a: list[int] = arr.copy()

    p_left: int = 0
    p_right: int = len(a) - 1
    flag: int = 1

    while p_left < p_right and flag:
        flag = 0

        for i in range(p_left, p_right):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                flag = 1
                swaps_count += 1
        p_right -= 1

        for i in range(p_right, p_left, -1):
            if a[i] < a[i - 1]:
                a[i], a[i - 1] = a[i - 1], a[i]
                flag = 1
                swaps_count += 1
        p_left += 1

        if not flag:
            break
    end_time = time()

    with open("time.txt", 'a') as time_file:
        print(f'Shaker time: {end_time - start_time: .2f} sec', file=time_file)
    with open("swaps.txt", 'a') as swaps_file:
        print(f'Shaker swaps_count: {swaps_count}', file=swaps_file)


def main() -> int:
    generation()
    method_simple_sort()
    method_bubble()
    method_comb_sort()
    method_shaker_sort()
    return 0


if __name__ == '__main__':
    main()
